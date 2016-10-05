"""
schedulemaster.py

CSCI-4210 Operating Systems F16

This rudimentary simulation of an operating system is a process simulation
model in Python to compare efficiency between first-come first-served,
shortest job first, and round robin process scheduling algorithms.
"""

import sys
import os
import Queue
from process import Process

class ScheduleMaster(object):
	n = 0 # Number of processes to simulate, determined by input file
	m = 1 # Number of processors (i.e. cores) available within the CPU
	t_cs = 8 # Time in ms it takes to perform a context switch
	t_slice = 84 # Time in ms each process is given to complete its
				 # 	CPU burst in round robin

	def __init__(self, input_file):
		self.t = 0 # Elapsed time in milliseconds
		self.read_input(input_file)

	# Any line beginning with a # character is ignored
	#	(these lines are comments).
	# All blank lines are also ignored, including lines containing
	#	only whitespace characters.
	# If an error in the input file format is detected,
	#	display an error message.
	def valid_line(self, line):
		return (not line.isspace()) and line[0] != '#'

	def read_input(self, input_file):
		with open(input_file, 'r') as input_data:
			process_strings = [line.strip() for line in input_data if self.valid_line(line)]
			self.process_list = []

			try:
				for process_string in process_strings:
					process_params = process_string.split('|')
					self.process_list.append(Process(*process_params))
			except TypeError as err:
				print 'Invalid input file format:'
				print '\t', err
				sys.exit(1)

			n = len(self.process_list)

	def show_queue(self):
		return repr(list(self.ready_queue.queue))

	def simulate(self, algorithm):
		self.ready_queue = Queue.Queue()
		print 'time ' + repr(self.t) + 'ms: Simulation started for ' + algorithm + ' [Q ' + self.show_queue() + ']' 
		# TODO Add processes from self.process_list to ready_queue based on algorithm.

		# TODO Set up some kind of while-loop here.
		# TODO Measure CPU burst time for each simulated process.
		# TODO Measure turnaround time for each simulated process.
		#			   == arrival time ... CPU burst completed, including context switches
		# TODO Measure wait time for each simulated process.
		#			   == time spent in ready queue, excluding context switches
		# TODO Print whenever a process starts using the CPU.
		# TODO Print whenever a process finishes using the CPU, i.e. completes its CPU burst.
		# TODO Print whenever a process is preempted.
		# TODO Print whenever a process starts performing I/O.
		# TODO Print whenever a process finishes performing I/O.
		# TODO Print whenever a process terminates (by finishing its last CPU burst).

		# TODO When all processes terminate, the simulation ends.
		print 'time ' + repr(self.t) + 'ms: Simulation ended for ' + algorithm

	def reset(self):
		self.t = 0

	def write_output(self, output_file, algorithm):
		with open(output_file, 'a') as output:
			output.write('Algorithm ' + algorithm + '\n')
			# TODO Print average CPU burst time.
			# TODO Print average wait time.
			# TODO Print average turnaround time.
			# TODO Print total number of context switches.
			# TODO Print total number of preemptions.


def main():
	# Check command line arguments.
	if len(sys.argv) != 3:
		print 'ERROR: Invalid arguments'
		print 'USAGE: ./a.out <input-file> <stats-output-file>'
		sys.exit(2)

	input_file = sys.argv[1]
	output_file = sys.argv[2]

	if os.path.isfile(output_file):
		os.remove(output_file)

	sm = ScheduleMaster(input_file)
	algorithms = ['FCFS', 'SJF', 'RR']

	for algorithm in algorithms:
		sm.simulate(algorithm)
		sm.write_output(output_file, algorithm)
		sm.reset()


if __name__ == "__main__":
	main()