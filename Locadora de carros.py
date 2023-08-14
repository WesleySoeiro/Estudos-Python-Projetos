import time
import os

new_car = []
new_value = []
dev_car = []
dev_value = []
list_cars = {'Fiat Uno 4p flex': '50',
             'Gol 1.0 4p flez': '60',
             'Spin 8l 4p 1.7': '100',
             'Prisma 4p 1.4': '90',
             'Cruze 4p aut 2.0': '200',
             'Montana 2p 1.6': '250',
             'Hilux SW4 8l aut 3.0': '800',
             }
list_cars_alug = {}

def finalizando_dev():
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
    
    
    
    
def finalizando():
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


def erro():
    print('\n===========')
    print('\n O valor selecionado é inválido, escolha novamente!')
    print('\n===========')
    time.sleep(2)
    pass
        
        
def mostrar_car():
    i = 1
    for carros, valor in list_cars.items():
        print(f'[{i}] - {carros} - R${valor} /dia.')
        i += 1
        
def dev_car():
    d = 1
    for devCar, devVlr in list_cars_alug.items():
        print(f'[{d}]: {devCar} - R${devVlr} /dia.')
        d += 1
        
        
def aluguel():
    print('\n===========')
    print('Alugar - escolha entre nossas opções o carro que se encaixa na sua necessidade.')
    print('===========\n')
    i = 1
    mostrar_car()
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
            mostrar_car()
            print('\n===========')
            print('Qual será seu carro?')

        else:
            erro()
    else:
        erro()

while True:
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
        mostrar_car()
        print('\n===========')
        print('Antes de continuarmos nos diga, deseja continuar a operação?')
        print('\n===========')
        print('0 - Sair | 1 - Continuar')
        op_user_port = int(input())
        time.sleep(0.5)
        if op_user_port == 1:
            aluguel()
            car = int(input()) - 1
            time.sleep(0.5)
            carro_esc = list(list_cars.keys())
            valor_esc = list(list_cars.values())
            print('\n===========\n')
            print(f'Você escolheu o {carro_esc[car]}? Ele esta custando {valor_esc[car]}')
            print('\n===========')
            print('\n===========\n')
            print(f'Por quantos dias você alugara este carro?')
            print('\n===========\n')
            dias = int(input())
            print('\n===========')
            print('\nO valor total da sua operação será de {} R$, deseja continuar a operação?'.format(int(dias) * int(valor_esc[car])))                
            print('\n===========')
            print("S / N")
            al_decis = input()
            time.sleep(0.5)
            if al_decis == 'N' or al_decis == 'n':
                pass
            elif al_decis == 'S' or al_decis == 's':
                finalizando()
                new_car.append(carro_esc[car])
                new_value.append(valor_esc[car])
                list_cars_alug = dict(zip(new_car, new_value))
                list_cars.pop(carro_esc[car], valor_esc[car])
                pass
            else:
                erro()
        elif op_user_port == 0:
            pass
        else:
            erro()
    elif op_user == 1:
        aluguel()
        car = int(input()) - 1
        time.sleep(0.5)
        carro_esc = list(list_cars.keys())
        valor_esc = list(list_cars.values())
        print('\n===========\n')
        print(f'Você escolheu o {carro_esc[car]}? Ele esta custando {valor_esc[car]}')
        print('\n===========')
        print('\n===========\n')
        print(f'Por quantos dias você alugara este carro?')
        print('\n===========\n')
        dias = int(input())
        print('\n===========')
        print('\nO valor total da sua operação será de {} R$, deseja continuar a operação?'.format(int(dias) * int(valor_esc[car])))                
        print('\n===========')
        print("S / N")
        al_decis = input()
        time.sleep(0.5)
        if al_decis == 'N' or al_decis == 'n':
            pass
        elif al_decis == 'S' or al_decis == 's':
            finalizando()
            new_car.append(carro_esc[car])
            new_value.append(valor_esc[car])
            list_cars_alug = dict(zip(new_car, new_value))
            list_cars.pop(carro_esc[car], valor_esc[car])
            pass
        else:
            erro()
    elif op_user == 2:
        print('\n===========')
        print('Devolver Carros - Qual carro deseja retornar?.')
        print('===========\n')
        dev_car()
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
            dev_car()
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
                finalizando_dev()
                time.sleep(2)
            else:
                erro()
                
        else:
            erro()
    else:
        erro()