import json
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo

FAQ_FILE = Path("faqs.json")

DEFAULT_FAQS = {
    "hours": "Our working hours are Monday to Friday, 9 AM to 5 PM.",
    "services": "We provide Python programming and software development services.",
    "contact": "You can contact us through our official website.",
    "internship": "Please check the official website for internship updates."
}


def load_faqs():
    if FAQ_FILE.exists():
        try:
            with FAQ_FILE.open("r", encoding="utf-8") as file:
                data = json.load(file)

            if isinstance(data, dict):
                return {
                    str(key).lower(): str(value)
                    for key, value in data.items()
                }

        except (json.JSONDecodeError, OSError):
            print("Warning: Could not read FAQs. Using default FAQs.")

    return DEFAULT_FAQS.copy()


def get_response(message, faqs):
    message = message.lower().strip()

    if message in ("hello", "hi", "hey"):
        return "Hello! Welcome to our chatbot."

    elif message in ("how are you", "how are you?"):
        return "I'm doing great! How can I help you?"

    elif message in ("help", "what can you do"):
        return (
            "You can ask about our hours, services, contact, "
            "or internship. Type 'bye' to exit."
        )

    elif message in ("time", "what time is it"):
        india_time = datetime.now(ZoneInfo("Asia/Kolkata"))
        return f"The current time in India is {india_time.strftime('%I:%M %p')} IST."
    
    elif message in ("date", "what is the date"):
        return f"Today's date is {datetime.now().strftime('%d-%m-%Y')}."

    elif message in faqs:
        return faqs[message]

    else:
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

        if not user_input:
            print("Bot: Please enter a message.")
            continue

        if user_input.lower().strip() in (
            "bye", "byee", "goodbye", "exit", "quit"):
            print("Bot: Goodbye! Have a nice day.")
            break

        response = get_response(user_input, faqs)
        print(f"Bot: {response}")


if __name__ == "__main__":
    main()
