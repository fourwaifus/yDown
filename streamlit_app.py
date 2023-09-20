## system requirements on requirements.txt ##
############################################

# initial module
import streamlit as st
from telebot import *
from pytube import YouTube
import os

st.write("debugging is running....")

api_token = "6157246761:AAHwtXyoWZBrMGs8JKfUsvthJakV9q59rdM"
bot = TeleBot(api_token)

@bot.message_handler(commands=['mp4'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")
	link = message.text.replace("/mp4 ", "")
	bot.reply_to(message, link)
	yt = YouTube(link)
	vid = yt.streams.get_highest_resolution()
	vid.download()

	for i in os.listdir():
		if i.endswith(".mp4"):
			print(i)
			video = open(i, "rb")
			bot.send_video(message.chat.id, video)
			try:
				os.remove(i)
			except:
				print("gagal menghapus!")

bot.polling()
