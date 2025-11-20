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

## 📂 Project Structure

small-business-chatbot/
│
├── README.md
├── chatbot_runner.py
├── business_chatbot_prompt.txt
└── sample_conversations.md


---

## 🚀 Getting Started

### 1. Install dependencies

pip install openai

### 2. Add your API key
Set environment variable:

export OPENAI_API_KEY="your_key_here"

### 3. Run the chatbot

python3 chatbot_runner.py


---

## 📝 Customize the Chatbot

Open the file:

business_chatbot_prompt.txt

Replace: {{business_name}}


With any business type. Examples:
- Sunrise Beauty Salon  
- J&M Auto Repair  
- CloudFix Tax Services  
- FitWell Personal Training  

---

## 💼 Example Use Cases

### Beauty Salon  
- Prices for hairstyles  
- Booking appointments  
- Product recommendations  

### Real Estate Agent  
- Property descriptions  
- Open house schedules  
- Collecting buyer info  

### Auto Repair Shop  
- Service pricing  
- Diagnostics  
- Drop-off instructions  

### Fitness Trainer  
- Class schedules  
- Membership pricing  
- Trial sessions  

---

## 💬 Sample Conversation (See sample_conversations.md)

Customer: "How much is a silk press?"  
Bot: "Our silk press service is $95, including shampoo and hydration. Would you like to book?"  

---

With any business type. Examples:
- Sunrise Beauty Salon  
- J&M Auto Repair  
- CloudFix Tax Services  
- FitWell Personal Training  

---

## 💼 Example Use Cases

### Beauty Salon  
- Prices for hairstyles  
- Booking appointments  
- Product recommendations  

### Real Estate Agent  
- Property descriptions  
- Open house schedules  
- Collecting buyer info  

### Auto Repair Shop  
- Service pricing  
- Diagnostics  
- Drop-off instructions  

### Fitness Trainer  
- Class schedules  
- Membership pricing  
- Trial sessions  

---

## 💬 Sample Conversation (See sample_conversations.md)

Customer: "How much is a silk press?"  
Bot: "Our silk press service is $95, including shampoo and hydration. Would you like to book?"  

---





