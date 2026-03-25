import psutil

import programmingtheiot.common.ConfigConst as ConfigConst


class BaseSystemUtilTask():
	"""
	Shell implementation representation of class for student implementation.
	
	"""
	
	def __init__(self, name = ConfigConst.NOT_SET, typeID = ConfigConst.DEFAULT_SENSOR_TYPE):
		self.name = name
		self.typeID = typeID
	
	def getName(self) -> str:
		return self.name
	
	def getTypeID(self) -> int:
		return self.typeID
	
	def getTelemetryValue(self) -> float:
		pass
	
class SystemCpuUtilTask(BaseSystemUtilTask):
	"""
	Class to return CPU performance data. 
	
	"""

	def __init__(self):
		super(SystemCpuUtilTask, self).__init__(name=ConfigConst.CPU_UTIL_NAME, typeID = ConfigConst.CPU_UTIL_TYPE)
	
	
	def getTelemetryValue(self) -> float:
		
		return psutil.cpu_percent()

class SystemMemUtilTask(BaseSystemUtilTask):
	"""
	Class to return Memory performance data. 
	
	"""

	def __init__(self):
		super(SystemMemUtilTask,self).__init__(name=ConfigConst.MEM_UTIL_NAME,typeID=ConfigConst.MEM_UTIL_TYPE)
	
	def getTelemetryValue(self) -> float:
		return psutil.virtual_memory().percent
				