from gtts import gTTS
import pygame
import time

tts = gTTS("Olá Mundo!!!", lang="pt-br")
tts.save("dados/audio.mp3")


# Inicializa o player de áudio
pygame.mixer.init()
pygame.mixer.music.load("dados/audio.mp3")
pygame.mixer.music.play()

# Espera o áudio terminar de tocar antes de fechar o programa
while pygame.mixer.music.get_busy():
    time.sleep(0.1)