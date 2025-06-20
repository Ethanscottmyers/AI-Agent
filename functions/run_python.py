import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    abs_working_dir = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path))
    if not target_file.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_file):
        return f'Error: File "{file_path}" not found'
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file'
    try:
        commands = ["python3", target_file]
        if args:
            commands.extend(args)
        result = subprocess.run(commands, cwd=abs_working_dir, capture_output=True, timeout=30, text=True)
        output = []
        if result.stdout:
            output.append(f"STDOUT:\n{result.stdout}")
        if result.stderr:
            output.append(f"STDERR:\n{result.stderr}")

        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")

        return "\n".join(output) if output else "No output produced."

    except Exception as e:
        return f'Error in executing Python file "{file_path}": {e}'