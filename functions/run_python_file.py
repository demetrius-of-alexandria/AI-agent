import os
import subprocess
def run_python_file(
        working_directory: str, file_path: str, args: list[str] | None = None
         ) -> str:
    try:
        absolute_working_directory = os.path.abspath(working_directory)
        abs_file_path = os.path.normpath(os.path.join(absolute_working_directory, file_path))

        if os.path.commonpath([absolute_working_directory, abs_file_path]) != absolute_working_directory:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(abs_file_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if abs_file_path.endswith('.py') == False:
            return f'Error: "{file_path}" is not a Python file'

        
        command = ["python", abs_file_path]
        if args is not None :
            command.extend(args)

        completed_process = subprocess.run(command,cwd = absolute_working_directory, capture_output = True, text = True, timeout = 30)
        output = []
        
        if completed_process.returncode != 0:
            output.append (f'Process exited with code {completed_process.returncode}')
        if not completed_process.stdout and not completed_process.stderr :
            output.append(f'No output produced')
        else:
            if completed_process.stdout:
                output.append(f"STDOUT:\n{completed_process.stdout}")
                        

            if completed_process.stderr:
                output.append(f"STDERR:\n{completed_process.stderr}")
                
        return "\n".join(output)
        
        

    except Exception as e:
        return f"Error: executing Python file: {e}"

        