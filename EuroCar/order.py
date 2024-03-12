from receipt import Receipt
import os
import time
class Order:
    def __init__(self, pay, bought_cars) -> None:
        self.pay = pay 
        self.bought_cars = bought_cars

    def get_user_wishes(self, cars):
        wish = int(input("> "))
        order1.bought_cars.append(str(cars[wish-1].model))
        order1.pay += int(cars[wish-1].price)
        order1.days()

    def days(self):
        os.system("cls")
        print("\nFür wie viele Tage willst du dieses Fahrzeug mieten?")
        days = int(input("> "))
        self.pay = self.pay * days
        order1.goodbye()
    
    def goodbye(self):
        os.system("cls")
        print("\nDanke, dass Sie bei uns eingekauft haben!\nWir hoffen, dass wir Sie bald wiedersehen werden!")
        Receipt.print_receipt(self=self, pay=self.pay, bought_cars=self.bought_cars)
        time.sleep(3)


order1 = Order(0, [])
