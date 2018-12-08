import sys
import matplotlib.pyplot as plt
import generate_random
def draw_random(method):
	if method == "1":
		seed = 1103515245
		random = generate_random.use_mid(seed,1000,5)
	elif method == "2":
		seed = 13
		A = 1103515245 
		C = 12345
		M = 2**31-1
		random = generate_random.use_linearcongruential(seed,A,C,M,1000)
	x=[]
	for i in range(1000):
		x.append(i+1)
	print(len(random))
	plt.plot(x,random)
	plt.title("Random Generate by LCG Method")
	plt.xlabel("Number")
	plt.ylabel('Value')
	plt.savefig("./ramdom.png")

def draw_idpt(method):
	idpt = []
	x = []
	for i in range(10,1001,1):
		if method == "1":
			seed = 1103515245
			random = generate_random.use_mid(seed,i,5)
		elif method == "2":
			seed = 13
			A = 1103515245 
			C = 12345
			M = 2**31-1
			random = generate_random.use_linearcongruential(seed,A,C,M,i)

		idpt.append(max(generate_random.get_independence(random)))
		x.append(i)
	print(idpt)
	print(x)
	plt.plot(x,idpt)
	plt.title("The Independence Departureness with N")
	plt.xlabel("N")
	plt.ylabel("Independence Departureness")
	plt.savefig("./Independence.png")

def draw_udpt(method):
	udpt = []
	x =[]
	for i in range(10,1001,1):
		if method == "1":
			seed = 1103515245
			random = generate_random.use_mid(seed,i,5)
		elif method == "2":
			seed = 13
			A = 1103515245 
			C = 12345
			M = 2**31-1
			random = generate_random.use_linearcongruential(seed,A,C,M,i)

		udpt.append(max(generate_random.get_uniformdepartureness(random)))
		x.append(i)
	plt.plot(x,udpt)
	plt.title("The Uniform Departureness with N")
	plt.xlabel("N")
	plt.ylabel("Uniform Departureness")
	plt.savefig("./Undependence.png")
	


def main():
	method = sys.argv[1]
#	draw_random(method)
#	draw_idpt(method)
	draw_udpt(method)


if __name__ == "__main__":
	main()
