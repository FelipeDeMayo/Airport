import os
from collections import deque

class Plane:
    def __init__(self, model, company, origin, destiny, capacity, number):
        self.model = model 
        self.company = company
        self.origin = origin
        self.destiny = destiny
        self.capacity = capacity
        self.number = number 

    def __str__(self):
        return (f"Plane {self.model} ({self.company}) from {self.origin} "
                f"to {self.destiny}, Capacity: {self.capacity}, "
                f"Flight Number: {self.number}")

plane_1 = Plane("Antonov An-124 Ruslan", "Delta Air Lines", "China", "Russia", 
                438, 777)
plane_2 = Plane("Boeing 747-8 Freighter", "American Airlines", "Canada", 
                "Brazil", 410, 1312)
plane_3 = Plane("Airbus BelugaXL", "IAG (British Airways & Iberia)", "Mexico", 
                "United States", 500, 804)
plane_4 = Plane("Boeing 777-8 Freighter", "Turkish Airlines", "Turkey", 
                "France", 301, 603)

queue = deque([plane_4, plane_3, plane_1, plane_2])

def find_plane_position(queue, flight_number): 
    for index, plane in enumerate(queue):
        if plane.number == flight_number:
            return index + 1 
    return None

def clear_options():
    if os.name == 'nt': 
        os.system('cls')
    else:  
        os.system('clear')

while True:

    options = input(
        "\nEnter\n(1) To list all planes in the takeoff queue\n"
        "(2) To authorize the takeoff of the first plane\n"
        "(3) To show the position of a plane according to the flight number\n"
        "(4) To view details of the next plane to take off\n"
        "(5) To authorize the takeoff of the next plane\n"
        "(6) To list the characteristics of the next plane\n"
        "(7) To show the total number of planes in the queue\n"
        "(0) To exit the program\n"
    )
    clear_options()

    valid_options = {'1', '2', '3', '4', '5', '6', '7', '8', '0'}
    if options not in valid_options:
        print("Invalid input. Please enter a valid option.")
        continue

    if options not in ('1', '2', '3', '4', '5', '6', '0', '7'):
        print("Invalid input. Please enter 1, 2, 3, 4, 5, 6, 7 or 0.")
        continue

    if options == '1':
        if queue:
            print(f"Total planes in the queue: {len(queue)}")
            for plane in queue:
                print(plane)
        else:
            print("No planes left in the queue.")
    
    elif options in ['2', '5']: 
        if queue:
            print(f"The takeoff of {queue[0]} is authorized")
            queue.popleft()
        else:
            print("No planes left in the queue.")

    elif options == '3':
        while True:
            try:
                flight_number = int(input(
                    "Enter the flight number to find its position: "
                ))
                break
            except ValueError:
                print("Invalid input. Please enter a valid flight number.")
        
        position = find_plane_position(queue, flight_number)
        
        if position:
            print(
                f"The plane with flight number {flight_number} "
                f"is in position {position} in the queue."
            )
        else:
            print(
                f"No plane with flight number {flight_number} "
                "found in the queue."
            )

    elif options == '4' or options == '6':
        if queue:
            print("Details of the next plane to take off:")
            print(queue[0])
        else:
            print("No planes left in the queue.")
    
    elif options == '7':
        print(f"Total number of planes in the queue: {len(queue)}")

    elif options == '0':
        print("Exiting the program.")
        break