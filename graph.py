import matplotlib.pyplot as plt

class Graph:
    def __init__(self, person):
        self.person = person

    def display(self):
        dic = self.person.dict
        labels = []
        sizes = []
        circle = plt.Circle((0, 0), 0.7, color="white")
        for label, size in dic.items():
            if size != 0:
                labels.append(label)
                sizes.append(size)
        plt.pie(sizes, labels=labels, autopct="%1.1f%%")
        plt.axis("equal")
        p = plt.gcf()
        p.gca().add_artist(circle)
        plt.show()

def create_graph(person):
    return Graph(person)


