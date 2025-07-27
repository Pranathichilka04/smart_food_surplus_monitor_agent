
markdown
Copy
Edit
# 🧠 Smart Food Waste AI – Voice-Enabled Surplus Optimization

A voice-assisted, AI-powered platform to help retail stores reduce **perishable food waste** through smart **prediction, redistribution, and donation**.

> 💡 Built for Sparkathon 2025 – under the theme **"Building a Sustainable Retail Future"**.

---

## 🚀 Features

🔍 **Surplus Predictor**  
Predicts stock likely to expire based on sales trends, shelf life, and current inventory.

🎤 **Voice Assistant (AI Agent)**  
Retailers and NGO partners can ask natural questions like:
- “How many carrots are expiring soon?”
- “Which store has the highest surplus?”
- “What can be donated today?”

📊 **Impact Dashboard**  
- Waste prevented (kg)  
- Items redistributed or discounted  
- Carbon emissions saved  
- Meals donated

🔔 **Smart Triggers**  
- Suggests redistribution to nearby stores  
- Activates discount strategy for at-risk items  
- Alerts NGO for donation pickups

🎙️ **Optional Voice Output**  
Enable voice replies using `pyttsx3` for accessibility.

---

## 💡 How It Works

1. 📥 Upload or connect real-time inventory data (CSV mock used in MVP).
2. 🤖 ML model forecasts demand and flags at-risk items.
3. 🧠 AI agent helps staff ask questions using natural language.
4. 📈 Store/NGO users can visualize insights and act accordingly.

---

## 🧱 Tech Stack

| Layer       | Tech                     |
|-------------|--------------------------|
| Frontend    | Streamlit                |
| Voice Input | SpeechRecognition (Google API) |
| Backend     | Python, Pandas           |
| AI Agent    | MockAgent / OpenAI (via `langchain`) |
| Visualization | Matplotlib, Seaborn    |
| Hosting     | Replit / Streamlit Cloud |
| Version Control | Git + GitHub         |

---

## 📂 Project Structure

smart-food-waste-ai/
├── ui/
│ └── app_streamlit.py # Main app UI
├── model/
│ └── predictor.py # Surplus prediction logic
├── aiagent/
│ └── agent.py # Voice agent logic
├── data/
│ └── inventory.csv # Sample dataset
├── requirements.txt # Python dependencies
├── .env # 🔐 Secret API keys (not pushed)
└── README.md

yaml
Copy
Edit

---

## 🧪 Sample Questions for AI Agent

- "Which items will expire in 2 days?"
- "What should I donate today?"
- "Tell me the weekly summary"
- "Is Store A overstocked on milk?"

---

## 🔐 Setup (Dev)

```bash
git clone https://github.com/<your-username>/smart-food-waste-ai.git
cd smart-food-waste-ai
pip install -r requirements.txt
streamlit run ui/app_streamlit.py
Set your .env:

ini
Copy
Edit
OPENAI_API_KEY=your_key_here
🌐 Live Demo
📍 Coming Soon – Hosted on Streamlit Cloud

🤝 Team
🧠 AI Agent – Pranathi Chilka

🧮 Prediction Model – [Your team member]

🎨 UI/UX & Voice – [Your team member]

🌍 Sustainability Strategy – [Your team member]

📣 Submission Tagline
“Helping retailers act before food expires, not after — with AI that listens, thinks, and prevents waste.”

🏁 For Judges
✅ Fully working MVP
✅ Replit / Streamlit Cloud deployable
✅ Code & model modularized
✅ AI-enhanced user experience
✅ Real-time simulation on sample data

📬 Contact
🔗 GitHub: github.com/<your-username>
📧 Email: your-email@example.com

