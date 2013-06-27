#Basic sensor model - all sensors have to inherit this class
#Author - Mahesh C
#FISAT
#Jun 27/2013


import os
import sys



class BasicSensor(object):
	def __init__(self,name,stype,):
		self.name=name
		self.type=stype
		#output variable {'parameter_name':[measured_value,maximum,'unit']}
		self.output={}
	#Redefine this function according to your sensor and 
	#fill the variable
	def readValue(self)	
		pass




