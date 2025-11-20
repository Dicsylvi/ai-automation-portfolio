import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def load_prompt():
    with open("business_chatbot_prompt.txt", "r") as f:
        return f.read()

if __name__ == "__main__":
    prompt = load_prompt().replace("{{business_name}}", "Sunrise Beauty Salon")

    user_question = "Hi, how much is a silk press and do you take walk-ins?"

    response = openai.ChatCompletion.create(
        model="gpt-4.1",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": user_question},
        ]
    )

    print(response["choices"][0]["message"]["content"])
