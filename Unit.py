import Timer

class Unit:

    _Name = "-"
    _Health = 1
    _Attack = 1
    _Armor = 1

    def Name_setter(self, val: str):
        if not val.isalpha():
            raise TypeError
        self._Name = val

    def Name_getter(self):
        return self._Name

    Name = property(Name_getter, Name_setter)

    def Health_setter(self, val: str):
        if val.isdigit():
            val = int(val)
            if val == 0:
                raise ValueError
            self._Health = val
        else:
            raise TypeError


    def Health_getter(self):
        return self._Health

    Health = property(Health_getter, Health_setter)

    def Attack_setter(self, val: str):
        if val.isdigit():
            val = int(val)
            if val == 0:
                raise ValueError
            self._Attack = val
        else:
            raise TypeError


    def Attack_getter(self):
        return self._Attack

    Attack = property(Attack_getter, Attack_setter)

    def Armor_setter(self, val: str):
        if val.isdigit():
            val = int(val)
            if val == 0:
                raise ValueError
            self._Armor = val
        else:
            raise TypeError

    def Armor_getter(self):
        return self._Armor

    Armor = property(Armor_getter, Armor_setter)

    @Timer.Time_Decorator
    def __init__(self):
        while True:
            try:
                self.Name = input("Enter name: ")
            except TypeError:
                print("*" * 100)
                print("Name of unit must be a string")
                print("*" * 100)
                continue

            try:
                self.Health = input("Enter health: ")
                self.Attack = input("Enter attack: ")
                self.Armor = input("Enter armor: ")
                break
            except ValueError:
                print("*" * 100)
                print("The number must be greater than 0!")
                print("*" * 100)
                continue
            except TypeError:
                print("*" * 100)
                print("The number must be whole and positive!")
                print("*" * 100)
                continue

    def Info_of_Unit(self):
        print("*" * 100)
        print(f"Information of unit {self.Name}:")
        print(f"Health: {self.Health} \n"
              f"Damage: {self.Attack}\n"
              f"Armor: {self.Armor}")
        print("*" * 100)



