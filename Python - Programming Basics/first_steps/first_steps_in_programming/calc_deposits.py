deposit_sum = float(input())
deposit_time = int(input())
yearly_percent = float(input()) / 100

# сума = депозирана сума + срок на депозита * ((депозирана сума * годишен лихвен процент ) / 12)
# 1. Изчисляваме натрупаната лихва: 200 * 0.057 (5.7%) = 11.40 лв.
# 2. Изчисляваме лихвата за 1 месец: 11.40 лв. / 12 месеца = 0.95 лв.
# 3. Общата сума е: 200 лв. + 3 * 0.95 лв. = 202.85 лв.
sum = deposit_sum + deposit_time * ((deposit_sum * yearly_percent)/12)
print(sum)

# 200 * 5.7