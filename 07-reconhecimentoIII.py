from random import randint
import speech_recognition as sr
from gtts import gTTS
import pygame
import time
import os

def criar_audio(caminho_audio, mensagem):
    tts = gTTS(mensagem, lang="pt-br")
    tts.save(caminho_audio)
    
    pygame.mixer.init()
    pygame.mixer.music.load(caminho_audio)
    pygame.mixer.music.play()
    
    # IMPORTANTE: Espera o áudio terminar antes de prosseguir
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
        
    pygame.mixer.quit()
    os.remove(caminho_audio)

# Passo 1: O robô fala
criar_audio("dados/welcome.mp3", "Escolha um número de um a dez")

# Passo 2: O microfone escuta
recon = sr.Recognizer()
with sr.Microphone() as source:
    print("Ajustando ruído ambiente... Aguarde 1 segundo.")
    recon.adjust_for_ambient_noise(source, duration=1)
    print("Diga alguma coisa (Fale o número agora):")
    audio = recon.listen(source)

# Dicionário de conversão
word_to_digit = {
    "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
    "um": 1, "dois": 2, "três": 3, "quatro": 4, "cinco": 5, "seis": 6, "sete": 7, "oito": 8, "nove": 9, "dez": 10
}

# Tratamento para evitar o crash (UnknownValueError)
try:
    # Passo 3: Reconhece a fala
    numero_texto = recon.recognize_google(audio, language='pt-BR').lower()
    print(f"Você disse: {numero_texto}")
    
    # Tenta converter a palavra falada para número inteiro
    # Se o Google entender "5" ou "cinco", ambos funcionam
    numero_usuario = word_to_digit.get(numero_texto, None)

    if numero_usuario is not None:
        resultado = randint(1, 10)
        print(f"Número sorteado: {resultado}")

        if numero_usuario == resultado:
            criar_audio("dados/venceu.mp3", "Parabéns! Você acertou o número.")
        else:
            criar_audio("dados/perdeu.mp3", f"Infelizmente você errou. Eu mentalizei o número {resultado}.")
    else:
        criar_audio("dados/erro.mp3", "Eu ouvi o que você disse, mas não parece ser um número de um a dez.")

except sr.UnknownValueError:
    print("Erro: Não foi possível entender o áudio. O microfone captou apenas silêncio ou ruído.")
    criar_audio("dados/silencio.mp3", "Desculpe, não consegui ouvir você.")
except sr.RequestError:
    print("Erro: Falha na conexão com o serviço do Google.")