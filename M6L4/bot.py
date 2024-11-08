import telebot
from config import TOKEN
import random


bot = telebot.TeleBot(TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")
    
@bot.message_handler(commands=['math'])
def calcuations(message):
    key = telebot.util.extract_arguments(message.text)
    bot.send_message(message.chat.id, eval(str(key)))

@bot.message_handler(commands=["randomfact"])
def randomfact(message):
    facts = [
        
        'В гта 5 После перезапуска проваленной миссии вас ждёт отличный от первоначального вступительный диалог, зависящий от обстоятельств провала.',
        'В гта 5 Если вы вызываете такси в аэропорту и рядом с вами есть ещё один человек, который ждёт машину, он станет недоволен, накричит и попытается ввязаться в драку.',
        'В гта 5 Если после разговора по телефону с каким-либо персонажем вы перезвоните ему вновь, он пожалуется, что у него нет времени и отметит, что вы только что разговаривали.',
        'В гта 5 Ламар комментирует прическу Франклина в конце одной из ранних миссий. При следующей встрече его реакция меняется в зависимости от того, поменяли вы причёску или нет.',
        'В гта 5 Вспышка из выхлопной трубы может поджечь бензиновую лужицу или дорожку.'
             
             ]
    bot.send_message(message.chat.id, str(random.choice(facts)))

@bot.message_handler(commands=["coin"])
def randomfact(message):
    money = random.choice(['Орел', 'Решка'])
    bot.send_message(message.chat.id, str(money))
# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()