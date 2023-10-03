from typing import Dict, Union, Optional

class Computer:

    # What attributes will it need?
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, description: str, processor_type: str, hard_drive_capacity: int, memory: int, operating_system: str, year_made: int, price: int ):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price
        # You'll remove this when you fill out your constructor

    def print_computer(self):
        return{("description:", self.description)
        ("processor_type:", self.processor_type)
        ("hard_drive_capacity:", self.hard_drive_capacity)
        ("memory:", self.memory)
        ("operating_system:", self.operating_system)
        ("year_made", self.year_made)
        ("price:", self.price),}

    def set_price(self, new_price: int):
        self.price = new_price

    
    def set_os(self, new_os: int):
        self.operating_system = new_os

    def refurbish(self, new_os: Optional[str] = None):
        if self in self.inventory:
            if int(self["year_made"]) < 2000:
                self.set_price = 0 # too old to sell, donation only
            elif int(self["year_made"]) < 2012:
                self.set_price = 250 # heavily-discounted price on machines 10+ years old
            elif int(self["year_made"]) < 2018:
                self.set_price = 550 # discounted price on machines 4-to-10 year old machines
            else:
                self.set_price = 1000 # recent stuff
        if new_os is not None:
            self.set_os = new_os # update details after installing new OS
        else:
            print("Item", self.description, "not found. Please select another item to refurbish.")