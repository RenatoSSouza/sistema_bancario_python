def deposit(bank_balance, bank_statement):
    deposit_value = float(input('Digite o valor do depósito: '))
    if deposit_value <= 0:
        print('Valor inválido')
    else:
        bank_balance += deposit_value
        bank_statement.append(f'Depósito: R$ {deposit_value}')
        print(f'Depósito de R$ {deposit_value:.2f} efetuado com sucesso!')
    return bank_balance, bank_statement