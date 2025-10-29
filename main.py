import os
import requests
from dotenv import load_dotenv
from mem0 import MemoryClient

# ---------------------------------------------------------------------
# 1️⃣ Load environment variables
# ---------------------------------------------------------------------
load_dotenv()

VANNA_API_KEY = os.getenv("VANNA_API_KEY")
MEM0_API_KEY = os.getenv("MEM0_API_KEY")
MEM0_ORG_ID = os.getenv("MEM0_ORG_ID")
MEM0_PROJECT_ID = os.getenv("MEM0_PROJECT_ID")

# ---------------------------------------------------------------------
# 2️⃣ Initialize Mem0 client
# ---------------------------------------------------------------------
mem0_client = MemoryClient(
    api_key=MEM0_API_KEY,
    org_id=MEM0_ORG_ID,
    project_id=MEM0_PROJECT_ID
)

# ---------------------------------------------------------------------
# 3️⃣ Helper: Retrieve preferences from Mem0
# ---------------------------------------------------------------------
def get_user_memories(user_id: str):
    try:
        response = mem0_client.search(
            query="preferences",
            filters={"user_id": user_id}
        )
        memories = response.get("results", [])
        if not memories:
            print("ℹ️  No memories found for this user.")
            return ""
        print("\n🧠 Retrieved user preferences from Mem0:")
        for m in memories:
            print(f" - {m['memory']}")
        return "\n".join([m["memory"] for m in memories])
    except Exception as e:
        print(f"⚠️  Mem0 fetch error: {e}")
        return ""

# ---------------------------------------------------------------------
# 4️⃣ Helper: Query Vanna
# ---------------------------------------------------------------------
def query_vanna(message: str, user_email: str, mem_context: str):
    url = "https://app.vanna.ai/api/v2/chat_sse"
    headers = {
        "Content-Type": "application/json",
        "VANNA-API-KEY": VANNA_API_KEY
    }

    prompt_with_context = (
        f"User preferences:\n{mem_context}\n\n"
        f"User query: {message}"
    )

    payload = {
        "message": prompt_with_context,
        "user_email": user_email,
        "acceptable_responses": ["text", "dataframe"]
    }

    print("\n📤 Sending query to Vanna...")
    response = requests.post(url, json=payload, headers=headers, stream=True)

    print("\n💬 Vanna response:")
    for line in response.iter_lines():
        if line:
            print(line.decode("utf-8"))

# ---------------------------------------------------------------------
# 5️⃣ Main run
# ---------------------------------------------------------------------
if __name__ == "__main__":
    USER_EMAIL_VANNA = os.getenv("VANNA_USER_EMAIL")
    USER_EMAIL_MEM0 = os.getenv("MEM0_USER_EMAIL")

    memories_text = get_user_memories(USER_EMAIL_MEM0)

    query_vanna(
        message="Show total questions in hosted app for adi@vanna.ai",
        user_email=USER_EMAIL_VANNA,
        mem_context=memories_text
    )
