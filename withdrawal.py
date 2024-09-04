from datetime import datetime
from services.convert_input import convert_input, locate_value_br

def withdrawal(bank_balance, bank_statement, daily_withdrawals, max_withdrawals=3, max_withdrawal_amount=500.00):
    if daily_withdrawals >= max_withdrawals:
        print("Você atingiu o limite diário de saques!")
        return bank_balance, bank_statement, daily_withdrawals
    
    withdrawal_value = convert_input((input('Digite o valor do saque: R$ ')))
    
    formatted_value = locate_value_br(withdrawal_value)

    if withdrawal_value <= 0:
        print('Valor inválido!')
    elif withdrawal_value > max_withdrawal_amount:
        print(f'Valor excede o limite máximo de R$ {locate_value_br(max_withdrawal_amount)} por saque.')
    elif withdrawal_value > bank_balance:
        print('Saldo insuficiente.')
    else:
        bank_balance -= withdrawal_value
        daily_withdrawals += 1
        bank_statement.append(f'Saque: R$ {formatted_value} data: {datetime.now().strftime("%H:%M:%S %d-%m-%Y")}')
        print(f'Saque de R$ {formatted_value} efetuado com sucesso!')
        
    return bank_balance, bank_statement, daily_withdrawals