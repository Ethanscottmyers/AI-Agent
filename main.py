import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

verbose = "--verbose" in sys.argv
args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]

if not args:
    print("Usage: python3 main.py <prompt> [--verbose]")
    sys.exit(1)
prompt = " ".join(args)

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

messages = [
    types.Content(role="user", parts=[types.Part(text=prompt)])
]
response = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages)
if verbose:
    print(f"User prompt: {prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

print(response.text)