import os
from dotenv import load_dotenv
import argparse
from openai import OpenAI
from prompts import system_prompt
from call_function import available_functions
import json
from call_function import call_function
import sys
def main():
    
    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if api_key == None:
        raise RuntimeError("It didn't work")


    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key = api_key,
    )
    parser = argparse.ArgumentParser(description= "Chatbot") 
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help= "Enable verbose output")
    args = parser.parse_args()                                    
    
    if args.verbose:
       print(f"User prompt:{args.user_prompt}")
    
    messages = [{"role": "system", "content": system_prompt},
        {"role":"user",  "content": args.user_prompt}]
    
    
    for _ in range(2):
        try:
            response = client.chat.completions.create(
                model="openrouter/free",
                messages = messages ,
                tools= available_functions,
                temperature= 0,
            )      
            message = response.choices[0].message
            messages.append(message)
            if not message.tool_calls:
                print(f"Final Response:{message.content}")
                return
            else:
                
                for tool_call in message.tool_calls:
                    result = call_function(tool_call, args.verbose)
                    messages.append(result)
                    
                    if not result["content"] :
                        raise Exception("no content produced")
                    if args.verbose == True:
                        print(f"-> {result['content']}")
        except Exception as e:
            print(f"Error{e}")
            continue

    print("Max iterations reached")
    sys.exit(1)

    
   



if __name__ == "__main__":
    main()
