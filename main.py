import os
from dotenv import load_dotenv
import argparse
from openai import OpenAI
from prompts import system_prompt
from call_function import available_functions
import json
from call_function import call_function

def main():
    
    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if api_key == None:
        raise RuntimeError("It didn't work")


    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key = api_key,
    )
    parser = argparse.ArgumentParser(description= "Chatbot") # why does this setup a command line argument parser. Where do these methods come from?
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help= "Enable verbose output")
    args = parser.parse_args()                                    #this is where the name of the parsed arguments is provided
    
    if args.verbose:
       print(f"User prompt:{args.user_prompt}")
    
    messages = [{"role": "system", "content": system_prompt},
        {"role":"user",  "content": args.user_prompt}]
    
    response = client.chat.completions.create(
        model="openrouter/free",
        messages = messages ,
        tools= available_functions,
        temperature= 0,
    )      
    message = response.choices[0].message
    if message.tool_calls:
        for tool_call in message.tool_calls:
            result = call_function(tool_call, args.verbose)
            if result["content"] == False:
                raise Exception("no content produced")
            if args.verbose == True:
                print(f"-> {result['content']}")

    else:
        print(message.content)   

   # print(response.usage)

    
   
    if response.usage is None:
        raise RuntimeError("It don't work")
    elif args.verbose == True:
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Response tokens: {response.usage.completion_tokens}")
        print (response.choices[0].message.content)
    else:
        print(response.choices[0].message.content)
    



if __name__ == "__main__":
    main()
