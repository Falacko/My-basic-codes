class Account:
    def __init__(self, customer_name):
        self.__name = customer_name
        self.__id = "Not in use, hahahaa"
        self.__saldo = 0.0
        self.__limit = 0.0
        self.__interest = 0.10
    
    def get_name(self):
        return self.__name
    
    def get_saldo(self):
        return self.__saldo
    
    
    def set_limit(self, new_limit):
        if new_limit >= 0:
            self.__limit = new_limit
        
    
    def deposit(self, amount):
        if self.__saldo < self.__limit:
            if self.__saldo - self.__limit < amount:    
                add_depo = (self.__limit - self.__saldo) * 2
                amount -= add_depo
            else:
                add_depo = amount
                amount = 0
        self.__saldo += amount
        return amount
            
    def withdrawal(self, amount):
        if self.__saldo - amount >= -self.__limit:
            self.__saldo -= amount
            return True
        else:
            return False
             
    
    def interest(self):
        if self.__saldo < 0:
            self.__saldo -= self.__interest * self.__saldo
        else:
            self.__saldo += self.__saldo * (self.__interest / 10)
        
        return self.__saldo
    
    
    def compare_accounts(self, other_account):
        return self.__saldo > other_account.get_saldo()
    
    def __str__(self):
        return "{}: saldo: {} eur, limit: {} eur, interest: {}%".format(self.__name, self.__saldo, self.__limit, self.__interest)