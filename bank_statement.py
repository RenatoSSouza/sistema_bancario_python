from datetime import datetime

def print_statement(bank_balance, bank_statement):
    # Nome do banco e data do extrato
    bank_name = "DioBank"
    current_date = datetime.now().strftime("%d-%m-%Y")
    
    # Cabeçalho do extrato
    print(f"\n{'='*40}")
    print(f"{bank_name:^40}")
    print(f"Data do Extrato: {current_date:^40}")
    print(f"{'='*40}")
    
    # Verificar se há movimentações
    if not bank_statement:
        print("Não foram realizadas movimentações.".center(40))
    else:
        # Cabeçalho da tabela
        print(f"{'Movimentação':<40}")
        print(f"{'-'*40}")
        
        # Exibir movimentações
        for transaction in bank_statement:
            print(f"{transaction:<40}")
    
    # Exibir saldo atual
    print(f"{'-'*40}")
    print(f"{'Saldo Atual':<30} R$ {bank_balance:>8.2f}")
    print(f"{'='*40}\n")