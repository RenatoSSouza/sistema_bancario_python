from datetime import datetime
from services.convert_input import convert_input, locate_value_br

def deposit(bank_balance, bank_statement):
    deposit_value = convert_input((input('Digite o valor do depósito: ')))
    if deposit_value <= 0:
        print('Valor inválido')
    else:
        bank_balance += deposit_value
        formatted_value = locate_value_br(deposit_value)
        bank_statement.append(f'Depósito: R$ {formatted_value} data: {datetime.now().strftime("%H:%M:%S %d-%m-%Y")}')
        print(f'Depósito de R$ {formatted_value} efetuado com sucesso!')
    return bank_balance, bank_statement