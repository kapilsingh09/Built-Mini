from google import genai
from google.genai import types
import os
from dotenv import load_dotenv
from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel
from rich.text import Text
from rich.rule import Rule
from prompt_toolkit import prompt
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.styles import Style

load_dotenv()

GEMINI_MODEL_NAME = "gemini-3.5-flash"

gemini_key = os.getenv("GEMINI_API_KEY")
if not gemini_key:
    console = Console()
    console.print("[bold red]API key not loaded[/bold red]")
    exit()

client = genai.Client(api_key=gemini_key)
console = Console()

from src.utils.tool_handlers import file_system_tools, execute_tool_calls
from src.utils.prompt import COT_SYSTEM_PROMPT


def call_gemini(conversation: list) -> str:
    """
    Sends the conversation to Gemini and handles the full tool loop internally.
    Gemini may call tools multiple times before giving a final text answer.
    This function keeps looping until Gemini stops calling tools.
    Returns Gemini's final plain text response.
    """
    while True:
        response = client.models.generate_content(
            model=GEMINI_MODEL_NAME,
            contents=conversation,
            config=types.GenerateContentConfig(
                system_instruction=COT_SYSTEM_PROMPT,
                tools=[file_system_tools],
                temperature=0.2, #good for deterministic output, adjust as needed maybe!
            )
        )

        parts = response.candidates[0].content.parts if response.candidates and response.candidates[0].content else []
        has_tool_call = any(
            hasattr(p, 'function_call') and p.function_call
            for p in parts
        )

        if has_tool_call:
            # Add Gemini's tool-request message to history
            conversation.append(types.Content(role="model", parts=parts))

            # Run all requested tools and collect results
            tool_response_parts = execute_tool_calls(parts, conversation)

            # Send all results back to Gemini in one message
            conversation.append(types.Content(role="user", parts=tool_response_parts))

            # Loop again — Gemini may need more tools or will now give final answer

        else:
            # No tool calls — this is Gemini's final text answer
            final_text = "".join(
                p.text for p in parts
                if hasattr(p, 'text') and p.text
            )
            # Add Gemini's final answer to history so next turn has full context
            conversation.append(types.Content(role="model", parts=parts))
            return final_text



from src.ui.header import show_header

#  MAIN FUNCTIONS  —  Gemini tool definitions and execution loop
def main():
    show_header(GEMINI_MODEL_NAME)

    history = InMemoryHistory()
    input_style = Style.from_dict({"prompt": "#d4a017 bold"})
    
    conversation = []

    while True:
        try:
            console.print('[#4a9eff][[/][black] AGENT [#4a9eff]][/] ', end="")
            user_input = prompt("[>] ", history=history, style=input_style).strip()
        except (KeyboardInterrupt, EOFError):
            console.print("\n[dim]shutting down. bye![/dim]")
            break

        if not user_input:
            continue

        if user_input.lower() in ("exit", "quit", "bye"):
            console.print("\n[dim]shutting down. bye![/dim]")
            break

        #conversation history of user
        console.print(f"[#4a9eff][[/][black] YOU [#4a9eff]][/] [white]{user_input}[/white]")
        conversation.append(
            types.Content(role="user", parts=[types.Part(text=user_input)])
        )

        console.print(
        "\n[#FFD700]●[/#FFD700] "
        "[bold]Thinking[/bold][dim] ...[/dim]\n"
        )

        # Call Gemini and get the final answer after all tool calls are done
        final_answer = call_gemini(conversation)
        
        # Display final answer in styled panel
        response_panel = Panel(
            final_answer,
            title="[bold #4a9eff]GEMINI RESPONSE[/bold #4a9eff]",
            border_style="bright_black",
            padding=(1, 2)
        )
        console.print(response_panel)
        console.print()


if __name__ == "__main__":
    main()