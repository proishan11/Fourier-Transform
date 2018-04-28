from math import pi, e
from matplotlib import pyplot


class DFT:
	def __init__(self):
		self.size_of_input = 0
		self.input_signal = []
		self.transform = []
		self.dftmatrix = []
		self.omega = 0

	def draw_ray(self, a, b):
		x = [b, b]
		y = [0, a]
		pyplot.plot(x, y, marker='o')




	def draw_graph(self, signal, xl, yl, heading):
		minv = min([abs(i) for i in signal])
		maxv = max([abs[i] for i in signal])
		plt.axhline(0, color = 'black')
		pyplot.axis([-1, self.size_of_input+2, -5, int(maxv)+2])

		pyplot.title(heading)
		pyplot.xlabel(xlab)
		pyplot.ylabel(ylab)


		for i in range(len(signal)):
			drawLine(abs(signal[i]), i)
		plt.show()

	def draw_input(self):	
		drawGraph(self.input_signal,'n--->', 'x[n]--->', 'Input Signal', self.size_of_inputs)
	
	def draw_transform(self):
		drawGraph(self.transform,'n--->','X[n]--->','Fourier Transform', self.size_of_input)

	def draw_all(self):
		self.draw_input()
		#self.draw_transform()



	def get_input(self):
		print("Enter the size of input signal")
		self.size_of_input = int(input())
		print("Enter the signal")
		for i in range(self.size_of_input):
			x,y = (int(x) for x in input().split())

			self.input_signal.extend([complex(x,y)])
		self.omega = e**complex(0, -2*pi/self.size_of_input)
		print(self.input_signal)

	def fill_dftmatrix(self):
		for i in range(self.size_of_input):
			temp = [self.omega**(i*j) for j in range(self.size_of_input)]
			self.dftmatrix.append(temp)

	def compute_DFT(self):
		#self.omega = 
		self.fill_dftmatrix()
		for i in range(self.size_of_input):
			temp_sum = 0
			for j in range(self.size_of_input):
				temp_sum += self.dftmatrix[i][j] * self.input_signal[j]
			self.transform.extend([temp_sum])
		print(self.transform)

def main():
	a = DFT()
	a.get_input()
	a.compute_DFT()
	a.draw_all()
	

if __name__ == '__main__':
	main()

