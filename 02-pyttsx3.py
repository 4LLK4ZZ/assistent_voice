import pyttsx3

engine = pyttsx3.init()
engine.setProperty("voice", "brazil")

# Utilizando o input para receber o texto a ser falado
#frase = input("Digite a frase que deseja ouvir:\n")
#engine.say(frase)
#engine.runAndWait()

# Utilizando o arquivo de texto para ler o conteúdo
arquivo = open("dados/frase.txt", "r", encoding="utf-8")
conteudo = arquivo.read()
engine.say(conteudo)
engine.runAndWait()