#!/usr/bin/env python
# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt
import random


class Kmeans():
    # Класс принимает список кортежей из координат (x, y), их длину и количество кластеров, на которые надо разбить
    def __init__(self, points=None, lenght=40, clasters_amount=3):
        if points == None:
            self.points = [(random.random(), random.random()) for x in range(lenght)]
            self.lenght = lenght
        else:
            self.points = points
            self.lenght = len(self.points)
        self.clasters_amount = clasters_amount
        
        self.centers = [(0, 0)] * clasters_amount
        self.set_centers()
        
        self.result = [1] * self.lenght
        self.find_the_nearest()
        
        self.draw()
        
    # Метод устанавливает начальные значения для центров кластеров
    def set_centers(self):
        a = [random.randint(0, self.lenght - 1) for x in range(self.clasters_amount)]
        while len(set(a)) != self.clasters_amount:
            a = [random.randint(0, self.lenght - 1) for x in range(self.clasters_amount)]
        
        for i in range(self.clasters_amount):
            self.centers[i] = self.points[a[i]]
            
            
    def get_centers(self):
        return self.centers
    
    # Метод устанавливает для каждой точки принадлежность к определённому кластеру (отображено в self.result)        
    def find_the_nearest(self):
        for i in range(len(self.result)):
            distance_to_centers = [0] * self.clasters_amount
            for j in range(self.clasters_amount):
                a = ((self.getPointsX()[i] - self.centers[j][0]) ** 2 + (self.getPointsY()[i] - self.centers[j][1]) ** 2) ** 0.5
                distance_to_centers[j] = a
            z = distance_to_centers.index(min(distance_to_centers))
            self.result[i] = z
            
    
    def get_result(self):
        return self.result
    
    # Рисует исходные точки, не распределённые на кластеры        
    def start_draw(self):
        plt.plot([x[0] for x in self.points], [x[1] for x in self.points], 'o')
        plt.show()
        
    
    def getPoints(self):
        return self.points
    
    
    def getPointsX(self):        
        return [x[0] for x in self.points]
    
    
    def getPointsY(self):
        return [x[1] for x in self.points]
    
    # Рисует кластеры из точек
    def draw(self):
        colors = ["r", 'g', 'b', 'yellow', 'orange', "purple", "brown", (0,0.8,0.5)] 
        for i in range(self.clasters_amount):
            sp = []
            for j in range(len(self.result)):
                if self.result[j] == i:
                    sp.append(self.points[j])
            plt.plot([x[0] for x in sp], [x[1] for x in sp], "o" , c=colors[i % len(colors)])
        plt.show()
        
    # Меняет центры кластеров    
    def change_centers(self):
        for i in range(self.clasters_amount):
            sp = []
            for j in range(len(self.result)):
                if self.result[j] == i:
                    sp.append(self.points[j])
            x = [x[0] for x in sp]
            y = [x[1] for x in sp]
            self.centers[i] = (sum(x) / len(x), sum(y) / len(y))
            
    # Метод, который делает пошагово весь алгоритм        
    def do_everything(self):
        previous = self.result[:]
        self.change_centers()
        self.find_the_nearest()
        self.draw()
        while self.result != previous:
            previous = self.result[:]
            self.change_centers()
            self.find_the_nearest()
            self.draw()
    
    # Метод, который выводит решение задачи кластеризации
    def do_result(self):
        previous = self.result[:]
        self.change_centers()
        self.find_the_nearest()
        self.draw()
        while self.result != previous:
            previous = self.result[:]
            self.change_centers()
            self.find_the_nearest()
        self.draw()


x = Kmeans(lenght=80, clasters_amount=4)
x.do_result()