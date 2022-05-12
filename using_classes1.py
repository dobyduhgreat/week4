# class Player:
#     max_hp = 4000 #class attribute: attached to class

# player1 = Player()

# print(player1.max_hp)
# player2 = Player()
# print(player2.max_hp)

# Player.max_hp = 5000
# print(player1.max_hp)
# print(player2.max_hp)

class Player:
    def __init__(self, name, hp):  # contructor method (creates class)
        self.name = name
        self.hp = hp
        self.score = 0


player1 = Player('Aaron', 1333)
player2 = Player('Irene', 1550)

print('P1: ', player1.name, " --HP: ", player1.hp, ' --Score: ', player1.score)
print('P2: ', player2.name, " --HP: ", player2.hp, ' --Score: ', player2.score)
player1.score += 10
player1.hp +=500
print('P1: ', player1.name, " --HP: ", player1.hp, ' --Score: ', player1.score)
print('P2: ', player2.name, " --HP: ", player2.hp, ' --Score: ', player2.score)