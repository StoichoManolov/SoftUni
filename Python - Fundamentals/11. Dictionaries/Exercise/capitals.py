countries = input().split(', ')
cities = input().split(', ')

zipped = zip(countries, cities)

together = {country: capital for country, capital in zipped}

for item,value in together.items():
    print(f'{item} -> {value}')