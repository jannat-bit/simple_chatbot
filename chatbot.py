import nltk
import re

# Sample keyword-based FAQ patterns and responses
FAQ_RESPONSES = {
    r"(hello|hi|hey)": "Hello! How can I help you today?",
    r"(hours|open|close)": "We are open from 9am to 5pm, Monday to Friday.",
    r"(location|address|where)": "We are located at 123 Main Street, Springfield.",
    r"(contact|phone|email)": "You can contact us at support@example.com or call 123-456-7890."
}

def get_response(user_input):
    user_input = user_input.lower()
    for pattern, response in FAQ_RESPONSES.items():
        if re.search(pattern, user_input):
            return response
    return "I'm sorry, I don't understand. Could you please rephrase your question?"
