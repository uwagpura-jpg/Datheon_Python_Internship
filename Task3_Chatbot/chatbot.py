import json
import re
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo

FAQ_FILE = Path("faqs.json")

DEFAULT_FAQS = {
    "hours": "Our working hours are Monday to Friday, 9 AM to 5 PM.",
    "services": "We provide Python programming and software development services.",
    "contact": "You can contact us through our official website.",
    "internship": "Please check our official website for internship updates."
}

INTENT_PATTERNS = {
    "hours": r"\b(hours?|timings?|open|closed|business hours)\b",
    "services": r"\b(services?|products?|offer|offers|provide)\b",
    "contact": r"\b(contact|email|phone|support)\b",
    "internship": r"\b(internship|internships|certificate|application)\b",
    "time": r"\b(time|clock)\b",
    "date": r"\b(date|today|day)\b"
}


def load_faqs():
    if FAQ_FILE.exists():
        try:
            with FAQ_FILE.open("r", encoding="utf-8") as file:
                data = json.load(file)

            if isinstance(data, dict):
                faqs = DEFAULT_FAQS.copy()
                faqs.update({
                    str(key).lower(): str(value)
                    for key, value in data.items()
                })
                return faqs

        except (json.JSONDecodeError, OSError):
            print("Warning: Could not read FAQs. Using default FAQs.")

    return DEFAULT_FAQS.copy()


def get_response(message, faqs):
    message = message.lower().strip()

    if not message:
        return "Please enter a message."

    if re.search(r"\b(hello|hi|hey)\b", message):
        if message in ("hello", "hi", "hey"):
            return "Hello! Welcome to our chatbot."

    if re.search(r"\b(how are you)\b", message):
        return "I'm doing great! How can I help you?"

    if re.search(r"\b(help|what can you do)\b", message):
        return (
            "You can ask about business hours, services, contact, "
            "internships, time, or date. Type 'bye' to exit."
        )

    matched_intents = []

    for intent, pattern in INTENT_PATTERNS.items():
        if re.search(pattern, message):
            matched_intents.append(intent)

    responses = []

    for intent in matched_intents:
        if intent == "time":
            current_time = datetime.now(
                ZoneInfo("Asia/Kolkata")
            )
            responses.append(
                f"Current time in India: "
                f"{current_time.strftime('%I:%M %p')} IST."
            )

        elif intent == "date":
            current_date = datetime.now(
                ZoneInfo("Asia/Kolkata")
            )
            responses.append(
                f"Today's date is {current_date.strftime('%d-%m-%Y')}."
            )

        elif intent in faqs:
            responses.append(faqs[intent])

    if responses:
        return "\n".join(responses)

    return (
        "Sorry, I don't understand that question. "
        "Type 'help' to see what you can ask."
    )


def main():
    faqs = load_faqs()

    print("=" * 40)
    print("      RULE-BASED CHATBOT")
    print("=" * 40)
    print("Hello! I'm your terminal chatbot.")
    print("Type 'help' for options or 'bye' to exit.")

    while True:
        user_input = input("\nYou: ").strip()

        if user_input.lower() in ("bye", "byee", "goodbye", "exit", "quit"):
            print("Bot: Goodbye! Have a nice day.")
            break

        response = get_response(user_input, faqs)
        print(f"Bot: {response}")


if __name__ == "__main__":
    main()
