from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

SYSTEM_PROMPT = """
You are an IPL analyst.

Explain cricket strategies.
Compare players.
Use statistics when possible.
"""

messages = [
    {"role": "system", "content": SYSTEM_PROMPT}
]

while True:
    user_question = input("\nYou: ")

    if user_question.lower() == "exit":
        break

    messages.append(
        {"role": "user", "content": user_question}
    )

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )

    answer = response.choices[0].message.content

    print("\nBot:", answer)

    messages.append(
        {"role": "assistant", "content": answer}
    )