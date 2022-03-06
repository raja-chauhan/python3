# Python3 program to find factorial of given number

# ----- Recursion -----
# method to find factorial of given number
def factorialUsingRecursion(n):
	if (n == 0):
		return 1;

	# recursion call
	return n * factorialUsingRecursion(n - 1);

# ----- Iteration -----
# Method to find the factorial of a given number
def factorialUsingIteration(n):
	res = 1;

	# using iteration
	for i in range(2, n + 1):
		res *= i;

	return res;

# Driver method
num = 5;
print("Factorial of",num,"using Recursion is:",
					factorialUsingRecursion(5));

print("Factorial of",num,"using Iteration is:",
					factorialUsingIteration(5));
	
# This code is contributed by mits
