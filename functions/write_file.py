
import os


def write_file(working_directory: str, file_path: str, content: str) -> str:

    try:
        absolute_path = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(absolute_path, file_path))

        if absolute_path != os.path.commonpath([absolute_path, target_file]):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if os.path.isdir(target_file):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        

    except Exception as e:
        return f"Error as {e}"

    try: 
        parent_directory = os.path.dirname(target_file)
        os.makedirs(parent_directory,exist_ok= True)
        with open(target_file,"w") as file:
            file_content = file.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error as {e}"



schema_write_file = {
    "type": "function",
    "function": {
    "name": "write_file",
    "description": "it takes a file in the working directory and adds to or alters it.",
    "parameters": {
        "type": "object",
        "properties":{
            "file_path":{
                "type": "string",
                "description": "Path to the file to create or overwrite, relative to the working directory",
            },  
            "content":{
                "type": "string",
                "description": "the text that is generated",
            },
        },
    "required":["file_path","content"],
        
    },
    },
}