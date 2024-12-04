""" pass generator
1) prende input numerico da utente
2) genera una password casuale con lettere, numeri,caretteri speciali
    la lunghezza sarà il l'input numerico dell'utente

usate git nella cartella del progetto
dopo useremo funzionalità per configurare l'origine remote

"""

import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

while True:
    try:
        length = int(input("Inserisci un numero tra 5 e 20 per la lunghezza della password: "))
        if 5 <= length <= 20:
            break
        else:
            print("Per favore, inserisci un numero valido tra 5 e 20.")
    except ValueError:
        print("Per favore, inserisci un numero valido.")

password = generate_password(length)
print(f"La tua password casuale è: {password}")
