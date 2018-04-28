import sys
try:
	from matplotlib import pyplot
except Exception as e:
	print('Module matplotlib not present! Graph will not be plotted')

class Convolution(object):
	"""docstring for Convolution"""
	
	def __init__(self):
		super(Convolution, self).__init__()
		self.input_function = []
		self.input_pos = -1
		self.impulse_response = []
		self.impulse_pos = -1
		self.convolution = []
		self.convolution_pos = -1

	def take_input(self):
		# All this should be taken as parameterized constructor
		print('Enter input function')
		self.input_function = [int(x) for x in input().split()]
		print('Enter the position of ordinate for input function')
		self.input_pos = int(input())

		print('Enter impulse response function')
		self.impulse_response = [int(x) for x in input().split()]
		print('Enter the position of ordinate for impulse response')
		self.impulse_pos = int(input())

	
	def calculate(self):
		self.convolution = [0] * ( len(self.input_function) 
			+ len(self.impulse_response) - 1 )

		for i in range(len(self.impulse_response)):
			temp = [x*self.impulse_response[i] for x in self.input_function]
			for j in range(len(temp)):
				self.convolution[i+j] += temp[j]

		self.convolution_pos = max(self.input_pos, self.impulse_pos)
				
	def print_convolution(self):
		print('The convolution is:')

		for i in self.convolution:
			print(i, end = ' ')
		print()

		for i in range(len(self.convolution)):
			if i == self.convolution_pos:
				print('^', end = ' ')
			else:
				print(end = '  ')
		print()

	def get_convolution(self):
		return self.convolution

	def plot(self):
		x_values = [int(x) - self.convolution_pos for x in range(len(self.convolution) + 1)]
		y_values = self.convolution
		y_values.append(0)

		pyplot.bar(x_values, y_values, width = 0.05)
		pyplot.axvline(0, color='red')
		pyplot.axhline(0, color = 'red')
		pyplot.title('Convolution')
		pyplot.xlabel('n')
		pyplot.ylabel('Y[n]')
		pyplot.show()


def main():
	convolution = Convolution()
	convolution.take_input()
	convolution.calculate()
	convolution.print_convolution()
	if 'matplotlib' in sys.modules:
		convolution.plot()

if __name__ == '__main__':
	main()