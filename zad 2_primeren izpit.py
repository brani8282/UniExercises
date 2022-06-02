class Travel:
    def __init__(self,id,destination,flight,price):
        self.id=id
        self.destination=destination
        self.flight=flight
        self.price=price
    def reduce(self):
        if self.price>200:
            self.price=(self.price-(((self.price)*10)//100))
            
    def print_info(self):
        print("Your ID is:",self.id,",your destination is:",self.destination,",flight:",self.flight,",flight price:",self.price,"euro.")


person1=Travel("Ivan Ivanov","London","business",150)
person1.reduce()
person1.print_info()