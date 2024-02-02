def main():
    VIITEKORKO = 1.3
    letters = ["A", "B", "C"]
    
    price = int(input("How much costs the house (euros)?\n"))
    savings = int(input("How much savings do you have (euros)?\n"))
    period = int(input("What is the loan period (years)?\n"))

    cheapest_bank = None
    cheapest = float('inf')

    for letter in letters:
        opening_costs = float(input(f"What is the opening costs in bank {letter} (eur)?\n"))
        marginal_bank = float(input(f"What is the loan marginal in bank {letter} (percentage)?\n"))

        amount_of_loan = price - savings

        total_interest = VIITEKORKO + marginal_bank
        total1 = amount_of_loan * ((1 + total_interest / 100)**period * total_interest / 100) / (
                (1 + total_interest / 100)**period - 1)
        current = total1 * period + opening_costs
        total = current + savings

        if current < cheapest:
            cheapest = current
            cheapest_bank = letter

    print(f"The bank {cheapest_bank} is the cheapest.")
    print("The costs for {:d} years loan are {:.2f} euros.".format(period, cheapest))
    print("The total payment is {:.2f} euros excluding own funding of {:.2f} euros.".format(total, savings))



main()
