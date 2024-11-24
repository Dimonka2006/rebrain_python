# Программа должна выводить время года по вводимому названию месяца
month = input()
# if month == 'January' or month == 'February' or month == 'Desember':
#     print('Winter is coming')
# elif month == 'March' or month == 'April' or month == 'May':
#     print('Of the spring!') 
# elif month == 'June' or month == 'July' or month == 'August':
#     print('summer')
# elif month == 'September' or month == 'October' or month == 'November':
#     print('autumn')

if month in ['January', 'February', 'Desember']:
    print('Winter is coming')
elif month in ['March', 'April', 'May']:
    print('Of the spring!') 
elif month in ['June', 'July', 'August']:
    print('summer')
elif month in ['September', 'October', 'November']:
    print('autumn')