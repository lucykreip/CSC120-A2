from computer import *

class ResaleShop:

    # What attributes will it need?
    inventory = []


    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, inventory = [] ):
        self.inventory = inventory
         # You'll remove this when you fill out your constructor

    # What methods will you need?

    def print_inventory(self):
        if self.inventory:
        # For each item
            for self.description in self.inventory:
            # Print its details
                print(f'Item ID: {self.description} :')
        else:
            print("No inventory to display.")

    def sell (self, description: str, processor_type: str, hard_drive_capacity: int, memory: int, operating_system: str, year_made: int, price: int ):
        computer = Computer(description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price)
        self.inventory.remove(computer)

    def buy (self, description: str, processor_type: str, hard_drive_capacity: int, memory: int, operating_system: str, year_made: int, price: int ):
        computer = Computer(description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price)
        self.inventory.append(computer)

def main():
    
    # First, let's make a computer

    # Print a little banner
        print("-" * 21)
        print("COMPUTER RESALE STORE")
        print("-" * 21)

        # Add it to the resale store's inventory
        print("Buying", Computer.description)
        print("Adding to inventory...")
        Computer.buy(Computer)
        print("Done.\n")

        # Make sure it worked by checking inventory
        print("Checking inventory...")
        Computer.print_inventory
        print("Done.\n")

        # Now, let's refurbish it
        new_OS = "MacOS Monterey"
        print("Refurbishing Item ID:", Computer.description, ", updating OS to", new_OS)
        print("Updating inventory...")
        Computer.refurbish()
        print("Done.\n")

        # Make sure it worked by checking inventory
        print("Checking inventory...")
        Computer.print_inventory()
        print("Done.\n")
    
        # Now, let's sell it!
        print("Selling Item ID:", Computer.description)
        Computer.sell
    
        # Make sure it worked by checking inventory
        print("Checking inventory...")
        Computer.print_inventory()
        print("Done.\n")

# Calls the main() function when this file is run
if __name__ == "__main__": main()

    

    
