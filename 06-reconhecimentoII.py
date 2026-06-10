import speech_recognition as sr
from gtts import gTTS
import pygame
import time
import os

def criar_audio(caminho_audio, mensagem):
    # Gera o arquivo de áudio no caminho especificado
    tts = gTTS(mensagem, lang="pt-br")
    tts.save(caminho_audio)
    
    # Inicializa e toca o áudio usando a variável (sem aspas)
    pygame.mixer.init()
    pygame.mixer.music.load(caminho_audio)
    pygame.mixer.music.play()
    
    # IMPORTANTE: Espera o áudio terminar de tocar antes de continuar
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
        
    # Encerra o mixer para liberar o arquivo antes de deletar
    pygame.mixer.quit()
    
    # Agora sim podemos deletar o arquivo gerado (usando a variável)
    os.remove(caminho_audio)

# Testando a introdução
criar_audio("dados/welcome.mp3", "Olá. Vou reconhecer a sua voz")

recon = sr.Recognizer()
with sr.Microphone() as source:
    # Ajusta o ruído para não pegar chiado do microfone
    recon.adjust_for_ambient_noise(source, duration=1)
    print("Diga alguma coisa:")
    audio = recon.listen(source)

try:
    frase = recon.recognize_google(audio, language='pt-BR')
    print(f"Você disse: {frase}")
    criar_audio("dados/mensagem.mp3", frase)
except sr.UnknownValueError:
    print("Não consegui entender o áudio.")
except sr.RequestError:
    print("Erro de conexão com o serviço de reconhecimento.")