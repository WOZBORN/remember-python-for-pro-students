import time

class Fighter:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.__is_alive = True

    def __add__(self, other: Fighter):
        self.name += other.name
        self.hp += other.hp
        self.attack += other.attack
        self.__money += other.__money

    def hit(self, damage: int):
        self.hp -= damage
        if self.hp <= 0:
            self.__is_alive = False
        

def create_fighter():  ## Унести в .__init__
    name = input("Введите имя бойца: ")
    hp = int(input("HP: "))
    attack = int(input("Сила удара: "))
    return Fighter(name, hp, attack)

def show_players(players: list[Fighter]):  ## Унести в __repr__
    for i, p in enumerate(players):
        print(f"{i+1}. {p.name}")
        print(f"HP: {p.hp}")


def fight(a, b):  ## Унести в метод .fight (где наноится урон методом .hit)
    while a.hp > 0 and  b.hp > 0:
        a.hp -= b.attack
        b.hp -= a.attack
        print(f"{a.name} - HP: {a.hp}")
        print(f"{b.name} - HP: {b.hp}")
        time.sleep(1)
    if a.hp == b.hp: print("Ничья!")
    else: print(a.name if a.hp > b.hp else b.name, "победил!")

def remove_dead(players):  ## Унести в метод .is_alive / .is_dead
    for p in players:
        if p.hp <= 0:
            players.remove(p)


## Сделать метод получения урона .hit

players = []
for i in range(2):
    players.append(create_fighter())

print(players[0] + players[1])
print(players[0].__money)

# Добавить абстрактный метод и пронаследоваться от него
# Можете сделать Fighter - абстрактным классом
# И, наследуясь от него, сдеать 2-3 разных класса бойца с небольшими отличиями (абстракция и полиморфизм - помним?)
