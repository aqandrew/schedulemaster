"""
job.py

This class represents an operation performed by a process using the CPU.
"""

class Job(object):
	def __init__(self, type_job, time_remaining):
		self.job_type = type_job
		self.remaining_time = time_remaining