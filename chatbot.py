from flask import Flask,render_template,request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app =flask(__name__)
english_bot=ChatBot("chatterbot",storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train("chatterbot.corpus.english")
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/get")
def get_bot_response():
    UserText=request.args.get('msg')
    return str(english_bot.get_response(UserText))

if __name__ == '__main__':
    app.run()