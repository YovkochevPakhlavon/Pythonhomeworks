class Animal:
    def __init__(self,diet,speed,weight):
        self.diet = diet
        self.speed = speed
        self.weight = weight
    def __str__(self):
        type_of_obj = type(self)
        name_of_obj = type_of_obj.__name__
        return f"{name_of_obj}: eats {self.diet}, average speed: {self.speed}, average weight: {self.weight}"
class Horse(Animal):
    def __init__(self, diet, speed, weight,power):
        super().__init__(diet, speed, weight)
        self.power = power

    def useage(self):
        return f'Horses are used for leisure activities, sports, and working purposes.'
    def horse_fact(self):
        return f"1 horsepower is equal to {self.power}"       
class Chicken(Animal):
    def __init__(self, diet, speed, weight,wingspan):
        super().__init__(diet, speed, weight)
        self.wingspan = wingspan
    def info_wingspan(self):
        return f'Chickens can have average wingspan about {self.wingspan} '

class Cow(Animal):
    def __init__(self, diet, speed, weight,fact):
        super().__init__(diet, speed, weight)
        self.fact = fact
    def cow_fact(self):
        return f'One interesting fact about cow is that {self.fact}'

horse = Horse('grass','50 km per hour','700 kg','746 W')
print(horse)
print(horse.useage())
print(horse.horse_fact())
print('--------------')
chicken = Chicken('corn','5 km per hour','20 kg','40-50 cm')
print(chicken)
print(chicken.info_wingspan())
print('--------------')
cow = Cow('grass','30 km per hour','500 kg','Cows have a great sense of smell and can smell things up to six miles away!')
print(cow)
print(cow.cow_fact())
       