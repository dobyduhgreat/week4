

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def change_password(self, password):
        self.password = password
        print('Your Password ahs been changed to', self.password)


class BankUser(User):
    def __init__(self, name, email, password):
        super().__init__(name,email,password)
        self.balance = 0

    def check_bal(self):
        print(f'{self.name} has an account a balance of {self.balance}')

bankuser1 = BankUser('Pip','pip@pip.pip','passpip')

bankuser1.check_bal()