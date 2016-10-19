"""
process.py

This class represents a process on an operating system. It can be in one of
three states: ready, running, or blocked.
"""

class Process(object):
	def __init__(self, pid, arrival_time, burst_time, burst_num, time_io):
		if not (type(pid) is str and len(pid) == 1 and pid.isupper()):
			raise TypeError('proc_id \'' + pid + '\' must be a capital letter')
		self.must_be_int('initial_arrival_time', arrival_time)
		self.must_be_int('cpu_burst_time', burst_time)
		self.must_be_int('num_bursts', burst_num)
		self.must_be_int('io_time', time_io)

		# Input file variables
		self.proc_id = pid;
		self.initial_arrival_time = int(arrival_time)
		self.cpu_burst_time = int(burst_time)
		self.num_bursts = int(burst_num)
		self.io_time = int(time_io)

		# Output file variables
		self.wait_time = 0
		self.turnaround_time = 0

	def must_be_int(self, parameter, argument):
		if not self.string_is_int(argument):
			raise TypeError(parameter + ' \'' + argument + '\' must be an integer')

	def string_is_int(self, some_string):
		try:
			int(some_string)
			return True
		except ValueError:
			return False