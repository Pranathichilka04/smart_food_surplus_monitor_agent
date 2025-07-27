import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from dotenv import load_dotenv

# Voice input (optional - use only if mic support exists)
import speech_recognition as sr
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from model.predictor import predict_surplus

# Load environment variables
load_dotenv()

# Load AI Agent
try:
    from aiagent.agent import load_agent
    agent = load_agent()
    agent_error = None
except Exception as e:
    agent = None
    agent_error = str(e)

# ------------------------------
# 🎉 App Introduction Section
# ------------------------------
st.set_page_config(page_title="Smart Food Waste AI Assistant", layout="centered")
st.title("🛒 Smart Food Surplus Prevention System")
st.markdown("""
Welcome to the **Smart Food Waste Assistant** 👋

This AI-powered tool helps **retailers and NGOs** reduce food waste by:
- 📦 **Predicting surplus inventory**
- 🧠 **Suggesting actions** (Redistribute / Discount / Donate)
- 🎙️ **Answering your questions** with a conversational agent
- 📊 **Visualizing insights** with real-time charts

**How to use:**
1. View or ask surplus-related questions (text or voice).
2. Explore visual dashboards on surplus and expiry trends.
3. Take informed action based on suggestions.
""")

st.markdown("---")

# ------------------------------
# Role Selector
# ------------------------------
user_type = st.selectbox("🔐 Login as", ["Store Manager", "NGO Partner"])

# ------------------------------
# Question Input Section
# ------------------------------
st.markdown("### 🔍 Ask a Question")
text_query = st.text_input("Type here or use the voice recorder below",
                           key="text_input")

# Voice Input (optional)
st.markdown("#### 🎙️ Speak a Question (click and talk)")
if st.button("🎧 Start Recording"):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening...")
        audio = r.listen(source)
        try:
            spoken_text = r.recognize_google(audio)
            st.success(f"You said: {spoken_text}")
            text_query = spoken_text
        except:
            st.error("Sorry, I couldn't understand your voice.")

# ------------------------------
# Run Agent
# ------------------------------
if text_query:
    if agent:
        with st.spinner("Analyzing with AI..."):
            try:
                response = agent.run(text_query)
                st.success("✅ AI Response:")
                st.write(response)
            except Exception as e:
                st.error(f"Error running agent: {str(e)}")
    else:
        st.warning("AI agent not available.")
        st.error(f"Agent Error: {agent_error}")

# ------------------------------
# Load Surplus Data
# ------------------------------
try:
    df = pd.read_csv("data/surplus_predictions.csv")
    data_available = True
except FileNotFoundError:
    st.warning("📂 Surplus predictions not found. Please run the predictor model.")
    data_available = False
    df = None

# ------------------------------
# Dashboard
# ------------------------------
st.markdown("---")
st.markdown("### 📊 Insights Dashboard")

if data_available and df is not None:
    if user_type == "Store Manager":
        if st.button("📦 Show Surplus by Store"):
            fig, ax = plt.subplots()
            sns.barplot(data=df,
                        x="store",
                        y="surplus_units",
                        hue="suggested_action",
                        ax=ax)
            ax.set_title("Surplus by Store & Action")
            st.pyplot(fig)

        if st.button("⏳ Expiry Breakdown"):
            fig, ax = plt.subplots()
            sns.histplot(data=df, x="days_to_expiry", bins=10, kde=True)
            ax.set_title("Items by Days to Expiry")
            st.pyplot(fig)

    elif user_type == "NGO Partner":
        st.markdown("#### 📥 Upcoming Donations")
        donations = df[df["suggested_action"] == "Donate"]
        if not donations.empty:
            st.dataframe(donations[["item", "store", "expiry_date", "surplus_units"]])
        else:
            st.info("No donations available currently.")
else:
    st.info("Dashboard data not available.")
