
class Person:
    def __init__(self):
        self.dict = {"housing": 0.0,
            "transportation":0.0,
            "food":0.0,
            "utilities":0.0,
            "clothing":0.0,
            "healthcare":0.0,
            "insurance":0.0,
            "supplies":0.0,
            "personal":0.0,
            "debt":0.0,
            "retirement":0.0,
            "education":0.0,
            "savings":0.0,
            "donations":0.0,
            "entertainment ":0.0
        }
        self.budget = 0.0
        self.sum = 0.0
    
    def new_budget(self,budget):
        self.budget = budget

    def add_finance(self,t,price):
        self.dict[t] += price
        self.budget -= price
        self.sum += price

    def reset_dict(self):
        self.dict = {"housing": 0.0,
            "transportation":0.0,
            "food":0.0,
            "utilities":0.0,
            "clothing":0.0,
            "healthcare":0.0,
            "insurance":0.0,
            "supplies":0.0,
            "personal":0.0,
            "debt":0.0,
            "retirement":0.0,
            "education":0.0,
            "savings":0.0,
            "donations":0.0,
            "entertainment ":0.0,
        }
    def reset_budget(self):
        self.budget = 0.0
    def reset_sum(self):
        self.sum = 0.0

    

def inpt(m = ''):
    n = input(m)
    return n


def create_person():
    x = Person()
    return(x)




    