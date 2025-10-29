import os
import requests
from dotenv import load_dotenv
from mem0 import MemoryClient

# ---------------------------------------------------------------------
# 1️⃣ Setup
# ---------------------------------------------------------------------
load_dotenv()

MEM0_API_KEY = os.getenv("MEM0_API_KEY")
MEM0_USER_EMAIL = os.getenv("MEM0_USER_EMAIL")
MEM0_ORG_ID = os.getenv("MEM0_ORG_ID")
MEM0_PROJECT_ID = os.getenv("MEM0_PROJECT_ID")

VANNA_API_KEY = os.getenv("VANNA_API_KEY")
VANNA_USER_EMAIL = os.getenv("VANNA_USER_EMAIL")

if not all([MEM0_API_KEY, MEM0_USER_EMAIL, MEM0_ORG_ID, MEM0_PROJECT_ID, VANNA_API_KEY, VANNA_USER_EMAIL]):
    raise ValueError("❌ Missing one or more required environment variables in .env file.")

mem0_client = MemoryClient(
    api_key=MEM0_API_KEY,
    org_id=MEM0_ORG_ID,
    project_id=MEM0_PROJECT_ID
)

# ---------------------------------------------------------------------
# 2️⃣ Helper functions
# ---------------------------------------------------------------------
def get_user_memories():
    """Fetch and return user preferences from Mem0."""
    try:
        memories = mem0_client.search(query="preferences", filters={"user_id": MEM0_USER_EMAIL})
        results = memories.get("results", [])
        return [m["memory"] for m in results]
    except Exception as e:
        print(f"⚠️ Error retrieving memories: {e}")
        return []


def add_new_preference():
    """Prompt the user to add a new preference."""
    print("\nWould you like to add any new preferences? (press Enter to skip)")
    new_pref = input("➡️  Your new preference: ").strip()

    if new_pref:
        try:
            messages = [{"role": "user", "content": new_pref}]
            mem0_client.add(messages, user_id=MEM0_USER_EMAIL, version="v2")
            print("✅ New preference added to memory!")
        except Exception as e:
            print(f"⚠️ Error adding preference: {e}")
    else:
        print("👍 No new preferences added.")


def query_vanna_with_context(question, memories):
    """Send question + memory context to Vanna API and display the answer."""
    context = "\n".join(f"- {m}" for m in memories) if memories else "No stored preferences."

    message = f"""
The user has the following preferences:
{context}

Now answer this question based on those preferences:
{question}
""".strip()

    print("\n🔍 Querying Vanna API...\n")

    payload = {
        "message": message,
        "user_email": VANNA_USER_EMAIL,
        "acceptable_responses": ["text"]
    }

    headers = {
        "Content-Type": "application/json",
        "VANNA-API-KEY": VANNA_API_KEY
    }

    try:
        response = requests.post("https://app.vanna.ai/api/v2/chat_sse", headers=headers, json=payload)
        response.raise_for_status()
        print("💬 Response from Vanna:\n")
        print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"⚠️ Error calling Vanna API: {e}")


# ---------------------------------------------------------------------
# 3️⃣ Main flow
# ---------------------------------------------------------------------
def main():
    print("🤖 Checking what I already know about you...\n")
    user_memories = get_user_memories()

    if user_memories:
        print("🧠 Here are your current preferences:\n")
        for i, m in enumerate(user_memories, 1):
            print(f"  {i}. {m}")
    else:
        print("No preferences stored yet.")

    add_new_preference()

    print("\nNow, what question would you like to ask?")
    question = input("❓ Your question: ").strip()
    if not question:
        print("No question entered. Exiting.")
        return

    query_vanna_with_context(question, user_memories)


# ---------------------------------------------------------------------
# 4️⃣ Run
# ---------------------------------------------------------------------
if __name__ == "__main__":
    main()
