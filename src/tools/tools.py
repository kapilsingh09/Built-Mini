
import os


def create_folder(folder_name: str) -> str:
    os.makedirs(folder_name, exist_ok=True)
    
    return f"Folder '{folder_name}' created successfully."


def create_file(file_path: str, content: str) -> str:
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    return f"File '{file_path}' created successfully."


def read_file(file_path: str) -> str:
    """
    Reads an existing file so Gemini can SEE the current code.
    This is critical for debugging — Gemini needs to read the file
    before it can fix it. Otherwise it's fixing blind.
    """
    if not os.path.exists(file_path):
        return f"Error: File '{file_path}' does not exist."
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()


def list_project_files(folder_name: str) -> str:
    """
    Lists all files inside a folder recursively.
    Gemini uses this during debugging to understand what files exist
    so it knows which ones to read and fix.
    """

    if not os.path.exists(folder_name):
        return f"Error: Folder '{folder_name}' does not exist."

    file_list = []
    for root, dirs, files in os.walk(folder_name):
    
        for file in files:

            relative_path = os.path.join(root, file).replace("\\", "/")
            file_list.append(relative_path)

    if not file_list:
        return f"No files found in '{folder_name}'."

    return "Files in project:\n" + "\n".join(file_list)

def run_tool(fn_name: str, fn_args: dict) -> str:
    if fn_name == "create_folder":

        return create_folder(fn_args["folder_name"])
    elif fn_name == "create_file":

        return create_file(fn_args["file_path"], fn_args["content"])
    elif fn_name == "read_file":

        return read_file(fn_args["file_path"])
    elif fn_name == "list_project_files":

        return list_project_files(fn_args["folder_name"])
    else:
        return f"Unknown tool: {fn_name}"

