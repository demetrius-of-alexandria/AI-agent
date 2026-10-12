import os



def get_files_info(working_directory: str, directory: str = ".") -> str:
    absolute_path = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(absolute_path,directory))

    if absolute_path != os.path.commonpath([absolute_path,target_dir]):
        
    
        return(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')

    if os.path.isdir(target_dir) == False:
        return(f'Error: "{directory}" is not a directory')
    
   
    try:
        files_info = []
        for item_name in os.listdir(target_dir) :
            path = os.path.join(target_dir, item_name)
            is_dir = os.path.isdir(path)
            size = os.path.getsize(path)
            files_info.append(f"- {item_name}: file_size={size} bytes, is_dir={is_dir}")
        
        return "\n".join(files_info)
    except Exception as e:
        return f"Error: {e}"


schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}