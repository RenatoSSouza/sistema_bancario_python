from deposit import deposit


menu = """
    [d] - Depositar
    [s] - Sacar
    [e] - Extrato
    [q] - Sair\n
    """
    
bank_balance = 0
bank_limit = 500
bank_statement = []
number_bank_withdrawals = 0
bank_withdrawls_limit = 3


while True:
    
    option = input(menu)
    option = option.lower()
    try:
        if option == 'd':
            print('Deposito\n')
            bank_balance, bank_statement = deposit(bank_balance, bank_statement)
        elif option == 's':
            print('Saque\n')
            #logic to withdraw
        elif option == 'e':
            print('Extrato\n')
            #logic to show statement
        elif option == 'q':
            print('Sair\n')
            break
        else:
                print('Opção inválida/n')
    except Exception:
        print('Valor inválido\n')
    
    print(f'Saldo: R$ {bank_balance:.2f}\n')
    print(f'extrato: {bank_statement}\n')