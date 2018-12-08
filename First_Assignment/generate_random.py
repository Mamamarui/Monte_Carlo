import time
import sys
import copy

class mid_type():
	def __init__(self,number,seed,s):
		self.num_random = number
		self.seed = seed
		self.s = s
		self.method = "mid"

class lingearcongruential_type():
	def __init__(self,number,seed,A,C,M):
		self.num_random = number
		self.seed = seed
		self.A = A
		self.C = C
		self.M = M
		self.method = "lingearcongruential"

def read_input(path_input):
	'''
		read the input file get the info.
	'''
	with open(path_input,"r") as f_inp:
		templines = f_inp.readlines()
	
	mid_log = False
	linear_log = False
	for index,item in enumerate(templines):
		if "method" in item:
			mode = item.split()[1]
			if mode == "1":
				mid_log = True
			elif mode == "2":
				linear_log = True
			continue
		if "number" in item:
			num_random = int(item.split()[1])
			continue
		if "seed" in item:
			seed = item.split()[1]
			continue
		if mid_log and "s" in item:
			s = int(item.split()[1])
			continue
		if linear_log and "A" in item:
			A = int(item.split()[1])
			continue
		if linear_log and "C" in item:
			C = int(item.split()[1])
			continue
		if linear_log and "M" in item:
			M = int(item.split()[1])
	if mode == "1":
		input_info = mid_type(num_random,seed,s)
	if mode == "2":
		input_info = lingearcongruential_type(num_random,seed,A,C,M)
	return input_info

def get_seed(len_random):
	'''
		get the seed from the clock time.
	'''
	seed = int((time.time()*10**(len_random))%10**(len_random))
	return seed

def use_mid(seed,num,s):
	'''
		the mid method to get the random num.
	'''
	print(" Using mid method.")
	print()
	random_list = [] 
	x_list = []
	x_list.append(seed)
	random_list.append(seed/10**(s*2))
	print("         1  epsilon%10d : %.15f " %(1,random_list[0]))
	x1 = int(seed**2*10**(-s))%(10**(s*2))
	x_list.append(x1)
	random_list.append(x1/10**(s*2))
	print("         2  epsilon%10d : %.15f" %(2,random_list[1]))
	for i in range(num-2):
		xi = int(x_list[i]*x_list[i+1]*10**(-s))%(10**(s*2))
		x_list.append(xi)
		random_list.append(xi/10**(2*s))
		print("%10d  epsilon%10d : %.15f" %(i+3,i+3,random_list[i+2]))
	print()
	return random_list

def use_linearcongruential(seed,A,C,M,num):
	'''
		the Linear congruential method to get the random num.
	'''
	print(" Linear congruential method.")
	print()
	random_list = []
	x_list = []
	x0 = (A*seed+C)%M
	x_list.append(x0)
	random_list.append(x0/M)
	print("         1  epsilon%d : %.15f " %(1,random_list[0]))
	for i in range(num-1):
		xi = (x_list[i]*A + C)%M
		x_list.append(xi)
		random_list.append(xi/M)
		print("%10d  epsilon%10d : %.15f" %(i+2,i+2,random_list[i+1]))
	print()
	return random_list

def get_uniformdepartureness(random):
	random_list = copy.deepcopy(random)
	random_list.sort()
	delta_n =[]
	for i in range(len(random_list)):
		if i == 0 :
			delta_n.append(max(abs(0-i/len(random_list)),abs(random_list[i]-(i+1)/len(random_list))))
		elif i == len(random_list)-1:
			delta_n.append(max(abs(random_list[i]-(i+1)/len(random_list)),abs(1-(i+2)/len(random_list))))
		else:
			delta_n.append(max(abs(random_list[i]-(i+1)/len(random_list)),abs(random_list[i+1]-(i+2)/len(random_list))))
	print(" Uniform departureness : %f " %max(delta_n))
	return delta_n

def get_independence(random):
	random_list1 = []
	random_list2 = []
	for i in range(len(random)):
		if i % 2 == 0:
			random_list2.append(random[i])
		else:
			random_list1.append(random[i])
	if len(random_list1) != len(random_list2):
		random_list2.append(1)

	epsilon_n = []
	N = len(random_list1)
	for i in range(N):
		x = random_list1[i]
		y = random_list2[i]
		nx = ny = nnxy = 0
		for index_x in range(N):
			if random_list1[index_x]<x:
				nx += 1
			if random_list1[index_x]<x and random_list2[index_x]<y:
				nnxy += 1
			if random_list2[index_x]<y:
				ny += 1
		epsilon_n.append(abs(nnxy/N-(nx/N)*(ny/N)))
	
	print(" Independence departureness : %f " %max(epsilon_n))
	return epsilon_n

def print_random(random,udpt,idpt):
	'''
		write the final result in the file named out.
	'''
	with open("out","w+") as f_out:
		f_out.write("Random list : \n")
		for i in range(len(random)):
			f_out.write(" %d %.15f\n" %(i+1,random[i]))
		f_out.write(" Uniform departureness : %f.\n" %max(udpt))
		f_out.write(" Independence departureness : %f.\n" %max(idpt))

def main():
	starttime = time.time()
	input_info = read_input(sys.argv[1])

	print()
	print("==================== start generate the random number =====================")
	if input_info.method == "mid":
		if input_info.seed == "random":
			seed = get_seed(input_info.s*2)
		else:
			seed = int(input_info.seed)
		random = use_mid(seed,input_info.num_random,input_info.s)
	elif input_info.method == "lingearcongruential":
		if input_info.seed == "random":
			seed = get_seed(4)
		else:
			seed = int(input_info.seed)
		random = use_linearcongruential(seed,input_info.A,input_info.C,input_info.M,input_info.num_random)
	udpt=get_uniformdepartureness(random)
	idpt=get_independence(random)
	print_random(random,udpt,idpt)
	print("==================== finish generate the random number ====================")
	endtime = time.time()
	print(" Calculation Time : %.3f s." %(endtime-starttime))
	print()


if __name__ == "__main__":
	main()

