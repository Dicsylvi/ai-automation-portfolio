# Small Business AI Chatbot

An AI-powered customer service assistant designed for small businesses.  
This chatbot can answer FAQs, schedule appointments, collect customer information, and respond to pricing or service inquiries.

It is fully customizable for any niche such as real estate, beauty salons, repair shops, fitness trainers, consultants, photographers, and more.

---

## 🔥 Features

✔ Friendly, professional customer service  
✔ Answer FAQs and provide business information  
✔ Handle pricing inquiries  
✔ Book/schedule appointments  
✔ Collect customer details  
✔ Ask follow-up questions for clarity  
✔ Fully customizable via prompt templates  
✔ Runs with any OpenAI-compatible model  

---

## 🧠 How It Works (Architecture)

Below is a simple flow diagram (GitHub-friendly):


        +-----------------------+
        |  User Asks a Question |
        +-----------+-----------+
                    |
                    v
        +-----------------------+
        |   Chatbot Prompt      |
        |  (business rules)     |
        +-----------+-----------+
                    |
                    v
        +-----------------------+
        | OpenAI Model (GPT-X) |
        | Processes Query       |
        +-----------+-----------+
                    |
                    v
        +-----------------------+
        |  Chatbot Response     |
        | (pricing, booking,    |
        |  FAQs, follow-ups)    |
        +-----------------------+


