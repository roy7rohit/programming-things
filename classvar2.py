class Shark:

    animalType = []
    location = 'ocean'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_followers(self, followers):
        print('this user has ' + str(followers) + 'followers')

    def fishtype(self):
        animalType.fishtype.append('dog')

def main():
    sammy = Shark('sammy', 5)
    print(sammy.name)
    print(sammy.location)
    sammy.set_followers(77)
    # print(sammy.fishtype())

if __name__ == '__main__':
    main()
