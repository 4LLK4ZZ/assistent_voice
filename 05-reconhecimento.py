import speech_recognition as sr

recon = sr.Recognizer()

with sr.Microphone() as source:
    print("Diga alguma coisa:\n")
    # Reduz o ruído do ambiente para o microfone te ouvir melhor
    recon.adjust_for_ambient_noise(source, duration=1)
    audio = recon.listen(source)

try:
    texto = recon.recognize_google(audio, language='pt-BR')
    print("Você disse: " + texto)
except sr.UnknownValueError:
    print("Não entendi o que você disse.")
except sr.RequestError as e:
    print(f"Erro ao acessar o serviço do Google; {e}")