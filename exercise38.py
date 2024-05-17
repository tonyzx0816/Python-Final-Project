user_month = input()
month = ['January', 'February', 'March', 'April', 'May',
         'June', 'July', 'August', 'September', 'October',
         'November', 'December']
if user_month in month:
    if user_month == 'January':
        print('31 days')
    elif user_month == 'Februay':
        print('28 or 29 days')
    elif user_month == 'March':
        print('31 days')
    elif user_month == 'April':
        print('30 days')
    elif user_month == 'May':
        print('31 days')
    elif user_month == 'June':
        print('30 days')
    elif user_month == 'July':
        print('31 days')
    elif user_month == 'August':
        print('31 days')
    elif user_month == 'September':
        print('30 days')
    elif user_month == 'October':
        print('31 days')
    elif user_month == 'November':
        print('30 days')
    elif user_month == 'December':
        print('31 days')
else:
    print('Not valid')