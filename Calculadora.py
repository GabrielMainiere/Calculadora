#Calculadora com While 

while True:
    try:
        numero1 = float(input('Digite o primeiro número: '))
        operacao = input('Digite o código da operação, com (| + | - | * | / |): ')
        numero2 = float(input('Digite o segundo número: ')) #Pede as entradas

        if operacao == '+':
            soma = numero1 + numero2
            print('Soma =',soma)

        elif operacao == '-':
            subtracao = numero1 - numero2
            print('Subtração =',subtracao)  #calcula as operações adequadas

        elif operacao == '*':
            multiplicacao = numero1 * numero2
            print('Multiplicação =',multiplicacao)
                
        elif operacao == '/':
            if numero2 != 0: # verifica se o divisor é 0, pois não existe divisão por 0
                divisao = numero1 / numero2
                print('Divisão =',divisao)
            else:
                print('Não existe divisão por 0.')
        else:
            print('Código de operação inválido.')

    except ValueError: #exceção para caso informe algo diferente de um número float
        print('Por favor, insira números válidos!')

    saida = input('Deseja continuar, se sim digite (sim): ').lower()
    if saida == 'sim': #checa se o usuário quer continuar ou não usando a calculadora
        continue       #caso a mensagem seja 'sim', maiúsculo ou minúsculo irá funcionar
    else:
        break
    