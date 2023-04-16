import openai
import os
from chatmaker import chatbot

# Initialize the API client
openai.api_key = os.environ["OPENAI_API_KEY"]


@chatbot("web")
def chat_gpt(conversation_history):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation_history,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    message = response.choices[0].message["content"].strip()
    return message