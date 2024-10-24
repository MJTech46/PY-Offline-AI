# Local AI Chatbot Project

This project implements a local AI chatbot using the **Mistral 7B** model optimized in the **GGUF format**. The chatbot can handle single-session conversations and support contextual dialogues.

## Getting Started

### Prerequisites

To run the model, you'll need the following:
- Python 3.x installed on your system.
- Necessary Python packages (see the [requirements](#requirements.txt) file).
- The **Mistral-7B-Instruct-v0.1.Q3_K_M.gguf** model downloaded to your project folder.

### Model Download

Please download the required model:  
[`mistral-7b-instruct-v0.1.Q3_K_M.gguf`](https://huggingface.co/)  
Place the model in the root of this project before running the code.

### Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/MJTech46/LOCAL-AI.git
    cd LOCAL-AI
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

### Running the Project

There are two main files for running the chatbot:

- **For a single session chat**: Run `main.py`
  
    ```bash
    python main.py
    ```

- **For a chat with context**: Run `main2.py`

    ```bash
    python main2.py
    ```

Both files use the Mistral model for generating responses. The `main.py` file is ideal for quick interactions, while `main2.py` maintains context over a longer conversation.

## Project Structure

- `main.py` - Handles single-session interactions.
- `main2.py` - Supports context-based dialogues.
- `requirements.txt` - Lists the required dependencies.
- `README.md` - This file.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
