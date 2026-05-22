"""
Tool Handlers Module

This module contains:
- file_system_tools: Tool declarations for Gemini
- execute_tool_calls: Function to execute tool calls from Gemini responses
"""

from google.genai import types
from src.tools.tools import run_tool


#  TOOL DECLARATIONS  —  the menu Gemini reads to know what it can call

file_system_tools = types.Tool(
    function_declarations=[

        types.FunctionDeclaration(
            name="create_folder",
            description="Creates a new folder/directory on the user's machine.",
            parameters=types.Schema(
                type=types.Type.OBJECT,
                properties={
                    "folder_name": types.Schema(
                        type=types.Type.STRING,
                        description="The folder path to create. E.g. 'todoapp'"
                    )
                },
                required=["folder_name"]
            )
        ),

        types.FunctionDeclaration(
            name="create_file",
            description="Creates a file at the given path and writes content into it. Also used to OVERWRITE a file when fixing bugs.",
            parameters=types.Schema(
                type=types.Type.OBJECT,
                properties={
                    "file_path": types.Schema(
                        type=types.Type.STRING,
                        description="Full relative path. E.g. 'todoapp/index.html'"
                    ),
                    "content": types.Schema(
                        type=types.Type.STRING,
                        description="The complete file content to write."
                    )
                },
                required=["file_path", "content"]
            )
        ),

        # New tool: read file — needed for debugging
        types.FunctionDeclaration(
            name="read_file",
            description="Reads and returns the current content of a file. Use this BEFORE fixing a bug so you can see the existing code.",
            parameters=types.Schema(
                type=types.Type.OBJECT,
                properties={
                    "file_path": types.Schema(
                        type=types.Type.STRING,
                        description="Path of the file to read. E.g. 'todoapp/script.js'"
                    )
                },
                required=["file_path"]
            )
        ),

        # New tool: list files — needed for debugging
        types.FunctionDeclaration(
            name="list_project_files",
            description="Lists all files inside a project folder. Use this when the user mentions a project so you know what files exist.",
            parameters=types.Schema(
                type=types.Type.OBJECT,
                properties={
                    "folder_name": types.Schema(
                        type=types.Type.STRING,
                        description="The root folder to scan. E.g. 'todoapp'"
                    )
                },
                required=["folder_name"]
            )
        ),
    ]
)


#  TOOL EXECUTION ENGINE  —  runs all tool calls from one Gemini response

def execute_tool_calls(parts: list, conversation: list) -> list:
    """
    Loops through all parts of a Gemini response.
    For each function_call part, runs the real Python function
    and collects results to send back to Gemini.

    Returns the list of FunctionResponse parts to append to conversation.
    """
    tool_response_parts = []

    for part in parts:
        if not hasattr(part, 'function_call') or not part.function_call:
            continue  # skip text parts, only handle tool calls

        fn_call = part.function_call
        fn_name = fn_call.name
        fn_args = dict(fn_call.args)

        print(f"\n  [tool] {fn_name}({fn_args})")

        # Run the real function on disk
        result = run_tool(fn_name, fn_args)
        print(f"  [done] {result}")

        # Wrap result for Gemini to read
        tool_response_parts.append(
            types.Part(
                function_response=types.FunctionResponse(
                    name=fn_name,
                    response={"result": result}
                )
            )
        )

    return tool_response_parts
