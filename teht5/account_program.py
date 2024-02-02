from account import Account

def create_accounts():
    name1 = input("Give the name of the first account owner.\n")
    name2 = input("Give the name of the first account owner.\n")

    ########################################################
    # Teht 1/6:
    # Luo kaksi tilia ylla annetuille nimille.
    ########################################################

    account1 =  Account(name1)
    account2 =  Account(name2)

    return account1, account2

def change_account_information(account, action_code):

    ########################################################
    # Teht 2/6:
    # Lisaa luottorajan muuttavan metodin kutsu ja
    # koron tilille laskevan metodin kutsu.
    ########################################################

    if action_code == 1:
        limit = float(input("What is the limit for the account?\n"))
        account.set_limit(limit)
         # lisaa luottorajan muuttava kasky tahan
    elif action_code == 2:
        account.get_interest()
           #lisaa koron tilille lisaava kasky tahan
    else:
        print("Error that is not reached except if you modified main.")


def deposit_to_account(account):
    amount = float(input("How much do you want to deposit to the account?\n"))

    ########################################################
    # Teht 3/6:
    # Lisaa tilille 'account' ylla kayttajalta pyydetty summa
    # (amount) kutsumalla sopivaa metodia.
    ########################################################

    added_amount =  account.deposit(amount)
    print("{:.2f} euros added to the account".format(added_amount))


def withdraw_if_possible(account):
    amount = float(input("How much do you want to widthdraw from the account?\n"))

    ########################################################
    # Teht 4/6:
    # Nosta tililta 'account' ylla kayttajalta pyydetty summa
    # (amount) kutsumalla sopivaa metodia. Lisaa tama
    # metodikutsu valintakaskyn ehtolauseeseen.
    ########################################################

    if account.withdrawal(amount):
        print("Withdrawal successfully done.")
    else:
        print("Withdrawal failed.")


def which_account_has_more_money(account1, account2):
    ########################################################
    # Teht 5/6:
    # Kayta valintakaskyn ehtolauseessa Account-luokan
    # metodia, joka suoraa vertailee kahden 'account'
    # olion saldojen suuruutta.
    # Lisaa metodikutsu, jolla selviaa taman tilin omistajan nimi.
    #########################################################
    account = None
    if  account1.compare_accounts(account2):
        account = account1
    else:
        account = account2


    name = Account.get_name()

    return name

def print_accounts(account1, account2):
    ########################################################
    # Teht 6/6:
    # Tulosta tilien tiedot kayttaen niiden __str__-metodia.
    ########################################################
    print("Account information:")
    print(account1) # taydenna tama rivi ekan tilin osalta
    print(account2) # taydenna tama rivi tokan tilin osalta


# Alla olevaa paaohjelmaa ei pida muokata millaan tavalla.
def main():

    account1, account2 = create_accounts()

    print("Adding limits")
    print("... for the first account")
    change_account_information(account1, 1)
    print("... for the second account")
    change_account_information(account2, 1)

    print("At the beginning")
    print_accounts(account1, account2)
    print()

    print("Deposit or withdraw:")
    action = input("Please choose deposit (press 'd'), withdraw (press 'w'), add interest (press 'i') or quit (press 'q')\n")
    while action != 'q':
        if action == 'd':
            print("Deposit to")
            print("...the first account:")
            deposit_to_account(account1)
            print("...the second account:")
            deposit_to_account(account2)
        elif action == 'w':
            print("Withdraw from")
            print("...the first account:")
            withdraw_if_possible(account1)
            print("...the second account:")
            withdraw_if_possible(account2)
        elif action == 'i':
            print("Adding interest to the accounts")
            change_account_information(account1, 2)
            change_account_information(account2, 2)
        elif action == 'q':
            print("Actions done, thank you.")
        else:
            print("Please try again.")

        print_accounts(account1, account2)
        print()
        action = input("Please choose deposit (press 'd'), withdraw (press 'w'), add interest (press 'i') or quit (press 'q')\n")


    print("Comparing accounts:")
    print(which_account_has_more_money(account1, account2), "has more money in the account.")
    print()

    print("At the end:")
    print_accounts(account1, account2)

main()