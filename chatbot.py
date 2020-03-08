rom ChatterBot.trainers import ListTrainer
from ChatterBot import ChatBot

bot=ChatBot('Test')
conv=open('chats.txt','r').readlines()

bot.set_trainer(ListTrainer)
bot.train(conv)

while True:
    request=input('you :')
    response=bot.get_response(request)
    print('Bot :' , response)
