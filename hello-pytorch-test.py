"""
Created on Tue Sep  6 09:25:39 2022

@author: Richter
"""
import sys

print("> Welcome to the Python installation test script 2!")

print("> Let's check the package pytorch ...")


try:
	import torch
	print("The module torch {0} is installed!".format(torch.__version__))
	print("Test finished successfully!")
except e:
	print("ERROR: Pytorch is not installed in the computer!")
	print("Try to install it or re-install it in case of malfunction.")
	sys.exit()


import numpy as np
import matplotlib.pyplot as plt

print("Hello World! torch, numpy and matplotlib have been loaded. Let's play with them!")

print('We will train a neural network that approximates y=sin(x)')

x = 5*torch.rand(30,1)
y = torch.sin(x)

print('We created a data set x with 50 random numbers in [0,4]')
print('and the vector y=f(x)')

plt.plot(x,y,'*',label='Data points')
plt.legend()
plt.show()

print('\nThe neural network has one input, a hidden later with 5 neurons, sigmoid activation and one output')

## The NN Model                                                                 
model = torch.nn.Sequential(
    torch.nn.Linear(1,5),
    torch.nn.Sigmoid(),
    torch.nn.Linear(5,1)
    )
print(model)

print('\nAs goal function for minimization we use the sum of squares')
loss_fn = torch.nn.MSELoss(reduction='sum')
print(loss_fn)

print('\nAs optimizer we use Adam:')
optimizer = torch.optim.Adam(model.parameters())
print(optimizer)

print('\nNow, we train the network using 5000 steps:')
losses = []
for t in range(5000):
    torch_prediction = model(x)
    loss = loss_fn(torch_prediction,y)
    losses.append(loss.item())
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()


plt.title('Optimization of the neural network')
plt.plot(losses,label='Reduction of the goal functional')
plt.xlabel('iterations')
plt.ylabel('loss')
plt.show()



print('\nNow the network has been trained and we apply it to test data from the interval [0,10]')
xt = torch.linspace(0,10,101).reshape(101,1)
yt = model(xt)
plt.title('Performance of the neural network')
plt.plot(x,y,'*',label='Data points')
plt.plot(xt.detach().numpy(),torch.sin(xt).detach().numpy(),label='Sine of test data')
plt.plot(xt.detach().numpy(),yt.detach().numpy(),label='Neural network approximation')
plt.legend()
plt.show()



