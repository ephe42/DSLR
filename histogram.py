#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import os
import re
import sys

def histogram(data, gryffindor, hufflepuff, ravenclaw, slytherin):
	for i in range(len(data[0])):
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
	gryffindor = np.zeros([0, len(data[0])])
	hufflepuff = np.zeros([0, len(data[0])])
	ravenclaw = np.zeros([0, len(data[0])])
	slytherin = np.zeros([0, len(data[0])])
	for i in range(len(data)):
		if data[i, 1] == "Gryffindor":
			gryffindor = np.append(gryffindor, np.array([data[i, :]]), axis=0)
		elif data[i, 1] == "Hufflepuff":
			hufflepuff = np.append(hufflepuff, np.array([data[i, :]]), axis=0)
		elif data[i, 1] == "Ravenclaw":
			ravenclaw = np.append(ravenclaw, np.array([data[i, :]]), axis=0)
		elif data[i, 1] == "Slytherin":
			slytherin = np.append(slytherin, np.array([data[i, :]]), axis=0)
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

def checkError():
	try:
		if len(sys.argv) == 2 and os.path.isfile(sys.argv[1]) and os.stat(sys.argv[1]).st_size > 0:
			data = np.loadtxt(sys.argv[1], dtype = str, delimiter = ",")
			if (len(data[:, 0]) >= 2):
				return data
	except:
		pass
	print("Error")
	exit(1)

if __name__ == "__main__":
	data = checkError()
	[data, gryffindor, hufflepuff, ravenclaw, slytherin] = parseHouse(data)
	histogram(data, gryffindor, hufflepuff, ravenclaw, slytherin)
