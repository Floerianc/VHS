import os
from pathlib import Path 
os.chdir(Path(__file__).parent)
class Receipt:
    def print_receipt(self, pay, bought_cars):
        with open("receipt.txt", "w", encoding="UTF-8") as f:
            f.write(f"Sie buchen: {bought_cars} und müssen {pay}€ bezahlen.")
        print(f"Sie buchen: {bought_cars} und müssen {pay}€ bezahlen.")