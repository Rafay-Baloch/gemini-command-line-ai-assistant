import os

from dotenv import load_dotenv
from google import genai


# Load environment variables from the .env file
load_dotenv()

# Read the private Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

# Verify that the API key is available
if not api_key:
    raise ValueError(
        "GEMINI_API_KEY was not found. Please check the .env file."
    )

# Connect the Python application with the Gemini API
client = genai.Client(api_key=api_key)


def generate_ai_response(user_prompt):
    """Send the user's prompt to Gemini and return the AI response."""

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=user_prompt
    )

    return response.text


print("=" * 55)
print("        DAY 7 - COMMAND-LINE AI ASSISTANT")
print("=" * 55)
print("Ask any question or enter an instruction.")
print("Type 'exit' to close the application.")
print("=" * 55)


while True:
    user_input = input("\nYou: ").strip()

    # Close the application when the user enters exit
    if user_input.lower() == "exit":
        print("\nAI Assistant: Goodbye!")
        break

    # Prevent an empty request
    if not user_input:
        print("AI Assistant: Please enter a question or instruction.")
        continue

    try:
        ai_response = generate_ai_response(user_input)

        print("\nAI Assistant:")
        print(ai_response)

    except Exception as error:
        print("\nAn error occurred while making the API request:")
        print(error)