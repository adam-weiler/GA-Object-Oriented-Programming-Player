class Player(): #A Player class.
    def __init__(self): #Every Player has attributes gold_coins, health_points, lives.
        self.restart() #Calls the restart method to set values to default.

    def __str__(self): #Returns a meaningful string that describes the instance.
        return f'Player instance:gold_coins={self.gold_coins} health_points={self.health_points} lives={self.lives}'

    def level_up(self): #An instance method that adds 1 to the Player's lives.
        self.lives += 1

    def collect_treasure(self): #An instance method that adds 1 to the Player's gold_coins. 
        self.gold_coins += 1
        
        if self.gold_coins % 10 == 0: #If gold_coins is divisible by 10 then Player gains a level.
            self.level_up()

    def do_battle(self, damage): #An instance method that subtracts damage from Player's health_points.
        self.health_points -= damage

        if self.health_points < 1: #If Player's health_points are less than 1, subtract a life and set health_points to 10.
            self.lives -= 1
            self.health_points = 10

        if self.lives == 0: #If Player's lives equals 0, Player's points are reset.
            self.restart()

    def restart(self): #Resets all values to their inital values.
        self.gold_coins = 0
        self.health_points = 10
        self.lives = 5


player_one = Player()
player_one.collect_treasure()
player_one.collect_treasure()
player_one.collect_treasure()
player_one.collect_treasure()
player_one.collect_treasure()
player_one.collect_treasure()
player_one.collect_treasure()
player_one.collect_treasure()
player_one.collect_treasure()
player_one.collect_treasure() #Player levels up and gains a life.
print(player_one) #Returns Player instance:gold_coins=10 health_points=10 lives=6
print()

player_two = Player()
player_two.do_battle(10)
player_two.do_battle(10)
player_two.do_battle(10)
player_two.do_battle(10)
player_two.do_battle(10) #Player dies and is reset.
print(player_two) #Returns Player instance:gold_coins=0 health_points=10 lives=5

#These are extra things inside the player_two object.
# print (player_two.__dict__) #Dictionary containing the class's namespace: {'gold_coins': 0, 'health_points': 10, 'lives': 5}
# print (player_two.__doc__) #Class documentation string: None
    # print (player_two.__name__) #Class name: There is no attribute __name__
# print (player_two.__module__) #Module name in which the class is defined: __main__
    # print (player_two.__bases__) #A possibly empty tuple containing the base classes, in the order of their occurance in the base class list: There is no attribute __bases__