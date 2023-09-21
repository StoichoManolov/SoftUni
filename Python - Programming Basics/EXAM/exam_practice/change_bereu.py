bitcoins = int(input())
chinese_yan = float(input())
commission = float(input())

chinese_in_euro = (chinese_yan * 0.15)
dolars_to_leva = chinese_in_euro * 1.76
bitcoins_euro = (bitcoins * 1168)

total = ((bitcoins_euro + dolars_to_leva) / 1.95)
total_with_commission = total - (total * (commission/100))
print(f'{total_with_commission:.2f}')
