#!/usr/bin/env python
# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt
import random

class Knn():
    def __init__(self, points=None, result=None, lenght=5, k=3):
        if points == None:
            self.points = [(random.random(), random.random()) for x in range(lenght)]
            self.lenght = lenght
            if k > len(self.points):
                k = 3
        else:
            self.lenght = len(self.points)
        if result == None:
            self.result = [random.randint(0, 1) for x in range(lenght)]
        elif len(result) != len(self.points):
            self.result = [random.randint(0, 1) for x in range(lenght)]
        else:
            self.result = result
        self.k = k

    # Определяем групповую принадлежность элемента на основе k ближайших соседей
    def predict(self, new):
        # Ищем расстояния от точки new до всех элеметов и заполняем distance. В group лежат соответсвующие элементам группы
        distance = []
        group = []
        for i in range(len(self.points)):
            distance.append(((new[0] - self.points[i][0]) ** 2 + (new[1] - self.points[i][1]) ** 2) ** 0.5)
            group.append(self.result[i])
        # Находим k ближайших элементов и добявляем в списко dop - дополнительный список
        dop = []
        for i in range(self.k):
            ind = distance.index(min(distance))
            value = distance[ind]
            distance[ind] = max(distance) + 55
            dop.append(self.result[ind])
        # Находим самую популярную по группе точку
        freq = {}
        for el in dop:
            freq[el] = freq.get(el, 0) + 1
        z = list(freq.items())
        z.sort(key=lambda x: x[1])
        print(z)
        return z[-1][0]

    # Добавляем в множество точек точку new, при этом определяя её групповую принадлежность
    def fit(self, new):
        answer = self.predict(new)
        self.points.append(new)
        self.result.append(answer)

    def draw(self):
        colors = ["r", 'g', 'b', 'yellow', 'orange', "purple", "brown", (0, 0.8, 0.5)]
        for i in range(len(set(self.result))):
            sp = []
            values = list(set(self.result))
            for j in range(len(self.result)):
                if self.result[j] == values[i]:
                    sp.append(self.points[j])
            plt.plot([x[0] for x in sp], [x[1] for x in sp], "o", c=colors[i % len(colors)])
        plt.show()

    def start_draw(self):
        plt.plot([x[0] for x in self.points], [x[1] for x in self.points], 'o')
        plt.show()

x = Knn(result=list([random.randint(0, 3) for x in range(45)]), lenght=45, k=5)
x.fit((0.5, 0.5))
x.draw()