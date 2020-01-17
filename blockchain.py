#Establish block

blockchain = []

def get_last_block_value():
    ''' Returns the last value of the current block '''
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=[1]):
    ''' Append a new value as well as the last clock value to the block '''
    ''' Args ::: transaction_account | last_trnasaction '''

    blockchain.append([last_transaction, transaction_amount])


def get_user_input():
    ''' returns the input of the user '''
    user_input = float(input('Your transaction amount please: '))
    return user_input


tx_amount = get_user_input()
add_value(tx_amount)


tx_amount = get_user_input()
add_value(last_transaction=get_last_block_value(), transaction_amount=tx_amount)


tx_amount = get_user_input()
add_value(tx_amount, get_last_block_value())


print(blockchain)