"""
process.py

This class represents a process on an operating system. It can be in one of
three states: ready, running, or blocked.
"""

import Queue

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

		# Representation of tasks needed to execute this process
		self.job_queue = Queue.Queue()

		# Whenever a process completes a CPU burst, it performs an I/O operation.
		for burst in range(self.num_bursts - 1):
			self.job_queue.put('burst')
			self.job.queue.put('io')
		# However, we do not care about the last process' I/O operation.
		else:
			self.job_queue.put('burst')

		self.current_job = None

	# Overriding __cmp__ is necessary to implement SJF's PriorityQueue.
	def __cmp__(self, other):
		return cmp(self.cpu_burst_time, other.cpu_burst_time)

	def must_be_int(self, parameter, argument):
		if not self.string_is_int(argument):
			raise TypeError(parameter + ' \'' + argument + '\' must be an integer')

	def string_is_int(self, some_string):
		try:
			int(some_string)
			return True
		except ValueError:
			return False

	def has_terminated(self):
		return self.job_queue.empty()

	def set_current_job(self):
		self.current_job = self.job_queue.get()