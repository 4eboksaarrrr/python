class User:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


    def print_info(self):
            print(' name: {}\n zarplata: {}\n'.format(
                self.name, self.salary)
            )