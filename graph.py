import matplotlib.pyplot as plt

class Graph:
    def __init__(self, person):
        self.person = person
        dic = self.person.dict
        self.labels = []
        self.totalSpent = []
        for label, spent in dic.items():
            if spent != 0:
                self.labels.append(label)
                self.totalSpent.append(spent)

    def display(self):
        circle = plt.Circle((0, 0), 0.7, color="white")
        plt.pie(self.totalSpent, labels=self.labels, autopct="%1.1f%%")
        plt.axis("equal")
        p = plt.gcf()
        p.gca().add_artist(circle)
        plt.show()
def create_graph(person):
    return Graph(person)


