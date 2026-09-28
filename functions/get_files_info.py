import os



def get_files_info(working_directory: str, directory: str = ".") -> str:
    absolute_path = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(absolute_path,directory))

    if absolute_path != os.path.commonpath([absolute_path,target_dir]):
        
    
        return(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')

    if os.path.isdir(target_dir) == False:
        return(f'Error: "{directory}" is not a directory')
    if os.path.isdir(target_dir) == True:
        return f'Success: "{directory}" is within the working directory'