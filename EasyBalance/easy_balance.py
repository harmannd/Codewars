import re

def balance(book):
    result = ""
    total_expense = 0
    count = 0
    pattern = re.compile('[^a-zA-Z0-9\.]+')

    input = book.split('\n')
    original_balance = float(pattern.sub('', input[0]))
    current_balance = original_balance
    result += 'Original Balance: ' + '{0:.2f}'.format(original_balance) + '\r\n'

    for x in range(1, len(input)):
        if input[x].strip():
            count += 1
            entry = pattern.sub(' ', input[x]).strip().split(' ')
            total_expense += float(entry[2])
            current_balance -= float(entry[2])
            entry[2] = '{0:.2f}'.format(float(entry[2]))
            result += ' '.join(entry) + ' Balance ' + '{0:.2f}'.format(current_balance) + '\r\n'

    result += 'Total expense  ' + '{0:.2f}'.format(original_balance - current_balance) + '\r\n'
    result += 'Average expense  ' + '{0:.2f}'.format(total_expense / count)
    return result