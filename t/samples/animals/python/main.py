import dog
import cat
from animal import Animal
from mammal import Mammal

def main(): 
    dog: Animal = dog.Dog("Odie");
    cat: Mammal = cat.Cat("Garfield");
    print(dog.name())
    print(cat.name())

if __name__ == '__main__':
    main()

