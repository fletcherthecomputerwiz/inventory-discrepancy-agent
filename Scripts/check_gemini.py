"""Check that the Gemini API key in .env works by making one small request."""
import os 
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import errors
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
model = os.getenv("GEMINI_MODEL")
if not api_key:
    sys.exit("GEMINI_API_KEY not found in environment variables")
if not model:
    sys.exit("GEMINI_MODEL not found in environment variables")

client = genai.Client(api_key=api_key)

try:
    if "--list" in sys.argv:
        for m in client.models.list():
            if "generateContent" in (m.supported_actions or []):
                print(m.name)
        sys.exit()
    response = client.models.generate_content(
        model=model,
        contents="Reply with the single word OK"
    )
    print(f"Model: {model}")
    print(f"Reply: {response.text}")

except errors.APIError as e:
    sys.exit(f"API call failed: {e.message}")

