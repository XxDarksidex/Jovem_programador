precos = {
    'queijo': 20.89,
    'pão': 17,
    'arroz': 28,
    'feijão': 10,
    'oleo': 8,
    'açucar': 6,
    'farinha': 6.50,
    'macarrão': 5.50,
    'leite': 6,
    'ovo': 12,
    'papel higienico': 20
}

total = 0

while True:
    item = input('Digite um item (digite "sair" para sair): ').lower()
    
    if item == 'sair':
        print(f'Total: R$ {total:.2f}')
        print('saindo...')
        break
    
    if item in precos:
        total += precos[item]
        print(f'R$ {precos[item]:.2f}')
    else:
        print('não encontrado')