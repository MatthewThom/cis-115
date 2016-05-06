class Pet:
    def __init__(self):
        Pet.__name = "Kitty"
        Pet.__animal_type = "cat"
        Pet.__age = 1

    def set_name(self):
        Pet.__name = input("What is the pet's name?")

    def set_animal_type(self):
        Pet.__animal_type = input("What type of animal is the pet?")

    def set_age(self):
        Pet.__age = input("How old (in years) is the pet?")

    def get_name(self):
        print(Pet.__name)

    def get_animal_type(self):
        print(Pet.__animal_type)

    def get_age(self):
        print(Pet.__age)

def main():
    pet = Pet()
    pet.set_name()
    pet.set_animal_type()
    pet.set_age()
    pet.get_name()
    pet.get_animal_type()
    pet.get_age()

main()
