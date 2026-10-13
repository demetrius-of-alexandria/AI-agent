
import os

def get_file_content(working_directory:str, file_path: str) -> str:
    
    try:
        absolute_path = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(absolute_path, file_path))

        if os.path.commonpath([absolute_path , target_file]) != absolute_path:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'

    except Exception as e:
        return f"Error as {e}"

    try:
   
        MAX_CHARS = 10000
      
        with open(target_file, "r") as file:
            file_content_string = file.read(MAX_CHARS)
        
        
       
        
            if file.read(1):
                file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        return file_content_string

    except Exception as e:
        return f"Error : {e}"


schema_get_file_content = {
    "type": "function",
    "function" : {
        "name" : "get_file_content",
        "description" : "Reads and returns the content of a specified file within the working directory, truncating if the file exceeds the maximum character limit.",
        "parameters": {
            "type":"object",
            "properties" : {
                "file_path" : {
                    "type" : "string",
                    "description": "file that gets read"
                },
            },
        },
    },
}

