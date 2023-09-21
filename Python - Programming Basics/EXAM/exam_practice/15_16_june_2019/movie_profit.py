film_name = input()
days = int(input())
tickets = int(input())
tickets_price = float(input())
cinema_tax = int(input())

price_for_day = tickets_price * tickets
price_for_all_days = price_for_day * days

percent_for_cinema = price_for_all_days - (price_for_all_days * (cinema_tax / 100))

print(f'The profit from the movie {film_name} is {percent_for_cinema:.2f} lv.')