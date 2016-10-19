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
		self.reset(input_file)

	def reset(self, input_file):
		self.t = 0 # Elapsed time in milliseconds
		self.num_context_switches = 0
		self.num_preemptions = 0
		self.read_input(input_file) # Erase output statistics

	"""
	Any line beginning with a # character is ignored
		(these lines are comments).
	All blank lines are also ignored, including lines containing
		only whitespace characters.
	If an error in the input file format is detected,
		display an error message (handled in process.py).
	"""
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
		queue_representation = '[Q '

		if self.ready_queue.queue:
			queue_representation += repr(list(self.ready_queue.queue))[1:-1].split(',').join()
		else:
			queue_representation += 'empty'
		
		return queue_representation + ']'

	def simulate(self, algorithm):
		if algorithm == 'SJF':
			self.ready_queue = Queue.PriorityQueue()
		else:
			self.ready_queue = Queue.Queue()

		print 'time ' + repr(self.t) + 'ms: Simulator started for ' + algorithm + ' ' + self.show_queue() 

		# TODO Set up some kind of while-loop here.
		# TODO Print whenever a process arrives to the CPU.
		# TODO Add processes from self.process_list to ready_queue based on algorithm.
		# TODO Measure turnaround time for each simulated process.
		#			   == arrival time ... CPU burst completed, including context switches
		# TODO Measure wait time for each simulated process.
		#			   == time spent in ready queue, excluding context switches
		# TODO Print whenever a process starts using the CPU.
		#	Note that this is t_cs / 2 if no process is currently using the CPU.
		# TODO Print whenever a process finishes using the CPU, i.e. completes its CPU burst.
		# TODO Print whenever a process is preempted.
		# TODO Print whenever a process starts performing I/O.
		# TODO Print whenever a process finishes performing I/O.
		# TODO Print whenever a process terminates (by finishing its last CPU burst).

		# TODO When all processes terminate, the simulation ends.
		if self.process_list:
			self.t += ScheduleMaster.t_cs / 2
			
		print 'time ' + repr(self.t) + 'ms: Simulator ended for ' + algorithm

		if algorithm != 'RR':
			print ''

	def write_output(self, output_file, algorithm):
		with open(output_file, 'a') as output:
			output.write('Algorithm ' + algorithm + '\n')

			# Print average CPU burst time, calculated from the input data.
			burst_times = [process.cpu_burst_time for process in self.process_list for burst_num in range(process.num_bursts)]
			average_burst_time = '%.2f' % (sum(burst_times) / float(len(burst_times)))
			output.write('-- average CPU burst time: ' + average_burst_time + ' ms\n')

			# Print average wait time.
			wait_times = [process.wait_time for process in self.process_list]
			average_wait_time = '%.2f' % (sum(wait_times) / float(len(wait_times)))
			output.write('-- average wait time: ' + average_wait_time + ' ms\n')

			# Print average turnaround time.
			turnaround_times = [process.turnaround_time for process in self.process_list]
			average_turnaround_time = '%.2f' % (sum(turnaround_times) / float(len(turnaround_times)))
			output.write('-- average turnaround time: ' + average_turnaround_time + ' ms\n')

			output.write('-- total number of context switches: ' + repr(self.num_context_switches) + '\n')
			output.write('-- total number of preemptions: ' + repr(self.num_preemptions) + '\n')


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
		sm.reset(input_file)


if __name__ == "__main__":
	main()