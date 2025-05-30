#!/usr/bin/env python
# coding: utf-8

# # Day 3 - Conversational AI - aka Chatbot!

# In[ ]:


# imports

import os
from dotenv import load_dotenv
from openai import OpenAI
import gradio as gr


# In[ ]:


# Load environment variables in a file called .env
# Print the key prefixes to help with any debugging

load_dotenv(override=True)
openai_api_key = os.getenv('OPENAI_API_KEY')
anthropic_api_key = os.getenv('ANTHROPIC_API_KEY')
google_api_key = os.getenv('GOOGLE_API_KEY')

if openai_api_key:
    print(f"OpenAI API Key exists and begins {openai_api_key[:8]}")
else:
    print("OpenAI API Key not set")

if anthropic_api_key:
    print(f"Anthropic API Key exists and begins {anthropic_api_key[:7]}")
else:
    print("Anthropic API Key not set")

if google_api_key:
    print(f"Google API Key exists and begins {google_api_key[:8]}")
else:
    print("Google API Key not set")


# In[ ]:


# Initialize

openai = OpenAI()
MODEL = 'gpt-4o-mini'


# In[ ]:


system_message = "You are a helpful assistant"



def chat(message, history):
    messages = [{"role": "system", "content": system_message}] + history + [{"role": "user", "content": message}]

    print("History is:")
    print(history)
    print("And messages is:")
    print(messages)

    stream = openai.chat.completions.create(model=MODEL, messages=messages, stream=True)

    response = ""
    for chunk in stream:
        response += chunk.choices[0].delta.content or ''
        yield response


# ## And then enter Gradio's magic!

# In[ ]:


gr.ChatInterface(fn=chat, type="messages").launch()


# In[ ]:


system_message = "You are a helpful assistant in a clothes store. You should try to gently encourage \
the customer to try items that are on sale. Hats are 60% off, and most other items are 50% off. \
For example, if the customer says 'I'm looking to buy a hat', \
you could reply something like, 'Wonderful - we have lots of hats - including several that are part of our sales event.'\
Encourage the customer to buy hats if they are unsure what to get."


# In[ ]:


def chat(message, history):
    messages = [{"role": "system", "content": system_message}] + history + [{"role": "user", "content": message}]

    stream = openai.chat.completions.create(model=MODEL, messages=messages, stream=True)

    response = ""
    for chunk in stream:
        response += chunk.choices[0].delta.content or ''
        yield response


# In[ ]:


gr.ChatInterface(fn=chat, type="messages").launch()


# In[ ]:


system_message += "\nIf the customer asks for shoes, you should respond that shoes are not on sale today, \
but remind the customer to look at hats!"


# In[ ]:


gr.ChatInterface(fn=chat, type="messages").launch()


# In[ ]:

def chat(message, history):

    relevant_system_message = system_message
    if 'belt' in message:
        relevant_system_message += " The store does not sell belts; if you are asked for belts, be sure to point out other items on sale."

    messages = [{"role": "system", "content": relevant_system_message}] + history + [{"role": "user", "content": message}]

    stream = openai.chat.completions.create(model=MODEL, messages=messages, stream=True)

    response = ""
    for chunk in stream:
        response += chunk.choices[0].delta.content or ''
        yield response


# In[ ]:


gr.ChatInterface(fn=chat, type="messages").launch()


# <table style="margin: 0; text-align: left;">
#     <tr>
#         <td style="width: 150px; height: 150px; vertical-align: middle;">
#             <img src="../business.jpg" width="150" height="150" style="display: block;" />
#         </td>
#         <td>
#             <h2 style="color:#181;">Business Applications</h2>
#             <span style="color:#181;">Conversational Assistants are of course a hugely common use case for Gen AI, and the latest frontier models are remarkably good at nuanced conversation. And Gradio makes it easy to have a user interface. Another crucial skill we covered is how to use prompting to provide context, information and examples.
# <br/><br/>
# Consider how you could apply an AI Assistant to your business, and make yourself a prototype. Use the system prompt to give context on your business, and set the tone for the LLM.</span>
#         </td>
#     </tr>
# </table>

# In[ ]:




