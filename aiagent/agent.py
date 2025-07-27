# aiagent/agent.py
'''import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI

load_dotenv()


class AIAgent:

    def __init__(self, openai_key):
        if not openai_key:
            raise ValueError("OPENAI_API_KEY not found in environment!")

        self.llm = ChatOpenAI(openai_api_key=openai_key,
                              temperature=0,
                              model_name="gpt-3.5-turbo")

    def run(self, query):
        response = self.llm.invoke(query)
        return response.content


def load_agent():
    openai_key = os.getenv("OPENAI_API_KEY")
    return AIAgent(openai_key)
'''

# aiagent/agent.py


def load_agent():

    class MockAgent:

        def run(self, query):
            query = query.lower()

            # Simulated responses based on keywords
            if "carrots" in query:
                return "🧺 Currently, 120 carrots are in stock. 30 units are expected to expire in 2 days at Store A. Suggestion: trigger donation."

            elif "bread" in query or "milk" in query:
                return "🥖 Store C has 15 bread loaves and 10 milk cartons expiring in 1 day. Suggested Action: Immediate Discount or NGO Alert."

            elif "surplus" in query:
                return "📊 Store B has the highest surplus today: 85 units of vegetables, mostly leafy greens nearing expiry."

            elif "waste" in query or "expired" in query:
                return "♻️ You're projected to waste ~8.4 kg of perishables this week. Suggest increasing markdowns on short-lifespan goods."

            elif "donate" in query:
                return "🎁 Recommended donations: 6 dairy items and 12 bakery products expiring within 24 hrs. Notifying nearest food bank."

            elif "expiry" in query or "expiring" in query:
                return "⏳ 5 items are expiring within 2 days: Spinach, Yogurt, Lettuce, Strawberries, and Milk."

            elif "store with most" in query or "which store" in query:
                return "🏬 Store B has the most surplus and short-lifespan goods this week. Consider redistributing to Store A."

            elif "ngo" in query or "food bank" in query:
                return "🤝 Nearby NGO: 'Food Angels' is available for pickup today between 5–7 PM. Suggested donation: Fruits & Dairy."

            elif "summary" in query or "report" in query:
                return ("📋 Weekly Summary:\n"
                        "- Total surplus: 215 units\n"
                        "- Donations: 3 NGO pickups\n"
                        "- Food waste prevented: 18.5 kg\n"
                        "- Estimated CO₂ saved: 22.7 kg")

            else:
                return f"🤖 Mock AI Response: I received your query — '{query}'. (This is a demo reply. For real AI, connect OpenAI API.)"

    return MockAgent()
