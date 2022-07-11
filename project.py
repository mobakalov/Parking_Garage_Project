class Garage():
    tickets = [{1:""}, {2:""}, {3:""}, {4:""}, {5:""}]
    parking_spaces = [{1:""}, {2:""}, {3:""}, {4:""}, {5:""}]
    current_ticket = {}
    
    def take_tickets(self):
        if self.tickets:
            print(self.tickets[0])
            self.current_ticket.update(self.tickets[0])
            del self.tickets[0]
            del self.parking_spaces[0]
        else:
            print("Garage is currently full, please try again later")
            
    def pay_for_parking(self):
        while True: 
            pay = int(input("Please enter your ticket number"))
            if 0 < pay < 5 and pay in self.current_ticket:
                if self.current_ticket[pay]:
                    print("Your ticket has been paid and you have 15 minutes to leave.")
                    break
                else: 
                    self.current_ticket[pay] = "paid"
                    print("Thank you, have a nice day!")
                    break
            else:
                break
                  
    def leave_garage(self):
        while True:
            exit = int(input("What is your ticket number?"))
            if 0 < exit < 5 and exit in self.current_ticket:
                if self.current_ticket[exit] == ("paid"):
                    print("Thank you! Have a nice day!")
                    self.current_ticket[exit] 
                    self.tickets.append(self.current_ticket)
                    self.parking_spaces.append(self.current_ticket)
                    break
                else:
                    print("Your ticket has not been paid")
                    break
            else: 
                print("Invalid entry, please try again")
                break
            
    def UserInput(self):
        while True:
            response = str(input("What would you like to do? Enter, Pay, Exit, or Quit")).lower()
            if response == "enter":
                self.take_tickets()
            elif response == "pay":
                self.pay_for_parking()
            elif response == "exit":
                self.leave_garage()
            elif response == "quit":
                print("Have a nice day!")
                break
            else:
                print("Invalid answer, please try again!")
                
test = Garage()
test.UserInput()









