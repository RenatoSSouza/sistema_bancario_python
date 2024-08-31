menu = """
    [d] - Depositar
    [s] - Sacar
    [e] - Extrato
    [q] - Sair
    """
    
bank_balance = 0
bank_limit = 500
bank_statement = []
number_bank_withdrawals = 0
bank_withdrawls_limit = 3


while True:
    
    option = input(menu)
    option = option.lower()
    print(option)
    if option == 'd':
        print('Deposito/n')
        #logic to deposit
    elif option == 's':
        print('Saque/n')
        #logic to withdraw
    elif option == 'e':
        print('Extrato/n')
        #logic to show statement
    elif option == 'q':
        print('Sair/n')
        break
    else:
        print('Opção inválida/n')