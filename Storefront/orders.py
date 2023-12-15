class Beverage:
    def __init__(self, size):
        self.size = size
        
    def to_dict(self):
        return {
            "size": self.size, 
        }

## Drink classes

class Coffee(Beverage):
    def __init__(self, size, milk, sugar, type):
        super().__init__(size)
        self.milk = milk
        self.sugar = sugar
        self.type = type
        self.price = 0
        
        if type == "Brewed Coffee":
            self.price = 2.5
        elif type == "Americano":
            self.price = 2.5
        elif type == "Cappuccino":
            self.price = 2.5
        elif type == "Latte":
            self.price = 2.5
        elif type == "Mocha":
            self.price = 2.5
        elif type == "Iced Coffee":
            self.price = 2.5
        elif type == "Iced Latte":
            self.price = 2.5
        elif type == "Cold Brew":
            self.price = 2.5
        elif type == "Seasonal Special: Pumpkin Spice Latte":
            self.price = 2.5


    def describe(self):
        return(f"{self.size} {self.type} coffee with {self.milk} milk and {self.sugar} sugar")
    
    def to_dict(self):
        return {
            **super().to_dict(), 
            "milk": self.milk, 
            "sugar": self.sugar, 
            "type": self.type, 
            "price": self.price
        }

class Tea(Beverage):
    def __init__(self, size, sugar, type):
        super().__init__(size)
        self.sugar = sugar
        self.type = type
        self.price = 2.0
    
    def describe(self):
        return(f"{self.size} {self.type} tea with {self.sugar} sugar")

    def to_dict(self):
        return {
            **super().to_dict(), 
            "sugar": self.sugar, 
            "type": self.type, 
            "price": self.price
        }

class Espresso(Beverage):
    def __init__(self, size):
        super().__init__(size)
        self.price = 2.0
        
    def describe(self):
        return(f"{self.size} espresso")
    
    def to_dict(self):
        return {
            **super().to_dict(), 
            "price": self.price
        }



class Chai(Beverage):
    def __init__(self, size, sugar, milk):
        super().__init__(size)
        self.sugar = sugar
        self.milk = milk
        self.price = 3.5

    def describe(self):
        return(f"{self.size} chai latte")
    
    def to_dict(self):
        return {
            **super().to_dict(), 
            "sugar": self.sugar, 
            "milk": self.milk, 
            "price": self.price
        }

class HotChocolate(Beverage):
    def __init__(self, size, milk):
        super().__init__(size)
        self.milk = milk
        self.price = 3.0
    
    def describe(self):
        return(f"{self.size} hot chocolate with {self.milk} milk")
    
    def to_dict(self):
        return {
            **super().to_dict(), 
            "milk": self.milk, 
            "price": self.price
        }

class Lemonade(Beverage):
    def __init__(self, size):
        super().__init__(size)
        self.price = 2.5
    
    def describe(self):
        output = f"{self.size} lemonade"
        return output
    
    def to_dict(self):
        return {
            **super().to_dict(), 
            "price": self.price
        }


class IcedTea(Beverage):
    def __init__(self, size, sweet):
        super().__init__(size)
        self.sweet = sweet
        self.price = 2.5
    
    def describe(self):
        output = f"{self.size}"
        
        if self.sweet == True:
            output += " unsweetened"
        else:
            output += " sweetened"

        output += " iced tea"

        return output
    
    def to_dict(self):
        return {
            **super().to_dict(), 
            "sweet": self.sweet, 
            "price": self.price
        }


# Food classes

class Croissant:
    def __init__(self, warmed, type):
        self.warmed = warmed
        self.type = type
        self.price = 2.5
    
    def describe(self):
        output = f"{self.type} croissant"

        if self.warmed == True:
            output += " - warmed"

        return output
    
    def to_dict(self):
        return {
            "warmed": self.warmed, 
            "type": self.type, 
            "price": self.price
        }


class Muffin:
    def __init__(self, warmed, type):
        self.warmed = warmed
        self.type = type
        self.price = 2.75
    
    def describe(self):
        output = f"{self.type} muffin"

        if self.warmed == True:
            output += " - warmed"

        return output
    def to_dict(self):
        return {
            "warmed": self.warmed, 
            "type": self.type, 
            "price": self.price
        }




class Cookie:
    def __init__(self, type, warmed):
        self.type = type
        self.warmed = warmed
        self.price = 1.5
    
    def describe(self):
        output = f"{self.type} cookie"

        if self.warmed == True:
            output += " - warmed"

        return output
    
    def to_dict(self):
        return {
            "type": self.type, 
            "warmed": self.warmed, 
            "price": self.price
        }


class Brownie:
    def __init__(self, warmed):
        self.warmed = warmed
        self.price = 2.0
    
    def describe(self):
        output = "Brownie"

        if self.warmed == True:
            output += " - warmed"
        
        return output
    
    def to_dict(self):
        return {
            "warmed": self.warmed, 
            "price": self.price
        }


class Scone:
    def __init__(self, type, warmed):
        self.type = type
        self.warmed = warmed
        self.price = 2.75
    
    def describe(self):
        output = f"{self.type} scone"

        if self.warmed == True:
            output += " - warmed"

        return output
    
    def to_dict(self):
        return {
            "type": self.type, 
            "warmed": self.warmed, 
            "price": self.price
        }   


class Cheesecake:
    def __init__(self, type):
        self.type = type
        self.price = 4.0
    
    def describe(self):
        output = f"{self.type} cheesecake"
        
        return output
    
    def to_dict(self):
        return {
            "type": self.type, 
            "price": self.price
        }