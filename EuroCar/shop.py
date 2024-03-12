import os
import time
from order import Order
class Store:
    def __init__(self) -> None:
        self.car = self.Car("", "", "", "", "")

    class Car:
        def __init__(self, _type, _id, model, bj, price) -> None:
            self.type = _type
            self.id = _id
            self.model = model
            self.bj = bj
            self.price = price

    def greeting(self):
        os.system("cls")
        print(f"Hallo {self.first_name} {self.last_name} und willkommen bei EuroCar!")
        time.sleep(3)
        store.show_types()

    def show_types(self):
        os.system("cls")
        print("Diese Typen an Autos bieten wir an!\n"+"Suchen Sie sich einfach das aus, was Ihnen am meisten zuspricht!\n"+"-"*50)
        print("1. PKWs\n2. LKWs\n")
        while True:
            choice = int(input("> "))
            if choice == 1:
                self.show_menu(choice=choice)
                break
            elif choice == 2:
                self.show_menu(choice=choice)
                break
            else:
                print("Dies ist keine Option")

    def show_menu(self, choice):
        os.system("cls")
        print(f"Diese Autos bieten wir momentan an!\n" + "-"*35)
        if choice == 1:
            _type = pkw
            print("\nPKWs\n")
            for i in range(len(pkw)):
                print(f"{pkw[i].id}. {pkw[i].model} aus dem Jahr {pkw[i].bj}, kostet {pkw[i].price}€ pro Tag.")
        else:
            _type = lkw
            print("\nLKWs\n")
            for i in range(len(lkw)):
                print(f"{lkw[i].id}. {lkw[i].model} aus dem Jahr {lkw[i].bj}, kostet {lkw[i].price}€ pro Tag.")
        print("\n")
        
        Order.get_user_wishes(self, cars=_type)


audi1 = Store.Car("PKW", "1", "Audi Q3", "2023", "45")
audi2 = Store.Car("PKW","2", "Audi Q4", "2024", "55")
mercedes = Store.Car("PKW","3", "Mercedes-Benz EQA", "2024", "60")
pkw = [audi1, audi2, mercedes]

mercedes2 = Store.Car("LKW","1", "Mercedes-Benz CharterWay", "2024", "110")
scania = Store.Car("LKW","2", "Scania R450", "2018", "100")
daf = Store.Car("LKW","3", "DAF XF 450", "2023", "130")
lkw = [mercedes2, scania, daf]

store = Store()