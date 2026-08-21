import json
import os
from dotenv import load_dotenv
from openai import OpenAI
import argparse
from prompts import system_prompt
from call_function import available_functions

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")

def main():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", help="User input prompt")  # ← add this
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    # Now we can access `args.user_prompt`
    client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
    )
    messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": args.user_prompt},
]
    # print(f"Messages: {messages}")
    # print(f"Verbose: {args.verbose}")
    response = client.chat.completions.create(model = "openrouter/free",messages = messages,tools=available_functions)
    # if args.verbose:
    #     print(f"User prompt: {args.user_prompt}")
    #     print(f"Prompt tokens: {response.usage.prompt_tokens}")
    #     print(f"Response tokens: {response.usage.completion_tokens}")
    if response.choices[0].message.tool_calls != None or len(response.choices[0].message.tool_calls) > 0:
        for tool_call in response.choices[0].message.tool_calls:
            function_args = json.loads(tool_call.function.arguments or "{}")
            print(f"Calling function: {tool_call.function.name}({function_args})")
    print(f"{response.choices[0].message.content}")


if __name__ == "__main__":
    main()
