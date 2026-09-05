import os
from dotenv import load_dotenv
from sarvamai import SarvamAI

load_dotenv()

api_key = os.getenv("API_KEY")

if not api_key:
    raise ValueError("API_KEY is not set")

client = SarvamAI(api_subscription_key=api_key)

prompt = """
You are a confidential, empathetic legal navigator focused on women's rights in India.
Your job is to help users understand their legal rights in simple, direct, concise language.
You are not a substitute for a qualified lawyer.

CRITICAL INSTRUCTION:
Do NOT output your internal reasoning, thought process, or planning notes. 
Start your response directly with your final reply to the user.

## LANGUAGE
* Respond in the same language and script used by the user (English, Hindi, Hinglish, Tamil, Telugu, etc.).

## GENERAL QUESTIONS
Briefly explain the relevant areas of women's legal rights in India and ask what specific situation they are facing.

## INCIDENT REPORTS
When the user describes a specific incident, provide exactly these two sections:

SECTION 1: LEGAL VIOLATIONS
* Identify applicable Indian laws (e.g., POSH Act 2013, Code on Wages, IPC/BNS provisions).
* Explain legal categories simply without claiming a definite violation unless established.

SECTION 2: ACTIONABLE NEXT STEPS
* Explain practical steps: Internal Committee (IC) / Local Committee (LC) process.
* Detail useful evidence (WhatsApp messages, emails, witness details).
* Explain interim protections and report avenues.

## SAFETY
* Prioritize safety if user is in immediate danger.
* Do not invent laws or deadlines.
"""

print("=" * 60)
print("          WOMEN'S RIGHTS LEGAL NAVIGATOR")
print("=" * 60)
print("I can help you understand women's legal rights in India.")
print("Type 'exit' or 'quit' to close the program.")
print("-" * 60)

while True:
    try:
        user_input = input("\nYou: ")
    except KeyboardInterrupt:
        print("\n\nNavigator: Goodbye!")
        break

    if user_input.strip().lower() in ["exit", "quit"]:
        print("\nNavigator: Goodbye. Take care!")
        break

    if not user_input.strip():
        print("Navigator: Please enter your question.")
        continue

    try:
        response = client.chat.completions(
            model="sarvam-105b",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": user_input},
            ],
            max_tokens=2048,
            reasoning_effort=None,
        )

        choice = response.choices[0]
        
        bot_reply = choice.message.content
        
        if bot_reply and bot_reply.strip():
            print("\nNavigator:")
            print(bot_reply.strip())
        else:
            print("\nNavigator: Received empty response from API. Please try rephrasing your question.")

    except Exception as e:
        print("\nNavigator: Something went wrong.")
        print(f"Technical error: {e}")

    print("\n" + "-" * 60)