import sys

#Input arguments by adding them to the sys.argv list.
#First element in the list must be "pendulum.py"

#For the second element, write "euler" to run Euler, or 'eulerCromer' to run Euler-Cromer
#Add a third element if you want to change the step size. Default is 0.03, don't add anything and this value is used. 
#Try another input in the interval [0.001, 0.05].
sys.argv = ['pendulum.py', 'eulerCromer', 0.005]


#Don't touch this code!
try:
    exec(open("pendulum.py").read())
except:
    print("Invalid argument. See main.py for instructions")