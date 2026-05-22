import shutil
import rich
from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel
from rich.text import Text
from rich.rule import Rule
from rich.align import Align

console = Console()


def show_header(model_name="gemini-3.5-flash"):
    """Responsive styled header for the AI agent"""

    # terminal width
    terminal_width = shutil.get_terminal_size().columns

    if terminal_width < 100:
        panel_height = 16
        left_padding = (1, 3)
        right_padding = (1, 2)
    else:
        panel_height = 18
        left_padding = (2, 6)
        right_padding = (2, 4)

    left_content = Text(justify="center")

    left_content.append("Built MINI\n", style="bold cyan")
    left_content.append("AI Coding Agent\n", style="white")
    left_content.append("powered by google genai\n", style="dim")
    left_content.append("v1.0.0", style="bright_black")

    # LEFT PANEL
    left = Panel(
        Align.center(left_content, vertical="middle"),
        border_style="bright_black",
        padding=left_padding,
        height=panel_height,
    )

    # RIGHT PANEL CONTENT
    info = Text()

    info.append("build ", style="bold white")
    info.append("<idea>      ", style="dim")
    info.append("Create a new project\n\n", style="white")

    info.append("fix   ", style="bold white")
    info.append("<project>   ", style="dim")
    info.append("Debug broken code\n\n", style="white")

    info.append("add   ", style="bold white")
    info.append("<feature>   ", style="dim")
    info.append("Add to existing project\n\n", style="white")

    info.append("exit  ", style="bold white")
    info.append("            ")
    info.append("Quit the agent\n\n", style="white")

    info.append("─" * 32 + "\n", style="dim")

    info.append("tip: ", style="bright_black")
    info.append("just type naturally", style="white")
    info.append(" — AI understands you", style="dim")

    # creator
    info.append("\n\n")
    info.append("~ by Karan Katyura", style="italic bright_black")

    # RIGHT PANEL
    right = Panel(
        Align.left(info, vertical="middle"),
        title="[dim]commands[/dim]",
        border_style="bright_black",
        padding=right_padding,
        height=panel_height,
    )

    # small screens → stack panels
    if terminal_width < 80:
        console.print(left)
        console.print(right)
    else:
        console.print(
            Columns(
                [left, right],
                equal=True,
                expand=True,
            )
        )


    console.print(
        f"\n[dim]model:[/dim] [white]{model_name}[/white]    "
        "[dim]tools:[/dim] [white]4 loaded[/white]"
    )

    console.print(Rule(style="bright_black"))


# if __name__ == "__main__":
#     show_header()