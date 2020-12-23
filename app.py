from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.response_selection import get_random_response
import chatterbot

app = Flask(__name__)
my_bot = ChatBot(name='Ruchir Chatbot',read_only = True,
                 response_selection_method=get_random_response,
                 logic_adapters=[
        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',
            'input_text': ' ',
            'output_text': 'Cannot understand'
        },
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'i honestly have no idea how to respond to that',
            'maximum_similarity_threshold': 0.7
        },
        {
            'import_path': 'chatterbot.logic.MathematicalEvaluation'
        },




    ]
    )

trainer = ChatterBotCorpusTrainer(my_bot)
trainer.train(
   "./conversation.yml"
)
trainer.train("chatterbot.corpus.english.greetings")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/hello")
def get_bot_response():
    userText = request.args.get('msg')
    print("hello")
    return str( my_bot.get_response(userText))



if __name__ == "__main__":
    app.run(debug=True)
