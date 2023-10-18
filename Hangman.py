import random
import string
from words import palavras

def get_valid(palavras): 
    palavra =  random.choice(palavras) #Pega uma palavra aleatoria
    while '-' in palavra or ' ' in palavra: 
        palavra = random.choice(palavras)
    return palavra.upper()

def hagman(): 
    palavra = get_valid(palavras)
    letras_palavra = set(palavra) #Letras de uma palavra
    alfabeto = set(string.ascii_uppercase)
    letras_utilizadas = set() #quais Letras foram Adivinhadas

    lives = len(letras_palavra) * 2

    #Entrada de dados
    while len(letras_palavra) > 0 and int(lives) > 0: 
        # Letras Utilizadas
        print(f'Voce ja utilizou as letras:', ' '.join(letras_utilizadas))

        #Palavra Atual
        word_list = [letter if letter in letras_utilizadas else '-' for letter in palavra]
        print(f'Palavra atual: ', ' '.join(word_list))

        letra_usuario = input(f'Adivinhe uma Letra, cuidado vc so tem {lives} Vidas: ').upper()
        if letra_usuario in alfabeto - letras_utilizadas: 
            letras_utilizadas.add(letra_usuario)
            lives = lives -1
            if letra_usuario in letras_palavra:
                letras_palavra.remove (letra_usuario)
        elif letra_usuario in letras_utilizadas:
            print(f'Voce já utilizadou esta Letra, Tente outra Vez como diria Raul!! voce so tem mais {lives} Vidas')
            lives = lives -1
        else: 
            print('Letra Invalida')
            lives = lives -1
          
    if lives == 0: 
        print(f'Você Morreu! a palavra era {palavra}')
    else:  
        print(f'Parabens vc acertou a palavra é {palavra}')
#user_input = input('Digite uma Letra: ')
hagman()
#print(user_input)