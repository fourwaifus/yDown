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

@bot.message_handler(commands=['start'])
def staRt(message):
    bot.send_message(message.chat.id, "Haloo Anjay!")
    

@bot.message_handler(commands=['mp3'])
def mP3(message):
    bot.send_message(message.chat.id, "Baik perminta'an anda akan kami proses")
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
            audio = open(i, "rb")
            try:
                bot.send_audio(message.chat.id, audio)
                os.remove(i)
            except:
                print("gagal menghapus!")

@bot.message_handler(commands=['mp4'])
def mP4(message):
	bot.send_message(message.chat.id, "Sabar Ya!")
	link = message.text.replace("/mp4 ", "")
	bot.send_message(message.chat.id, "Tunggu sebentar")
	yt = YouTube(link)
	vid = yt.streams.get_highest_resolution()
	vid.download()

	for i in os.listdir():
		if i.endswith(".mp4"):
			print(i)
			video = open(i, "rb")
			try:
			    bot.send_video(message.chat.id, video)
			    os.remove(i)
			except:
				print("gagal menghapus!")

bot.polling()
