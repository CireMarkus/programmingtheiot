#####
# 
# This class is part of the Programming the Internet of Things
# project, and is available via the MIT License, which can be
# found in the LICENSE file at the top level of this repository.
# 
# Copyright (c) 2020 by Andrew D. King
# 

import logging
import unittest

from programmingtheiot.cda.system.SystemUtilTasks import SystemNetInUtilTask

class SystemNetInUtilTaskTest(unittest.TestCase):
	"""
	This test case class contains very basic unit tests for
	SystemCpuUtilTask. It should not be considered complete,
	but serve as a starting point for the student implementing
	additional functionality within their Programming the IoT
	environment.
	"""
	
	@classmethod
	def setUpClass(self):
		logging.basicConfig(format = '%(asctime)s:%(module)s:%(levelname)s:%(message)s', level = logging.DEBUG)
		logging.info("Testing SystemNetInUtilTask class...")
		self.netInUtilTask = SystemNetInUtilTask()
	def setUp(self):
		pass

	def tearDown(self):
		pass

	def testGetTelemetryValue(self):
		val = self.netInUtilTask.getTelemetryValue()
		
		self.assertGreaterEqual(val, 0.0)
		logging.info("Net in utilization: %s bytes.", str(val))

if __name__ == "__main__":
	unittest.main()
	