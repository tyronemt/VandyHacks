import matplotlib.pyplot as plt

class Graph:
    def __init__(self, person):
        self.person = person
        dic = self.person.dict
        self.total = []
        totalSpent = 0
        for label, spent in dic.items():
            totalSpent += spent
        remains = self.person.budget - totalSpent
        self.labels = ["Amount Spent\n" + "($" + str(totalSpent) + ")", "Amount Left\n" + "($" + str(remains) + ")"]
        self.total.append(totalSpent)
        self.total.append(remains)

    def display(self):
        circle = plt.Circle((0, 0), 0.8, color="white")
        explode = (0.05, 0)
        plt.pie(self.total, explode=explode, labels=self.labels, autopct='%1.1f%%')
        plt.axis("equal")
        p = plt.gcf()
        p.gca().add_artist(circle)
        plt.show()
def create_graph(person):
    return Graph(person)


