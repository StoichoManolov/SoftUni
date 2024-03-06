class Zoo:

    def __init__(self,name,budget,animal_capacity,workers_capacity):

        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self,animal,price):

        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        elif self.__animal_capacity > len(self.animals) and self.__budget < price:
            return 'Not enough budget'
        return 'Not enough space for animal'

    def hire_worker(self,worker):

        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return 'Not enough space for worker'

    def fire_worker(self,worker_name):
        try:
            worker = [w for w in self.workers if w.name == worker_name][0]
            self.workers.remove(worker)
            return f'{worker_name} fired successfully'
        except IndexError:
            return f'There is no {worker_name} in the zoo'

    def pay_workers(self):

        money_to_pay = sum([w.salary for w in self.workers])

        if money_to_pay <= self.__budget:
            self.__budget -= money_to_pay
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):

        money_to_feed = sum([a.money_for_care for a in self.animals])

        if money_to_feed <= self.__budget:
            self.__budget -= money_to_feed
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self,amount):

        self.__budget += amount

    def animals_status(self):
        result = f'You have {len(self.animals)} animals\n'

        amount_of_lions = [a for a in self.animals if a.__class__.__name__ == 'Lion']

        result += f'----- {len(amount_of_lions)} Lions:\n'

        for lion in amount_of_lions:
            result += f'{lion}\n'

        amount_of_tigers = [a for a in self.animals if a.__class__.__name__ == 'Tiger']

        result += f'----- {len(amount_of_tigers)} Tigers:\n'

        for tiger in amount_of_tigers:
            result += f'{tiger}\n'

        amount_of_cheetahs = [a for a in self.animals if a.__class__.__name__ == 'Cheetah']

        result += f'----- {len(amount_of_cheetahs)} Cheetahs:\n'

        for cheetah in amount_of_cheetahs:
            result += f'{cheetah}\n'

        return result[:-1]

    def workers_status(self):

        result = f"You have {len(self.workers)} workers\n"

        keepers = [w for w in self.workers if w.__class__.__name__ == 'Keeper']
        caretakers = [w for w in self.workers if w.__class__.__name__ == 'Caretaker']
        vets = [w for w in self.workers if w.__class__.__name__ == 'Vet']

        result += f'----- {len(keepers)} Keepers:\n'

        for keeper in keepers:
            result += f'{keeper}\n'

        result += f'----- {len(caretakers)} Caretakers:\n'

        for taker in caretakers:
            result += f'{taker}\n'

        result += f'----- {len(vets)} Vets:\n'

        for vet in vets:
            result += f'{vet}\n'

        return result[:-1]




