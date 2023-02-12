from random import randint
import matplotlib.pyplot as plt


def resultado():
    variavel_grafico = 0
    y = [0] # é nescessário iniciar a lista y em 'zero', porque la no if
            # desempeho em gráfico será dado append nos resultados e a variável Y
            # vai garantir que o gráfrico inicie em zero.
    grafico = []
    erro_n1 = []
    erro_n2 = []
    erro_resposta = []
    acertos = 0
    erros = 0
    total = 0
    print('')
    print('-=' * 20)
    print('Você terá 5 tabuadas para tentar acertar, boa sorte')
    while True:
        total += 1
        # este bloco while True vamos pegar o que o usuário digitar
        # caso digite alguma coisa que não seja um numero inteiro,
        # vamos tratar o erro
        n1 = randint(2, 10)
        n2 = randint(2, 10)
        print(f'{n1} x {n2} = ?', end=' ')
        text = str(input(""))
        if text.isalpha():  # verifica se o input/text é strings
            print("!Erro! Você digitou letras.")
            erros += 1
        else:  # caso a string seja 'número'
            numero = int(text)  # transfornar string em número
            resposta = n1 * n2
            if resposta == numero:
                acertos += 1
                variavel_grafico += 1
                grafico.append(variavel_grafico)
            if resposta != numero:
                erros += 1
                erro_n1.append(n1)
                erro_n2.append(n2)
                erro_resposta.append(n1 * n2)
                variavel_grafico -= 1
                grafico.append(variavel_grafico)


        if total == 5:
            break
    print(f'Total de tentativas, {total}')
    print(f'Erros, {erros}')
    print(f'acertos, {acertos}')
    if erros > 0:
        print('')
        print(' - - - - - - D I G I T E - - - - - -')
        print('1 para ver qual tabuada você errou ')
        print('2 para ver seu desempenho em gráfico ')
        print('3 para jogar de novo ')
        print('4  para sair do jogo')
        digite = str(input('>> '))

        # qual tabuada errou
        if digite == '1':
            print('    >>>Correção')
            for c in range(len(erro_n1)):
                print(f'{erro_n1[c]} x {erro_n2[c]} = {erro_resposta[c]}')

        # desempenho em gráfico
        if digite == '2':
            x = [0, 1, 2, 3, 4, 5]
            for item in grafico:
                y.append(item)
            plt.plot(x, y, label='grafico_do_jogo')
            plt.ylabel('Gráfico (acertos/erros)')
            plt.xlabel('TABUADA')
            plt.show()

        # reiniciar o jogo
        if digite == '3':
            resultado()

        if digite == '4':
            print('Fim de jogo')



    else: # este else vai entrar se o jogador acertou todas
        print('1 para ver seu desempenho em gráfico ')
        print('2 para jogar de novo ')
        print('3 - para sair do jogo')
        digite = str(input('>> '))

        if digite == '1':
            x = [0, 1, 2, 3, 4, 5]
            for item in grafico:
                y.append(item)
            plt.plot(x, y, label='grafico_do_jogo')
            plt.ylabel('Gráfico (acertos/erros)')
            plt.xlabel('TABUADA')
            plt.show()

        if digite == '2':
            resultado()

        if digite != 1 and digite != 2:
            print('Fim de jogo')

# inicio do código #
print('----- TABUADA - Vamos jogar? ------')
print('-=' * 20)
escolha = str(input('s/n: '))
if escolha == 's' or escolha == 'S':
    resultado()
else:
    print('Até breve! :)')
