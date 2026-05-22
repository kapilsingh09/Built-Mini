# Built-Mini 🚀

A lightweight AI-powered coding assistant that helps you scaffold projects, debug code, and automate file operations. Built with Google's Gemini API, it acts like Claude Code or GitHub Copilot right in your CLI.

## What It Does

[-] **Project Scaffolding** — Automatically create folder structures and boilerplate files
[-] **Code Debugging** — Get intelligent suggestions for fixing bugs
[-] **File Operations** — Create, read, and modify files programmatically
[-] **Interactive CLI** — Chat-style interface with rich formatting and history 💬
[-] **Multi-turn Conversations** — Maintain context across your entire session

## Features ✨

[+] Google Gemini 3.5 Flash integration for fast, intelligent responses
[+] File system tools for automated project creation
[+] Rich terminal UI with panels and formatted output
[+] Conversation history with prompt_toolkit
[+] Chain-of-thought prompting for better reasoning
[+] Lightweight and extensible architecture

## Quick Start

### Prerequisites

- Python 3.8 or higher
- Google Gemini API key 🔑

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/kapilsingh09/Built-Mini.git
   cd Built-Mini
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your API key**
   
   Create a `.env` file in the project root:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```
   
   Get your API key from [Google AI Studio](https://aistudio.google.com/apikey)

### Usage

Run the assistant:
```bash
python main.py
```

Start chatting! Examples:

```
You: Create a Python FastAPI project structure
Assistant: 🚀 Creating your FastAPI project...
[Creates folders and files]

You: What does this function do?
Assistant: [Analyzes and explains]

You: Fix the bug in my main.py
Assistant: [-] Issue found on line 15
[+] Fixed! Here's the corrected version...
```

## Project Structure

```
my_claude_code/
├── main.py                 # Entry point - runs the chat loop
├── requirements.txt        # Python dependencies
└── src/
    ├── agent/              # Agent logic (extensible)
    ├── tools/
    │   ├── __init__.py
    │   └── tools.py        # File system and action tools
    ├── ui/
    │   └── header.py       # CLI display components
    └── utils/
        ├── prompt.py       # System prompts and configurations
        ├── tool_handlers.py # Tool execution logic
        └── __init__.py
```

## API Reference

### Core Functions

**`call_gemini(conversation: list) → str`**
- Sends conversation to Gemini API
- Handles tool calls internally
- Returns final text response

**`file_system_tools`**
- Create folders and files
- Read file contents
- List directory structures

## Configuration

Edit `src/utils/prompt.py` to customize:

[-] System prompts and conversation style
[-] Model parameters (temperature, etc.)
[-] Tool definitions and behaviors

## Contributing 🤝

We'd love your help! Here's how to contribute:

### Getting Started

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-idea`
3. Make your changes
4. Test thoroughly
5. Commit with clear messages: `git commit -m "Add: new feature description"`
6. Push and create a Pull Request

### Contribution Guidelines

[+] Add new tools in `src/tools/tools.py`
[+] Update prompts in `src/utils/prompt.py`
[+] Improve UI components in `src/ui/`
[+] Write clear commit messages
[+] Test with different prompts and edge cases

### Areas to Contribute

- 🎯 New tool implementations (database operations, API calls, etc.)
- 🎨 Enhanced UI and formatting
- 📚 Better documentation and examples
- 🐛 Bug fixes and optimizations
- ⚡ Performance improvements
- 🧪 Test coverage

### Reporting Issues

Found a bug? Have a suggestion? [Open an issue](https://github.com/kapilsingh09/Built-Mini/issues) with:

- Clear description of the issue
- Steps to reproduce
- Expected vs actual behavior
- Python version and OS

## Dependencies

- **google-genai** — Google Gemini API client
- **python-dotenv** — Environment variable management
- **rich** — Beautiful terminal formatting
- **prompt_toolkit** — Advanced command-line input

## License

MIT License — Feel free to use this in your own projects! 📄

## Roadmap 🗺️

[-] Support for Claude API integration
[-] Local model support
[-] Database operations tools
[-] Web scraping utilities
[-] Unit test generation
[-] Code review and linting tools

## Getting Help

- 💬 Check existing [issues](https://github.com/kapilsingh09/Built-Mini/issues)
- 📖 Read the source code — it's well-documented
- ✉️ Reach out with questions

## Made with ❤️

Built by developers, for developers. Happy coding! 🎉
