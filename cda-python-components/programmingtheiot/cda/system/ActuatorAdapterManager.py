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

from importlib import import_module

import programmingtheiot.common.ConfigConst as ConfigConst
from programmingtheiot.common.ConfigUtil import ConfigUtil
from programmingtheiot.common.IDataMessageListener import IDataMessageListener

from programmingtheiot.data.ActuatorData import ActuatorData

from programmingtheiot.cda.sim.HvacActuatorSimTask import HvacActuatorSimTask
from programmingtheiot.cda.sim.HumidifierActuatorSimTask import HumidifierActuatorSimTask

class ActuatorAdapterManager(object):
	"""
	Shell representation of class for student implementation.
	
	"""
	
	def __init__(self, dataMsgListener: IDataMessageListener = None):
		self.dataMsgListener = dataMsgListener

		self.configUtil = ConfigUtil()

		self.useSimulator = self.configUtil.getBoolean( \
			section = ConfigConst.CONSTRAINED_DEVICE, key=ConfigConst.ENABLE_SIMULATOR_KEY)
		self.useEmulator = self.configUtil.getBoolean( \
			section = ConfigConst.CONSTRAINED_DEVICE, key = ConfigConst.ENABLE_EMULATOR_KEY)
		self.deviceID = self.configUtil.getProperty(\
			section = ConfigConst.CONSTRAINED_DEVICE, key = ConfigConst.DEVICE_LOCATION_ID_KEY,  defaultVal= ConfigConst.NOT_SET)
		self.locationID = self.configUtil.getProperty(\
			section = ConfigConst.CONSTRAINED_DEVICE, key=ConfigConst.DEVICE_LOCATION_ID_KEY, defaultVal= ConfigConst.NOT_SET)

		self.humidifierActuator = None 
		self.hvacActuator = None 
		self.ledDisplayActuator = None

		self._initEnvironmentalActuationTasks()

	def sendActuatorCommand(self, data: ActuatorData) -> bool:
		if data and not data.isResponseFlagEnabled():
			if data.getLocationID() == self.locationID: 
				logging.info(f"Actuator command received for location ID {str(data.getLocationID)}. Processing...")

				aType = data.getTypeID()
				responseData = None

				#TODO: implement appropriate logging and error handling
				if aType == ConfigConst.HUMIDIFIER_ACTUATOR_TYPE and self.humidifierActuator: 
					responseData = self.humidifierActuator.updateActuator(data)
				elif aType == ConfigConst.HVAC_ACTUATOR_TYPE and self.hvacActuator: 
					responseData = self.hvacActuator.updateActuator(data)
				elif aType == ConfigConst.LED_DISPLAY_ACTUATOR_TYPE and self.ledDisplayActuator: 
					responseData = self.ledDisplayActuator.update(data)
				else: 
					logging.warning(f"No valid actuator type. Ignoring actuation for type: {data.getTypeID()}")
				#TODO: in a later module, the responseData instance will be passed to a callback funciton implemented in DeviceDataManger via IDataMessageListener

				return responseData
			else: 
				logging.warning(f"Location ID doesn't match. Ignoring acutation (me) {str(self.locationID)} != (you) {str(data.getLocationID())}")
		else: 
			logging.warning(f"Actuator request received. Message is empty or resonse. Ignoring.")
		return None
	def setDataMessageListener(self, listener: IDataMessageListener) -> bool:
		if listener: 
			self.dataMsgListener = listener

	def _initEnvironmentalActuationTasks(self):
		if not self.useEmulator: 
			self.humidifierActuator = HumidifierActuatorSimTask()

			self.hvacActuator = HvacActuatorSimTask()
