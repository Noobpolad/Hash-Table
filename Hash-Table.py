import csv

class Visitor():

	def __init__(self, name, ID, counter=0):
		self._name = name
		self._ID = ID
		self._counter = counter
		self._nextData = None

	def getTheName(self):
		return self._name

	def setTheName(self, name):
		self._name = name

	def getTheCounter(self):
		return self._counter

	def setTheCounter(self, number):
		self._counter = number

	def getTheID(self):
		return self._ID

	def setTheID(self, ID):
		self._ID = ID	

	def getTheNextData(self):
		return self._nextData

	def setTheNextData(self, data):
		self._nextData = data	

class HashTable:

	def __init__(self):
		self._array = [None] * 10
		self._editingArray = [None] * 10

	def insertTheData(self, arr, data):
		if arr[self.function(data.getTheID(),len(arr))] != None:
			cur = arr[self.function(data.getTheID(),len(arr))]
			while 1:
				if cur.getTheNextData() == None:
					cur.setTheNextData(data)
					break	
				cur = cur.getTheNextData()	
		else: 
			arr[self.function(data.getTheID(),len(arr))] = data	

	def display(self):
		for a in range(0,len(self._array)):
			cur = self._array[a]
			while cur != None:
				print(cur.getTheName(),cur.getTheID(),cur.getTheCounter(),"At possition:",a + 1)
				cur = cur.getTheNextData()		

	def function(self, ID, parametr):	
		key = (int(ord(ID[0])) + int(ord(ID[1])) + int(ID[2]) + int(ID[3]) + int(ID[4]) + int(ID[5])) % int(parametr)	
		return int(key)		

	def deleteAll(self,arr):
		for a in range(0,len(arr)):
			arr[a] = None 

	#The method to chech if we have a collision, thus if in one row there is more than 2 records solve the collision		

	def isCorrect(self):
		for a in range(0,len(self._array)):
			counter = 0
			cur = self._array[a]
			while cur != None:
				counter += 1
				if counter > 2:
					return False
				cur = cur.getTheNextData()
		return True				

	def collisionSolving(self):
		while self.isCorrect() == False:
			self._array.append(None)
			self._editingArray.append(None)
			for a in range(0,len(self._array)):
				cur = self._array[a]
				while cur != None:
					tmp = Visitor(cur.getTheName(),cur.getTheID(),cur.getTheCounter())
					self.insertTheData(self._editingArray,tmp)
					cur = cur.getTheNextData()
			self.deleteAll(self._array)	
			for a in range(0,len(self._editingArray)):
				cur = self._editingArray[a]
				while cur != None:
					tmp = Visitor(cur.getTheName(),cur.getTheID(),cur.getTheCounter())
					self.insertTheData(self._array,tmp)
					cur = cur.getTheNextData()
			self.deleteAll(self._editingArray)		

	def increaseTheCounter(self,ID):
		for pos in range(0,len(self._array)):
			cur = self._array[pos]
			while cur != None:
				if cur.getTheID() == ID:
					cur.setTheCounter(str(int(cur.getTheCounter()) + 1))
					return
				cur = cur.getTheNextData()	
		
	def operation(self):	
		file = open('Visitors.csv')
		reader = csv.reader(file)
		for row in reader:
			self.insertTheData(self._array,Visitor(row[0],row[1],row[2]))
			self.collisionSolving()
		newFile = open('Visitors.csv','w',newline = '')
		writer = csv.writer(newFile)
		ID = input("Insert the ID: ")
		exist = False
		for pos in range(0,len(ht._array)):
			cur = self._array[pos]
			while cur != None:
				if ID == cur.getTheID():
					self.increaseTheCounter(ID)
					print("Visitor's counter with ID:" + ID + " has been increased, thank you for using.")
					exist = True
				writer.writerow((cur.getTheName(),cur.getTheID(),cur.getTheCounter()))
				cur = cur.getTheNextData()
		if exist == False:
			print("Im sorry, the person with ID:" + ID + " is not existing.")	

ht = HashTable()				
ht.operation()