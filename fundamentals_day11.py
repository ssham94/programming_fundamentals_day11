emotion_list = {'Happy' : 3, 'Anger': 1, 'Stress' : 2, 'Confused' : 1, 'Hunger' : 2}

class Person:
    def __init__(self, give_name, emotions_felt):
        self.name = give_name
        self.emotions = emotions_felt

    def __str__(self):
        return f"Name: {self.name}, Emotions felt: {self.emotions}"

    def emotion_level(self):
        for k in self.emotions.keys():
            if self.emotions[k] == 1: 
                print(f"I am feeling a low level amount of {k}")
            elif self.emotions[k] == 2:
                print(f"I am feeling a medium level amount of {k}")
            elif self.emotions[k] == 3:
                print(f"I am feeling a high level amount of {k}")

    
stanley = Person('Stanley', emotion_list)
print(stanley)
stanley.emotion_level()
