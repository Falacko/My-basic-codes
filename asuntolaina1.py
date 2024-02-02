def main():
    VIITEKORKO = 1.3
    letters = ["A","B","C"]
    price = int(input("How much costs the house (euros)?\n"))
    savings = int(input("How much savings do you have (euros)?\n"))
    period = int(input("What is the loan period (years)?\n"))
    for letter in letters:
        opening_costs = int(input(f"What is the opening costs in bank {letter} (eur)?\n"))
        marginal_bank = float(input(f"What is the loan marginal in bank {letter} (percentage)?\n"))
        amount_of_loan = price - savings
        total_interest = marginal_bank + VIITEKORKO
        total = amount_of_loan * ((1 + total_interest / 100)**period * total_interest/100) / ((1 + total_interest/100)**period - 1)
        cheapest = (total * period + opening_costs) - amount_of_loan
        total = cheapest + amount_of_loan
    A = [0]
    B = [1]
    C = [2]
    if A <= B and A <= C:
        print(f"The bank A is the cheapest.")
    elif B <= A and B <= C:
        print(f"The bank B is the cheapest.")
    else:
        print(f"The bank C is the cheapest.")

    print(f"The costs for {period:d} years loan are {cheapest:.2f} euros.".format(period, cheapest))
    print(f"The total payment is {total:.2f} euros excluding own funding of {savings:.2f} euros.".format(total, savings))


main()