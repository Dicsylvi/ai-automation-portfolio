import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def load_prompt():
    with open("business_chatbot_prompt.txt", "r") as f:
        return f.read()

prompt = load_prompt().replace("{{business_name}}", "Sunrise Beauty Salon")

messages = [
    {"role": "system", "content": prompt}
]

print("Chatbot ready! Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    messages.append({"role": "user", "content": user_input})

    response = openai.ChatCompletion.create(
        model="gpt-4.1",
        messages=messages
    )

    bot_reply = response["choices"][0]["message"]["content"]
    print("Bot:", bot_reply)

    messages.append({"role": "assistant", "content": bot_reply})
