# Gemini Command-Line AI Assistant

A simple command-line AI assistant developed using Python and the Google Gemini API. The application accepts questions or instructions from the user, sends them to a Large Language Model through an API, and displays the generated response in the terminal.

This project was developed as part of Day 7 of the Big Brains Generative AI Internship.

## Project Objective

The purpose of this project is to understand how developers integrate Large Language Models into software applications using APIs. It demonstrates API authentication, prompt submission, response handling, error handling, and API-key security.

## Technologies Used

- Python
- Google Gemini API
- Google GenAI Python SDK
- python-dotenv
- Visual Studio Code
- Git and GitHub

## Features

- Accepts questions and instructions through the terminal
- Sends user input to the Gemini API
- Displays AI-generated responses
- Supports multiple requests during one session
- Handles empty input and API errors
- Closes safely when the user enters `exit`
- Protects the API key using a private `.env` file

## Project Structure

```text
Day_7_LLM_API_Assistant/
│
├── screenshots/
│   ├── 1-first-api-request.jpg
│   ├── 2-second-api-request.jpg
│   ├── 3-application-exit.jpg
│   ├── 4-source-code-part-1.jpg
│   └── 5-source-code-part-2.jpg
│
├── app.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Installation and Local Execution

### 1. Clone the repository

```bash
git clone https://github.com/Rafay-Baloch/gemini-command-line-ai-assistant.git
```

### 2. Open the project directory

```bash
cd gemini-command-line-ai-assistant
```

### 3. Install the required libraries

```bash
python -m pip install -r requirements.txt
```

### 4. Create the environment file

Create a file named `.env` in the main project directory and add your private Gemini API key:

```env
GEMINI_API_KEY=your_api_key_here
```

### 5. Run the application

```bash
python app.py
```

Enter a question or instruction in the terminal. Type `exit` to close the application.

## Request and Response Flow

1. The user enters a question or instruction in the terminal.
2. The Python application receives the user input.
3. The application sends an authenticated request to the Gemini API.
4. The Gemini model processes the prompt and generates a response.
5. The API returns the generated response to the Python application.
6. The application displays the response in the terminal.

## API Security

The Gemini API key is stored inside a private `.env` file. The `.env` file is included in `.gitignore`, which prevents the private API key from being uploaded to GitHub.

The `.env.example` file contains only a placeholder and helps other users understand how to configure their own API key.

## Testing

The application was tested using multiple prompts.

### Test 1 — Generative AI Explanation

The user asked the assistant to explain Generative AI in three simple bullet points. The Gemini API successfully returned a clear and structured explanation.

### Test 2 — Product Description

The prompt was changed to request a professional product description for a wireless keyboard. The API successfully returned a relevant product description.

### Test 3 — Exit Command

The `exit` command was tested successfully, and the application closed safely.

## Screenshots

The `screenshots` directory contains proof of:

- Successful first API request
- Successful changed prompt and response
- Application exit functionality
- Python source code
- Working command-line application

## Learning Outcomes

Through this project, I learned:

- What an API is and how applications use APIs
- How an LLM API processes requests and returns responses
- How to connect Python with the Google Gemini API
- How to receive input through a command-line interface
- How to protect an API key using environment variables
- How to handle API errors
- How to document and publish a small AI project on GitHub

## Conclusion

This project demonstrated the difference between manually using an AI chatbot and integrating an LLM into a software application. It provided practical experience with API authentication, sending prompts, receiving generated responses, protecting private credentials, and creating a basic command-line AI assistant.

## Author

**Abdur Rafay Hassan Baloch**

- GitHub: [Rafay-Baloch](https://github.com/Rafay-Baloch)
- LinkedIn: [Abdur Rafay Hassan Baloch](https://www.linkedin.com/in/abdur-rafay-hassan-baloch-0860b9225/)
- Project Repository: [Gemini Command-Line AI Assistant](https://github.com/Rafay-Baloch/gemini-command-line-ai-assistant)

## Disclaimer

This project was developed for educational and internship purposes. Users must create and protect their own Gemini API key.