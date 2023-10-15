import random

def guess(x):
    rad_num = random.randint(1, x)
    guess = 0
    while guess != rad_num:
        guess = int(input(f'Adivie um numero entre 1 e {x}: '))
        if guess < rad_num: 
            print('tente outra vez, o numero é maior')
        elif guess >  rad_num: 
            print('Tente outra vez, o nimero é menor') 
        
    print(f'Parabens, vc acertou!! o numero é {rad_num}')    

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'C': 
        guess = random.randint(low, high)
        feedback = input(f'O  numero {guess} é Maior (H), Menor (L) ou esta correto (C)')
        if feedback == 'H':
            high = guess - 1
        if feedback == 'L':
            low = guess + 1                    

    print(f'A Maquina encontrou o numero, {guess} é o numero correto!!! \0/ ')

#guess(10)
computer_guess(int(input('Qual o numero secreto: ')))