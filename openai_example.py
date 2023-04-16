import openai
import os
from chatmaker import CLIChatMaker, WebChatMaker

# Initialize the API client
openai.api_key = os.environ["OPENAI_API_KEY"]

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


chatbot = CLIChatMaker(chat_gpt)
#chatbot = WebChatMaker(chat_gpt)
chatbot.run()