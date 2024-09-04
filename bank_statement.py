from datetime import datetime

from services.convert_input import locate_value_br

def print_statement(bank_balance, bank_statement):

    bank_name = "DioBank"
    current_date = datetime.now().strftime("%d-%m-%Y")
    
    print(f"\n{'='*40}")
    print(f"{bank_name:^40}")
    print(f"Data do Extrato: {current_date:^40}")
    print(f"{'='*40}")
    
    if not bank_statement:
        print("Não foram realizadas movimentações.".center(40))
    else:
        print(f"{'Movimentação':<40}")
        print(f"{'-'*40}")
        
        for transaction in bank_statement:
            print(f"{transaction:<40}")
    
    formatted_value = str(locate_value_br(bank_balance))
    print(f"{'-'*40}")
    print(f"{'Saldo Atual':<30} {formatted_value}")
    print(f"{'='*40}\n")