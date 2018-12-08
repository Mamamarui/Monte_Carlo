import matplotlib.pyplot as plt
import random
x=[]
y=[]
for i in range(1000):
    xi_i = random.random()
    x.append(i+1)
    y.append(xi_i)

print(y)
plt.plot(x,y)
plt.show()


