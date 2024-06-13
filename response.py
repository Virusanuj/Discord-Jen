from random import choice, randint
from gemini import get_gemini_response

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()
    return get_gemini_response(lowered)
