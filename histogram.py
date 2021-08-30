#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import os
import re
import sys

def histogram(data, gryffindor, hufflepuff, ravenclaw, slytherin):
	i = 10
	plt.hist(gryffindor[:, i], label = "Grynffindor", color = "red", alpha = 0.5)
	plt.hist(hufflepuff[:, i], label = "Hufflepuff", color = "yellow", alpha = 0.5)
	plt.hist(ravenclaw[:, i], label = "Ravenclaw", color = "blue", alpha = 0.5)
	plt.hist(slytherin[:, i], label = "Slytherin", color = "green", alpha = 0.5)
	plt.legend(loc = "upper right", frameon = False)
	plt.title(data[0, i])
	plt.xlabel("Grades")
	plt.ylabel("Number of student")
	plt.show()

def delCoLette(data, i):
	for j in range(1, len(data)):
		if data[j, i] != str(np.nan) and re.search("^[+-]?([0-9]+[.])?[0-9]+$", data[j, i]) == None:
			return [np.delete(data, i, 1), i]
	return [data, i + 1]

def removeLetter(house):
	house = np.delete(house, 0, 1)
	i = 0
	while i < len(house[0]):
		[house, i] = delCoLette(house, i)
	return house

def parseHouse(data):
	data[data == ''] = np.nan
	gryffindor = data[np.where(data[:, 1] == "Gryffindor")]
	hufflepuff = data[np.where(data[:, 1] == "Hufflepuff")]
	ravenclaw = data[np.where(data[:, 1] == "Ravenclaw")]
	slytherin = data[np.where(data[:, 1] == "Slytherin")]
	data = removeLetter(data)
	gryffindor = removeLetter(gryffindor)
	hufflepuff = removeLetter(hufflepuff)
	ravenclaw = removeLetter(ravenclaw)
	slytherin = removeLetter(slytherin)
	gryffindor = gryffindor.astype(float)
	hufflepuff = hufflepuff.astype(float)
	ravenclaw = ravenclaw.astype(float)
	slytherin = slytherin.astype(float)
	return [data, gryffindor, hufflepuff, ravenclaw, slytherin]

if __name__ == "__main__":
	try:
		if os.stat("datasets/dataset_train.csv").st_size > 0:
			data = np.loadtxt("datasets/dataset_train.csv", dtype = str, delimiter = ",")
		else:
			sys.exit("Error")
	except:
		sys.exit("Error")
	[data, gryffindor, hufflepuff, ravenclaw, slytherin] = parseHouse(data)
	histogram(data, gryffindor, hufflepuff, ravenclaw, slytherin)
