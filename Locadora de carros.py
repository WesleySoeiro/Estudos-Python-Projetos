import time
import os

new_car = []
new_value = []
dev_car = []
dev_value = []
list_cars = {'Fiat Uno 4p flex': ' R$ 50 /dia',
             'Gol 1.0 4p flez': ' R$ 60 /dia',
             'Spin 8l 4p 1.7': ' R$ 100 /dia',
             'Prisma 4p 1.4': ' R$ 90 /dia',
             'Cruze 4p aut 2.0': ' R$ 200 /dia',
             'Montana 2p 1.6': ' R$ 250 /dia',
             'Hilux SW4 8l aut 3.0': ' R$ 800 /dia',
             }
list_cars_alug = {}

while True:
    os.system('cls')
    print('\n===========')
    print('Bem vindo à locadora de carros')
    print('===========\n')
    time.sleep(0.5)
    print('O que deseja fazer?')
    time.sleep(0.5)
    print('0 - Mostrar portifólio | 1 - Alugar um carro | 2 - Devolver um carro')
    op_user = int(input())
    time.sleep(0.5)

    if op_user == 0:
        print('\n===========')
        print('Portifólio - Estes são os modelos em nosso portifólio.')
        print('===========\n')
        i = 1
        for carro, valor in list_cars.items():
            print(f'[{i}]: {carro} - {valor}')
            i += 1
        print('\n===========')
        print('Antes de continuarmos nos diga, deseja continuar a operação?')
        print('\n===========')
        print('0 - Sair | 1 - Continuar')
        op_user_port = int(input())
        time.sleep(0.5)
        if op_user_port == 1:
            print('\n===========')
            print('Alugar - escolha entre nossas opções o carro que se encaixa na sua necessidade.')
            print('===========\n')
            i = 1
            for carro, valor in list_cars.items():
                print(f'[{i}]: {carro} - {valor}')
                i += 1
            print('\n===========')
            print('Antes de continuarmos nos diga, deseja continuar a operação?')
            print('===========')
            print('\n===========')
            print('0 - Sair | 1 - Continuar')
            op_user_alug = int(input())
            time.sleep(0.5)
            if op_user_alug == 1:
                print("Você escolheu a opção Alugar?")
                print("S / N")
                al = input()
                time.sleep(0.5)
                if al == 'N' or al == 'n':
                    pass
                elif al == 'S' or al == 's':
                    print('\n===========')
                    print('Alugar - Digite o número do carro que você deseja.')
                    print('===========\n')
                    i = 1
                    for carro, valor in list_cars.items():
                        print(f'[{i}]: {carro} - {valor}')
                        i += 1
                    print('\n===========')
                    print('Antes de continuarmos nos diga, deseja continuar a operação?')
                    print('===========')
                    print('\n===========')
                    print('Qual será seu carro?')
                    car = int(input()) - 1
                    time.sleep(0.5)
                    carro_esc = list(list_cars.keys())
                    valor_esc = list(list_cars.values())
                    print(
                        f'Você escolheu o {carro_esc[car]}? Ele esta custando {valor_esc[car]}, deseja finalizar a operação?')
                    print("S / N")
                    al_decis = input()
                    time.sleep(0.5)
                    if al_decis == 'N' or al_decis == 'n':
                        pass
                    elif al_decis == 'S' or al_decis == 's':
                        time.sleep(0.5)
                        print('\n===========')
                        print('\nEstamos processando a sua operação, por favor aguarde...')
                        print('\n===========')
                        time.sleep(2)
                        print('\n===========')
                        print('\nEstamos processando a sua operação, por favor aguarde...')
                        print('\n===========')
                        time.sleep(2)
                        print('\n===========')
                        print('\nPronto!')
                        print('\n===========')
                        time.sleep(1)
                        print('\n===========')
                        print(f'\nParabéns, você alugou o {carro_esc[car]}!')
                        print('\n===========')
                        time.sleep(2)
                        print('\n===========')
                        print('\nObrigado por Utilizar nossos serviços!')
                        print('\n===========')
                        time.sleep(2)
                        new_car.append(carro_esc[car])
                        new_value.append(valor_esc[car])
                        list_cars_alug = dict(zip(new_car, new_value))
                        list_cars.pop(carro_esc[car], valor_esc[car])
                        pass
                    else:
                        print('\n===========')
                        print('\nO valor selecionado é inválido, escolha novamente!')
                        print('\n===========')
                        time.sleep(2)
                else:
                    print('\n===========')
                    print('\nO valor selecionado é inválido, escolha novamente!')
                    print('\n===========')
                    time.sleep(2)
            else:
                print('\n===========')
                print('\nO valor selecionado é inválido, escolha novamente!')
                print('\n===========')
                time.sleep(2)
        else:
            print('\n===========')
            print('\nO valor selecionado é inválido, escolha novamente!')
            print('\n===========')
            time.sleep(2)
    elif op_user == 1:
        print('\n===========')
        print('Alugar - escolha entre nossas opções o carro que se encaixa na sua necessidade.')
        print('===========\n')
        i = 1
        for carro, valor in list_cars.items():
            print(f'[{i}]: {carro} - {valor}')
            i += 1
        print('\n===========')
        print('Antes de continuarmos nos diga, deseja continuar a operação?')
        print('===========')
        print('0 - Sair | 1 - Continuar')
        op_user_alug = int(input())
        time.sleep(0.5)
        if op_user_alug == 1:
            print("Você escolheu a opção Alugar?")
            print("S / N")
            al = input()
            time.sleep(0.5)
            if al == 'N' or al == 'n':
                pass
            elif al == 'S' or al == 's':
                print('\n===========')
                print('Alugar - Digite o número do carro que você deseja.')
                print('===========\n')
                i = 1
                for carro, valor in list_cars.items():
                    print(f'[{i}]: {carro} - {valor}')
                    i += 1
                print('\n===========')
                print('Qual será seu carro?')
                car = int(input()) - 1
                time.sleep(0.5)
                carro_esc = list(list_cars.keys())
                valor_esc = list(list_cars.values())
                print(f'Você escolheu o {carro_esc[car]}? Ele esta custando {valor_esc[car]}, deseja finalizar a operação?')
                print("S / N")
                al_decis = input()
                time.sleep(0.5)
                if al_decis == 'N' or al_decis == 'n':
                    pass
                elif al_decis == 'S' or al_decis == 's':
                    time.sleep(0.5)
                    print('\n===========')
                    print('\nEstamos processando a sua operação, por favor aguarde...')
                    print('\n===========')
                    time.sleep(2)
                    print('\n===========')
                    print('\nEstamos processando a sua operação, por favor aguarde...')
                    print('\n===========')
                    time.sleep(2)
                    print('\n===========')
                    print('\nPronto!')
                    print('\n===========')
                    time.sleep(1)
                    print('\n===========')
                    print(f'\nParabéns, você alugou o {carro_esc[car]}!')
                    print('\n===========')
                    time.sleep(2)
                    print('\n===========')
                    print('\nObrigado por Utilizar nossos serviços!')
                    print('\n===========')
                    time.sleep(2)
                    new_car.append(carro_esc[car])
                    new_value.append(valor_esc[car])
                    list_cars_alug = dict(zip(new_car, new_value))
                    list_cars.pop(carro_esc[car], valor_esc[car])
                    pass
                else:
                    print('\n===========')
                    print('\nO valor selecionado é inválido, escolha novamente!')
                    print('\n===========')
                    time.sleep(2)
            else:
                print('\n===========')
                print('\nO valor selecionado é inválido, escolha novamente!')
                print('\n===========')
                time.sleep(2)
        else:
            print('\n===========')
            print('\nO valor selecionado é inválido, escolha novamente!')
            print('\n===========')
            time.sleep(2)

    elif op_user == 2:
        print('\n===========')
        print('Devolver Carros - Qual carro deseja retornar?.')
        print('===========\n')
        d = 1
        for devCar, devVlr in list_cars_alug.items():
            print(f'[{d}]: {devCar} - {devVlr}')
            d += 1
        print('\n===========')
        print('Antes de continuarmos nos diga, deseja continuar?')
        print('===========')
        print('0 - Sair | 1 - Continuar')
        op_user_dev = int(input())
        time.sleep(0.5)
        if op_user_dev == 0:
            pass
        elif op_user_dev == 1:
            print(f'Você gostaria de devolver qual carro? Escolha na lista abaixo: ')
            d = 1
            for devCar, devVlr in list_cars_alug.items():
                print(f'[{d}]: {devCar} - {devVlr}')
                d += 1

            dev = int(input()) - 1
            time.sleep(0.5)
            carro_dev = list(list_cars_alug.keys())
            valor_dev = list(list_cars_alug.values())
            print(f'Você escolheu o {carro_dev[dev]}? Deseja finalizar a operação e devolver este carro?')
            print("S / N")
            dev_decis = input()
            time.sleep(0.5)
            if dev_decis == 'N' or dev_decis == 'n':
                pass
            elif dev_decis == 'S' or dev_decis == 's':
                list_cars[carro_dev[dev]] = valor_dev[dev]
                del list_cars_alug[carro_dev[dev]]
                time.sleep(0.5)
                print('\n===========')
                print('\nEstamos processando a sua operação, por favor aguarde...')
                print('\n===========')
                time.sleep(2)
                print('\n===========')
                print('\nEstamos processando a sua operação, por favor aguarde...')
                print('\n===========')
                time.sleep(2)
                print('\n===========')
                print('\nPronto!')
                print('\n===========')
                time.sleep(1)
                print('\n===========')
                print(f'\nO carro {carro_dev[dev]} foi devolvido com sucesso!')
                print('\n===========')
                time.sleep(2)
                print('\n===========')
                print('\nObrigado por Utilizar nossos serviços!')
                print('\n===========')
                time.sleep(2)
            else:
                print('\n===========')
                print('\nO valor selecionado é inválido, escolha novamente!')
                print('\n===========')
                time.sleep(2)
                pass
        else:
            print('\n===========')
            print('\nO valor selecionado é inválido, escolha novamente!')
            print('\n===========')
            time.sleep(2)
    else:
        print('\n===========')
        print('\nO valor selecionado é inválido, escolha novamente!')
        print('\n===========')
        time.sleep(2)