# Project 2 Multiple Tool Calling

This project leverages the following technologies:

- **uv** (Python package manager)
- **openaigents** SDK
- **python-dotenv** (for environment variable management)

## Clone the Repository

To get started, clone this project using:

```bash
git clone <repository-url>
cd project_2
```

## Setup

1. **Install dependencies**  
    Ensure you have [uv](https://github.com/astral-sh/uv) installed. Then run:

    ```bash
    uv pip install -r requirements.txt
    ```

2. **Environment Variables**  
    Create a `.env` file in the project root and add your required environment variables.

## Usage

Run your main script as needed:

```bash
uv python main.py
```

## Notes

- The project uses the [openaigents](https://github.com/openai/openaigents) SDK for agentic AI features.
- [python-dotenv](https://github.com/theskumar/python-dotenv) is used to load environment variables from `.env`.

## License

See [LICENSE](./LICENSE) for details.