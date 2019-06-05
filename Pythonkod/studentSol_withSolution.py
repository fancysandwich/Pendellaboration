from math import *
def euler(t, theta, dtheta, dt, m, L, g):
	# # Our solutions:
	t += dt # Increasing initial time
	
	accel = -g/L * sin(theta) # equation of pendulum motion without damping

	# Numerical methods

	# 1) Euler method:
	theta += dtheta * dt
	dtheta += accel * dt

	return t, theta, dtheta

def eulerCromer(t, theta, dtheta, dt, m, L, g):
	t += dt
	accel = -g/L * sin(theta)
	# 2) Euler-Cromer
	dtheta += accel * dt # velocity at later time
	theta += dtheta * dt # position at later time
	return t, theta, dtheta

def energy(theta, dtheta, m, L, g):
	energy = 0.5 * m * L ** 2 * dtheta ** 2 + m * g * L * (1 - cos(theta))  # energy equation
	return energy
