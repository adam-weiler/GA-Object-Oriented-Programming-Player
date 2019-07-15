class Player():
    def __init__(self):
        self.gold_coins = 0
        self.health_points = 10
        self.lives = 5

    def __str__(self):
        return f'Player instance:gold_coins={self.gold_coins} health_points={self.health_points} lives={self.lives}'

    def level_up(self):
        self.lives += 1

    def collect_treasure(self):
        self.gold_coins += 1
        
        if self.gold_coins % 10 == 0:
            self.level_up()



player_one = Player()
player_one.level_up()
player_one.level_up()
player_one.level_up()
player_one.collect_treasure()
player_one.collect_treasure()
player_one.collect_treasure()
player_one.collect_treasure()
player_one.collect_treasure()
player_one.collect_treasure()
player_one.collect_treasure()
player_one.collect_treasure()
player_one.collect_treasure()
player_one.collect_treasure()
print(player_one)
print()



player_two = Player()
print(player_two)