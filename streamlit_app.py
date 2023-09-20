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

@bot.message_handler(commands=['mp3'])
	def mp3(message):
	bot.reply_to(message, "Baik perminta'an anda akan kami proses")
    link = message.text.replace("/mp3 ", "")
    mp3_p = YouTube(link)
    mp3_o = mp3_p.streams.filter(only_audio=True).first()
    mp3_d = mp3_o.download(output_path=".")
    base, ext = os.path.splitext(mp3_d)
    mp3_f = base + '.mp3'
    os.rename(mp3_d, mp3_f)

    for i in os.listdir():
		if i.endswith(".mp3"):
			print(i)
			video = open(i, "rb")
			bot.send_audio(message.chat.id, audio)
			try:
				os.remove(i)
			except:
				print("gagal menghapus!")
    
    
@bot.message_handler(commands=['mp4'])
def send_welcome(message):
	bot.reply_to(message, "Sabar Ya!")
	link = message.text.replace("/mp4 ", "")
	bot.send_message(message.chat.id, "Tunggu sebentar"
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
