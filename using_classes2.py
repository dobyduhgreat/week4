

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def change_password(self, password):
        self.password = password
        print('Your Password ahs been changed to', self.password)


user1 = User('Jane', 'jane@nucamp.co', 'password')
print(user1.password)
user1.change_password('NewPass111')
print(user1.password)
