class VenderShop():

    def sell_dog_to(self, owner: Human):
        dog = Dog();
        dog.name = "Toby";
        dog.owner = owner;

        owner.pet = dog;
    }
}
