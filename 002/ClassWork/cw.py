import decimal

CMD_DEPOSIT = 'п'
CMD_WITHDRAW = 'c'
CMD_EXIT = 'в'
MULTIPLICITY = 50
PERCENT_REMOVAL = decimal.Decimal(15) / decimal.Decimal(1000)
MAX_REMOVAL = 30
MIN_REMOVAL = 600
PERCENT_DEPOSIT = decimal.Decimal(3) / decimal.Decimal(100)
COUNTER_OPERATION = 3
RICHNESS_SUM = 5_000_000
RICHNESS_PERCENT = decimal.Decimal(10) / decimal.Decimal(100)

bank_account = 0
counter = 0

comand = input(f'пополнить - {CMD_DEPOSIT}, снять - {CMD_WITHDRAW}, выйти - {CMD_EXIT}')
while comand != CMD_EXIT:
    if bank_account > RICHNESS_SUM:
        sum_percent = bank_account * RICHNESS_PERCENT
        bank_account -= sum_percent

    if comand == (CMD_DEPOSIT, CMD_WITHDRAW):
        counter += 1
        amount = 0
        while amount % MULTIPLICITY != 0:
            amount = decimal.Decimal(f'Vvedite summu kratnuy {MULTIPLICITY} ->')

        if comand ==CMD_DEPOSIT:
            bank_account += amount
        elif comand ==CMD_WITHDRAW:
            new_amount = amount * PERCENT_REMOVAL
            bank_account -= amount
