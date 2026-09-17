class Dog:

    """
    Dog class
    
    Keeps track of a dog for a dog tracker application
    
    
    """

# init

    def __init__(self, 
                 name:str, 
                 breed:str, 
                 age:int, 
                 weight:float):
        """
        Constructor for Dog class

        Parameters
        name: Name of the dog
        breed: Breed of the dog
        age: Current age of the dog
        weight: Current weight of the dog

        """
        #raise NotImplementedError("Not implemented yet")
        self._name = name
        self._breed = breed
        self._age = age
        self._weight = weight
        self._last_meal_time = None
        self._last_walk_time = None



    # Accessors

    def is_fed(self):
        #Stub
        raise NotImplementedError("Not implemented yet")

    def is_walked(self):
        #Stub
        raise NotImplementedError("Not implemented yet")

    def is_healthy_weight(self):
        #Stub
        raise NotImplementedError("Not implemented yet")

    def bark(self):
        #Stub
        # raise NotImplementedError("Not implemented yet")
        print("Woof!")

    def get_weight(self):
        return self._weight
    
    # Mutators

    def feed(self):
        #Stub
        raise NotImplementedError("Not implemented yet")

    def walk(self):
        #Stub
        raise NotImplementedError("Not implemented yet")

    def set_weight(self, new_weight_in_kg : float):
        #Stub
        #raise NotImplementedError("Not implemented yet")
        self._weight = new_weight_in_kg


# Main Function
if __name__ == "__main__":
    waffle = Dog("Waffle", "Newfoundland (Landseer)", 8, 58.97)
    waffle.bark()
    print(waffle.get_weight())
    waffle.set_weight(57.23)
    print(waffle.get_weight())

    jazz = Dog("Jazz", "Goldendoodle", 6, 27.5)