#####
# 
# This class is part of the Programming the Internet of Things
# project, and is available via the MIT License, which can be
# found in the LICENSE file at the top level of this repository.
# 
# You may find it more helpful to your design to adjust the
# functionality, constants and interfaces (if there are any)
# provided within in order to meet the needs of your specific
# Programming the Internet of Things project.
# 

import logging
import random

import programmingtheiot.common.ConfigConst as ConfigConst

from programmingtheiot.data.SensorData import SensorData
from programmingtheiot.cda.sim.SensorDataGenerator import SensorDataSet

class BaseSensorSimTask():
	"""
	Shell representation of class for student implementation.
	
	"""

	DEFAULT_MIN_VAL = ConfigConst.DEFAULT_VAL
	DEFAULT_MAX_VAL = 1000.0
	
	def __init__(self, name = ConfigConst.NOT_SET, typeID: int = ConfigConst.DEFAULT_SENSOR_TYPE, dataSet = None, minVal: float = DEFAULT_MIN_VAL, maxVal: float = DEFAULT_MAX_VAL):
		self.name = name 
		self.typeID = typeID
		self.dataSet = dataSet
		self.dataSetIndex = 0
		self.lastestSensorData = None
		self.useRandomizer = False

		if not self.dataSet:
			self.useRandomizer = True
			self.minVal = minVal
			self.maxVal = maxVal

	def getName(self) -> str: 
		return self.name

	def getTypeID(self) -> int: 
		return self.typeID

	def generateTelemetry(self) -> SensorData:
		"""
		Implement basic logging and SensorData creation. Sensor-specific functionality
		should be implemented by sub-class.
		
		A local reference to SensorData can be contained in this base class.
		"""
		sensorData = SensorData(typeID= self.getTypeID(), name = self.getName())
		sensorVal = ConfigConst.DEFAULT_VAL

		if self.useRandomizer: 
			sensorVal = random.uniform(self.minVal,self.maxVal)
		else: 
			sensorVal = self.dataSet.getDataEntry(index = self.dataSetIndex)
			self.dataSetIndex = self.dataSetIndex + 1
			
			if self.dataSetIndex >= self.dataSet.getDataEntryCount() - 1: 
				self.dataSetIndex = 0
		
		sensorData.setValue(sensorVal)
		self.lastestSensorData = sensorData
		
		return self.lastestSensorData
	
	def getTelemetryValue(self) -> float:
		"""
		If a local reference to SensorData is not None, simply return its current value.
		If SensorData hasn't yet been created, call self.generateTelemetry(), then return
		its current value.
		"""
		if not self.lastestSensorData: 
			self.generateTelemetry()
		return self.lastestSensorData.getvaleu()
	
	def getLatestTelemetry(self) -> SensorData:
		"""
		This can return the current SensorData instance or a copy.
		"""
		if not self.lastestSensorData: 
			self.generateTelemetry()
		return self.lastestSensorData
	