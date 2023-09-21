yearly_tax = int(input())

sneakers = yearly_tax * 0.60
jersey = sneakers * 0.80
ball = jersey * 0.25
accessories = ball * 0.20
cost = yearly_tax + sneakers + jersey + ball + accessories

print(cost)