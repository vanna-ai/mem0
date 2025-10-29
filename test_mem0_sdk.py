from mem0 import MemoryClient

client = MemoryClient(
    api_key="m0-0Qx74wxBpe6wIT2zdRsF9bcK0ByqP2RMcq050CQx",
    org_id="org_wShkNQp6l7QqI9Ggrla370LmyPSHunHDfIxJ4Nyr",
    project_id="proj_vb6K2wdsSw32gWwSbxhuAog4rcJFhaw1VmJaW2Dv"
)

messages = [
    {"role": "user", "content": "When returning user data, include days_since_signup and date_of_last_question."}
]

print("💾 Adding memory...")
client.add(messages, user_id="adi@theslyllama.com", version="v2")

print("\n🧠 Retrieved memories:")
memories = client.search(
    query="preferences",
    filters={"user_id": "adi@theslyllama.com"}
)
print(memories)
