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

import programmingtheiot.common.ConfigConst as ConfigConst

from programmingtheiot.data.BaseIotData import BaseIotData

class SystemPerformanceData(BaseIotData):
	"""
	Shell representation of class for student implementation.
	
	"""
	DEFAULT_VAL = 0.0
	
	def __init__(self, d = None):
		super(SystemPerformanceData, self).__init__(name = ConfigConst.SYSTEM_PERF_MSG, typeID = ConfigConst.SYSTEM_PERF_TYPE, d = d)
		
		self.cpuUtil    = ConfigConst.DEFAULT_VAL
		self.memUtil    = ConfigConst.DEFAULT_VAL
		self.diskUtil   = ConfigConst.DEFAULT_VAL
		self.netInUtil  = ConfigConst.DEFAULT_VAL
		self.netOutUtil = ConfigConst.DEFAULT_VAL
	
	def getCpuUtilization(self):
		return self.cpuUtil
	
	def getDiskUtilization(self):
		return self.diskUtil
	
	def getMemoryUtilization(self):
		return self.memUtil
	
	def getNetInUtilization(self):
		return self.netInUtil

	def getNetOutUtilization(self):
		return self.netOutUtil
	
	def setCpuUtilization(self, cpuUtil):
		self.updateTimeStamp()
		self.cpuUtil = cpuUtil
	
	def setDiskUtilization(self, diskUtil):
		self.updateTimeStamp()
		self.diskUtil = diskUtil
	
	def setMemoryUtilization(self, memUtil):
		self.updateTimeStamp()
		self.memUtil = memUtil
	
	def setNetInUtilTask(self, netInUtil):
		self.updateTimeStamp()
		self.netInUtil = netInUtil

	def setNetOutUtilTask(self,netOutUtil):
		self.updateTimeStamp()
		self.netOutUtil = netOutUtil
	
	def _handleUpdateData(self, data):
		if data and isinstance(data, SystemPerformanceData):
			self.cpuUtil     = data.getCpuUtilization()
			self.diskUtil    = data.getDiskUtilization()
			self.memUtil     = data.getMemUtilization()
			self.netInUtil   = data.getNetInUtilization()
			self.netOutUtil  = data.getNetOutUtilization()

	def __str__(self):
		return "System Performance Data:\n\n \
		{}={}\n{}={}\n{}={}\n{}={}\n{}={}\n" \
		.format("CPU Utilization",self.cpuUtil \
				,"Disk Utilization",self.diskUtil \
        		,"Memory Utilization",self.memUtil \
				,"NetOut Utilization",self.netOutUtil\
                ,"NetIn Utilization",self.netInUtil)