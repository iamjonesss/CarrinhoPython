### IMPORTAÇÕES ###

import datetime
import os

### DATA ###

data_atual = datetime.date.today()

dia = f'{data_atual.day:0>2}'
mes = f'{data_atual.month:0>2}'
ano = f'{data_atual.year:0<4}'

### CÓDIGO ###

list_produtos = ["maçã", 3.50,
                "banana", 5.00,
                "max steel", 20.00,
                "abacate", 15.90,
                "jequiti", 500.12 
]

carrinho = []
preco_total = []

### FUNÇÕES ###

def estoque():
    print('====================[NOSSOS PRODUTOS]====================')
    for posicao in range(0, len(list_produtos)):
        if posicao % 2 == 0:
            print(f'{list_produtos[posicao]:.<30}', end='')
        else:
            print(f'R${list_produtos[posicao]:6.2f}')


### LOOP ###

os.system('cls') # CLS NO CONSOLE
estoque()

while True:

    print('=========================================================')

    produto_carrinho = str(input("Digite o produto desejado: ")).lower()
    
    
    if produto_carrinho in list_produtos:
            
            os.system('cls') # CLS NO CONSOLE

            carrinho.append(produto_carrinho)
            preco = list_produtos.index(produto_carrinho) + 1
            preco_total.append(list_produtos[preco])
            
            print('========================[CARRINHO]=======================')
            print(carrinho)
            print(preco_total)

            estoque()
    
    elif produto_carrinho == "0":
        os.system('cls') # CLS NO CONSOLE
        
        break

    else:
        print("Veja se digitou errado, se não, não há em nosso estoque.")
        
preco_total_carrinho = sum(preco_total)

print(f'Carrinho finalizado, o valor total da compra é: R${preco_total_carrinho}')
print('Quantidade de itens: {}'.format(len(carrinho)))
print('Data da compra: {}/{}/{}'.format(dia, mes, ano))