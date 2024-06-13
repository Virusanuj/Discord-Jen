import google.generativeai as genai
import os
from dotenv import load_dotenv
import json

# Load environment variables from .env file
load_dotenv()

# Configure the Google Generative AI API key
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# Import and initialize the gemini-pro model
model = genai.GenerativeModel('gemini-pro')

# Loading history
with open('tuning.json', 'r') as file:
    tuning = json.load(file)
chat = model.start_chat(history=tuning)

def get_gemini_response(question):
    try:
        # Send the question to the model and get the response
        response = chat.send_message(question, stream=True)
        
        # Ensure the response is fully accumulated
        response.resolve()
        
        # Assuming response contains a text attribute or similar after resolving
        response_text = response.text  # Adjust this based on the actual attribute of GenerateContentResponse
        
        return response_text
    except Exception as e:
        # Handle exceptions (e.g., API errors)
        print(f"An error occurred: {e}")
        return "Sorry, I couldn't process your request."


if __name__ == "__main__":
    question = "What is the capital of France?"
    response = get_gemini_response(question)
    print(response)
