from gtts import gTTS
import pygame
import time
import os

def cria_audio(mensagem):
    tts = gTTS(mensagem, lang="pt-br")
    tts.save("dados/mensagem.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("dados/mensagem.mp3")
    pygame.mixer.music.play()
    os.remove("dados/mensagem.mp3")

    # Espera o áudio terminar de tocar antes de fechar o programa
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
    
# 1- Utilizando a função diretamente
cria_audio("Aprendendo a criar um assistente virtual")

# 2- Utilizando com o input
frase = input("Digite a frase a ser falada:\n")
cria_audio(frase)

# 3- Utilizando com arquivo
arquivo = open("dados/frase.txt", "r", encoding="utf-8")
conteudo = arquivo.read()
cria_audio(conteudo)