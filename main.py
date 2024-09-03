from deposit import deposit
from withdrawal import withdrawal
from bank_statement import print_statement

menu = """
    [d] - Depositar
    [s] - Sacar
    [e] - Extrato
    [q] - Sair\n
    """
    
bank_balance = 0
bank_statement = []
daily_withdrawals = 0

while True:
    
    option = input(menu)
    option = option.lower()
    try:
        if option == 'd':
            print('Deposito\n')
            bank_balance, bank_statement = deposit(bank_balance, bank_statement)
        elif option == 's':
            print('Saque\n')
            bank_balance, bank_statement, daily_withdrawals = withdrawal(bank_balance, bank_statement, daily_withdrawals)
        elif option == 'e':
            print('Extrato\n')
            print_statement(bank_balance, bank_statement)
        elif option == 'q':
            print('Sair\n')
            break
        else:
                print('Opção inválida/n')
    except Exception:
        print('Valor inválido\n')
    
    print(f'Saldo: R$ {bank_balance:.2f}\n')
    print(f'extrato: {bank_statement}\n')