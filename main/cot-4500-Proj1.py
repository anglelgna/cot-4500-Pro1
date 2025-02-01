# Angelina Alderman
# COT 4500
# Programming Assignment 1

# Approximation Algorithm
def approximation_algorithm(a, tolerance, counter = 0):
	print (f"{counter} : {a}")
	diff = a
	while diff >= tolerance:
		counter += 1
		y = a
		a = (a / 2) + (1 / a)
		print (f"{counter} : {a}")
		diff = abs(a - y)
	print()
	print(f"Convergence after {counter} iterations")
	return

# Bisection Method

def fun(x):
	return (x + 4)*x**2 - 10

def dfun(x):
	return 3*x**2 + 8*x

def bisection_method(a, b, tolerance, counter = 0):
	if fun(a) * fun(b) < 0:
		midpoint = (a + b) / 2
	if abs(fun(midpoint)) < tolerance:
		print(midpoint)
		return counter
	if fun(a) * fun(midpoint) < 0:
		return bisection_method(a, midpoint, tolerance, counter + 1)
	else:
		return bisection_method(midpoint, b, tolerance, counter + 1)

# Fixed Point
def fpfun(x):
	return ((-x - 4) * x + 1) * x + 10

def fixed_point(a, tolerance, max_iterations, counter = 0):
	counter += 1
	p = fpfun(a)
	if counter > max_iterations or p == float("inf") or p == float("-inf"):
		print("Result diverges")
		print()
		print(f"Failure after {counter} iterations")
		return counter
	print (f"{counter} : {p}")
	if abs(a - p) < tolerance:
		print()
		print(f"Success after {counter} iterations")
		return counter
	return fixed_point(p, tolerance, max_iterations, counter)

# Newton Method

def newton_method(a, tolerance, counter = 0):
	if dfun(a) == 0:
		print("Unsuccessful (derivative is 0)")
		return counter
	if abs(fun(a)) < tolerance:
		print(counter)
		print("Success")
		return counter
	return newton_method(a - fun(a)/dfun(a), tolerance, counter + 1)

# Main
def main():
	approximation_algorithm(1.5, .000001)
	print()
	bisection_method(1, 2, 10**-3)
	print()
	fixed_point(1.5, .000001, 50)
	print()
	newton_method(-4, 10**-4)


if __name__ == "__main__":
	main()