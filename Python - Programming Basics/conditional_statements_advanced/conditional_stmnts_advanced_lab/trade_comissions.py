city = input().lower()
sales = float(input())
cities = 'sofia', 'plovdiv', 'varna'
commission = 0
if city == 'sofia':
    if 0 <= sales <= 500:
        commission = 0.05
    elif 500 < sales <= 1000:
        commission = 0.07
    elif 1000 < sales <= 10000:
        commission = 0.08
    elif sales > 10000:
        commission = 0.12

if city == 'varna':
    if 0 <= sales <= 500:
        commission = 0.045
    elif 500 < sales <= 1000:
        commission = 0.075
    elif 1000 < sales <= 10000:
        commission = 0.10
    elif sales > 10000:
        commission = 0.13

if city == 'plovdiv':
    if 0 <= sales <= 500:
        commission = 0.055
    elif 500 < sales <= 1000:
        commission = 0.08
    elif 1000 < sales <= 10000:
        commission = 0.12
    elif sales > 10000:
        commission = 0.145

if city not in cities or commission == 0:
    print('error')
else:
    total_commission = sales * commission
    print(f'{total_commission:.2f}')


