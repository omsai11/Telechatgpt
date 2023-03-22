!pip install pyTelegramBotAPI 
!pip install openai 
 
open_AI_APi="" 
bot_api="" 
 
import telebot 
import os 
import openai 
openai.organization = "" 
openai.api_key = open_AI_APi 
# openai.Model.list() 
bot = telebot.TeleBot(bot_api, parse_mode=None) 
 
def response(prompt): 
  response = openai.Completion.create( 
  model="text-davinci-003", 
  prompt=prompt, 
  temperature=0.9, 
  max_tokens=150, 
  top_p=1, 
  frequency_penalty=0.0, 
  presence_penalty=0.6, 
  stop=[" Human:", " AI:"]) 
  return response['choices'][0]['text'] 
 
 
# response("how are you") 
 
def response1(prompt): 
  response = openai.ChatCompletion.create( 
      model="gpt-3.5-turbo", 
  messages=[ 
        {"role": "assistant", "content": ('you are a assistant you can add information about your firm bot here are question' + '{' + prompt+'}')}, 
    ] 
  ) 
  return response['choices'][0]['message']['content'] 
 
 
# response("how are you") 
 
@bot.message_handler(commands=['start', 'help']) 
def send_welcome(message): 
 bot.reply_to(message, "how are you doing?") 
  
@bot.message_handler(func=lambda message: True) 
def echo_all(message): 
 bot.reply_to(message, response1(message.text)) 
 
bot.infinity_polling()
