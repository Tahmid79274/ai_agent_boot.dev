import os
from dotenv import load_dotenv
from openai import OpenAI
import argparse
from google.genai import types

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")

def main():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", help="User input prompt")  # ← add this
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    # Now we can access `args.user_prompt`
<<<<<<< HEAD
    client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
    )
    # prompt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    response = client.chat.completions.create(model = "openrouter/free",messages = args.user_prompt)
    if response.usage is not None:
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Response tokens: {response.usage.completion_tokens}")
    print(f"User prompt: Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.")
    print(f"Prompt tokens: {response.usage.prompt_tokens}")
    print(f"Response tokens: {response.usage.completion_tokens}")
    print(f"Response: {response.choices[0].message.content}")
=======
    client = genai.Client(api_key=api_key)
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    response = client.models.generate_content(model="gemini-2.5-flash",contents=messages)
    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print(f"Response: {response.text}")
    

    
    
>>>>>>> 314364f5a927f7b3e748266cd62e6b739dda769c


if __name__ == "__main__":
    main()
