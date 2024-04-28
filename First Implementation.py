def car_price(year, first_price, annual_increase):
    first_year = 1986
    price = first_price
    while first_year < year:
        price = price + (price * annual_increase/100)
        first_year += 1
        print(f"The price is now {price} and the year is {first_year}")
    The_year = "The price of the car in {} is {} naira"
    print(The_year.format(year, price))


car_price(2024, 1500, 9)
