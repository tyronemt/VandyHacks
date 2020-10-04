global p

p = []

class Person:
    def __init__(self, name):
        self.name = name
        self.dict = {"housing": 0,
            "transportation":0,
            "food":0,
            "utilities":0,
            "clothing":0,
            "healthcare":0,
            "insurance":0,
            "supplies":0,
            "personal":0,
            "debt":0,
            "retirement":0,
            "education":0,
            "savings":0,
            "donations":0,
            "entertainment":0,
        }
        self.budget = 0
    
    def new_budget(self,budget):
        self.budget = budget

    def add_finance(self,t,price):
        self.dict[t] += price
        self.budget -= price

    def reset_dict(self):
        self.dict = {"housing": 0,
            "transportation":0,
            "food":0,
            "utilities":0,
            "clothing":0,
            "healthcare":0,
            "insurance":0,
            "supplies":0,
            "personal":0,
            "debt":0,
            "retirement":0,
            "education":0,
            "savings":0,
            "donations":0,
            "entertainment ":0,
        }
    def reset_budget(self):
        self.budget = 0

    

def inpt(m = ''):
    n = input(m)
    return n


def in_class(username):
    for i in p:
        if username.lower() == i.name.lower():
            return (True,i)
    return (False,username)

def create_person(name):
    x = Person(name)
    p.append(x)
    return(x)




    