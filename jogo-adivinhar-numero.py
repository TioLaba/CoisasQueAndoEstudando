from random import choice

print('Bem-vindo ao jogo do tio\n')

numeros_listas = [x for x in range(10)]
numero_secreto = choice(numeros_listas)

jogadas = 5
while jogadas > 0:
    chute = int(input('Escolha um número para chutar: '))
    
    if chute == numero_secreto:
        print('Parabéns, você acertou!')
        print(f'O número secreto é {numero_secreto}')
        break
    
    jogadas -= 1
    
    if chute < numero_secreto:
        print('O seu chute foi menor que o número secreto')
    elif chute > numero_secreto:
        print('O seu chute foi maior que o número secreto')

    print(f'Você tem {jogadas} jogadas restantes.')

if jogadas == 0:
    print('Você perdeu!!!')
    print(f'O número secreto era {numero_secreto}')

print('Fim')
