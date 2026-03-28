import psutil
import time

import programmingtheiot.common.ConfigConst as ConfigConst
from programmingtheiot.common.ConfigConst import DEFAULT_SENSOR_TYPE, NOT_SET


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
				
class SystemDiskUtilTask(BaseSystemUtilTask):
    """
    Class to return the disk usage. 
    """
    def __init__(self):
        super(SystemDiskUtilTask,self).__init__(name=ConfigConst.DISK_UTIL_NAME,typeID=ConfigConst.DISK_UTIL_TYPE)
    
    def getTelemetryValue(self) -> float:
        return psutil.disk_usage("/").percent
    

class SystemNetInUtilTask(BaseSystemUtilTask):
    """
    Class to return the network usage.
    """
    def __init__(self):
        super(SystemNetInUtilTask,self).__init__(name=ConfigConst.NET_IN_UTIL_NAME, typeID=ConfigConst.NET_IN_UTIL_TYPE)

    def getTelemetryValue(self) -> float:
		# Inital network stats 
        interval = 1
        stats_before = psutil.net_io_counters()
        bytes_recv_before = stats_before.bytes_recv
        
        time.sleep(interval)
        
        # Post interval stats. 
        stats_after = psutil.net_io_counters()
        bytes_recv_after = stats_after.bytes_recv
        
        return (bytes_recv_after - bytes_recv_before) / interval

class SystemNetOutUtilTask(BaseSystemUtilTask):
    """
    Class to return the network usage.
    """
    def __init__(self):
        super(SystemNetOutUtilTask,self).__init__(name=ConfigConst.NET_OUT_UTIL_NAME, typeID=ConfigConst.NET_OUT_UTIL_TYPE)

    def getTelemetryValue(self) -> float:
        interval = 1
		# Inital network stats 
        stats_before = psutil.net_io_counters()
        bytes_sent_before = stats_before.bytes_sent
        
        time.sleep(interval)
        
        # Post interval stats. 
        stats_after = psutil.net_io_counters()
        bytes_sent_after = stats_after.bytes_sent
        
        return (bytes_sent_after - bytes_sent_before) / interval