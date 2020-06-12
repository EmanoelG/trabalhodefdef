def valoresima(num):  # essa é a questão 1    #### 
    """ \033[07;34mEssa funcao faz com que : para um N informado pelo usuario. use a funcao q receba um valor N 
    inteiro e imprima ate a n-esima linha;
    Ex:
    1
    22
    333
    ...
    nnnn...\033[m"""
    for i in range(1, num):
        print(str( i ) * i )

        

def somanumeros(): # quest03
    """\033[07;36mEssa funcao soma 3 valores e retorna a soma delas\033"""
    n1 = int(input('\033[04;35mInforme o 1° valor inteiro: \033[m'))
    n2 = int(input('\033[04;34;42mInforme o 2° valor inteiro: \033[m'))
    n3 = int(input('\033[04;33;45mInforme o 3° valor inteiro: \033[m'))
    s = ((n1 + n2) + n3)  
    print(f'\033[36mA soma de {n1} + {n2} + {n3} é igual á: {s}\033[m')



def umdois(num):  #quest02
    """\033[32mEssa funcao faz com que : para um N informado pelo usuario. use a funcao q receba um valor N \ninteiro e imprima ate a n-esima linha ex : \n1 \n12 \n123 \n...\033[m
    """
    for c in range(1, num+1):
        print(end=' ')
        numn= list()
        for i in range(1,c+1):
            numn.append(i) 
            print(i,end=' ')
        print("\n",end=' ')




def poss(n): #quest04
    """\033[36mEssa funcao mostra se o valor e negativo mostrando N ou se positivo mostrando P\033[m"""
    print(f'{n} é um valor: ',end='')
    if n <= 0:
        print('N',end='')
    elif n > 0:
        print('P',end='') 
print()

def somaimposto(imp): ## questao05
    """ 
    \033[36mEssa funcao adiciona o imposto ao produto\033[m
    """
    x = (      imp +(     (imp / 100 )   * 35 )) ### na questao nao dava quantos porcento , coloquei 35% ....
    print(f'Esse e o valor doa produto com ao imposto dentro {x:.2f}R$')

def oqfaz():
    while True:
        print('\033[02;31mAntes de tudo sou a função que mostra o que cada função faz\033m')
        des= str(input('\033[02;35mDeseja saber oq cada funcao faz S/N: \033[m')).lower()
        if des == 's':
            margens()
            x= str(input('\033[36m\tdigite a letra da funcao que deseja saber ! \t\t\t\nV. valoresima \t\nS. somanumeros \t\nU. umdois \t\nP. poss \t\nSI. somaimposto \n\033[m')).upper()
            margens()
            if x == 'V':
                print(help(valoresima))
            elif x == 'S':
                print(help(somanumeros))
            elif x == 'U':
                print(help(umdois))
            elif x == 'P':
                print(help(poss))
            elif x == 'SI':
                print(help(somaimposto))
            
        else:
            print('\033[36;45mOk ja entendi...\033[m')
            break

    
def margens():
    print('\033[32m-=-=\033[m'*15)


