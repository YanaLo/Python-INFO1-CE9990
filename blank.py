while True:
    capital = input("How much capital do you have? ")
    capital = float(capital)

    rate = input("What percent interest are you getting? ")
    rate = float(rate)

    years = input("Compounded annually for how many years? ")
    years = float(years)

    fraction = 1 + rate / 100
    final = capital * fraction ** years 

    print("After ", years, " years, you will end up with $",
        round(final, 2), ".", sep = "")

    print() #Skip a line (i.e., output one newline character and nothing else).
