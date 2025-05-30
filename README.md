Conversational AI Chatbot with Gradio.


A flexible and customizable chatbot built with OpenAI's GPT models and Gradio, designed for business applications with dynamic system prompting capabilities.

![chatbot](https://github.com/user-attachments/assets/b18bce26-65b0-4d42-99de-7fe8bb58dfba)


🚀 Features

Interactive Chat Interface: Clean, web-based chat UI powered by Gradio

Streaming Responses: Real-time response generation for better user experience

Dynamic System Prompting: Contextual system messages that adapt based on user input

Business-Ready: Pre-configured for retail/sales scenarios with customizable prompts

Multi-API Support: Ready for OpenAI, Anthropic, and Google AI APIs

Conversation History: Maintains context throughout the chat session


🛠️ Installation


Clone the repository

bash git clone https://github.com/yourusername/conversational-ai-chatbot.git

cd conversational-ai-chatbot


Install dependencies

pip install openai gradio python-dotenv


Set up environment variables

Create a .env file in the project root and add the following:


OPENAI_API_KEY=your_openai_api_key_here

ANTHROPIC_API_KEY=your_anthropic_api_key_here  # Optional

GOOGLE_API_KEY=your_google_api_key_here        # Optional




Usage

Basic Chatbot

Run the script to launch a basic helpful assistant:

The application will start a local web server (typically at http://127.0.0.1:7860) where you can interact with the chatbot.

Business Applications

The code includes examples for customizing the chatbot for specific business scenarios:

Retail Sales Assistant


Promotes items on sale (hats 60% off, other items 50% off)

Gently encourages customers toward sale items

Handles specific product inquiries with contextual responses


Dynamic Context Handling

The chatbot can modify its behavior based on user input:


Detects keywords in messages

Applies relevant system message modifications

Provides contextual responses (e.g., redirecting belt inquiries to available items)


 Customization

System Messages

Modify the system_message variable to customize your chatbot's personality and knowledge:

pythonsystem_message = "You are a helpful assistant in a [YOUR BUSINESS TYPE]. 

You should [SPECIFIC INSTRUCTIONS FOR YOUR USE CASE]."

Dynamic Responses

Add conditional logic to the chat function for context-aware responses:

pythondef chat(message, history):

    relevant_system_message = system_message
    
    
    # Add your custom conditions
    
    if 'specific_keyword' in message.lower():
    
        relevant_system_message += " Additional context for this scenario."
        
  
🔐 API Keys

This project supports multiple AI providers:


OpenAI: Required for the current implementation

Anthropic: Optional, for Claude models

Google AI: Optional, for Gemini models


Sign up for API keys at:


OpenAI Platform

Anthropic Console

Google AI Studio


🎨 Use Cases

Business Applications


Customer Service: Automated support with business-specific knowledge

Sales Assistant: Product recommendations and sales guidance

Information Desk: Company FAQ and general inquiries


Educational Applications


Tutoring: Subject-specific educational assistance

Language Learning: Conversational practice with native-like responses

Technical Support: Code help and programming guidance


📞 Support

If you encounter any issues or have questions:

contact me: chyootch@gmail.com
