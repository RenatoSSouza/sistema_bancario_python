from babel.numbers import format_currency

def convert_input(value):
    return float(value.replace(',', '.'))

def locate_value_br(valor):
    return format_currency(valor, 'BRL', locale='pt_BR')