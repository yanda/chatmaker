from flask import Flask, request, jsonify, render_template
from rich.console import Console
from rich.markdown import Markdown

class BaseChatMaker():
    def __init__(self, chat_function):
        self.chat_function = chat_function
        self.conversation_history = []

    def run(self):
        raise NotImplementedError

class CLIChatMaker(BaseChatMaker):
    def __init__(self, chat_function):
        self.chat_function = chat_function
        self.conversation_history = []
        self.console = Console()

    def run(self):
        self.console.print("Welcome to the ChatGPT Command Line Simulator!")
        self.console.print("Type 'exit' to quit the program.")

        while True:
            user_input = self.console.input("\n[green]▶ ")
            if user_input.lower() == "exit":
                self.console.print("Goodbye!")
                break

            self.conversation_history.append({"role": "user", "content": user_input})
            with self.console.status("[bold green]ChatGPT is thinking...") as status:
                assistant_response = self.chat_function(self.conversation_history)
                self.conversation_history.append({"role": "assistant", "content": assistant_response})
                md = Markdown(assistant_response)
                self.console.print(md)

class WebChatMaker(BaseChatMaker):
    def __init__(self, chat_function):
        self.chat_function = chat_function
        self.conversation_history = []
        self.app = Flask(__name__)

    def interact(self):
        user_input = request.json.get("user_input")
        if user_input:
            self.conversation_history.append({"role": "user", "content": user_input})
            assistant_response = self.chat_function(self.conversation_history)
            self.conversation_history.append({"role": "assistant", "content": assistant_response})
            return jsonify({"response": assistant_response})
        else:
            return jsonify({"error": "User input is missing."}), 400
        
    def index(self):
        return render_template("index.html")
    
    def run(self):
        self.app.add_url_rule('/', view_func=self.index, methods=['GET'])
        self.app.add_url_rule('/chat', view_func=self.interact, methods=['POST'])

        self.app.run(debug=True)