# Newton-Raphson method 

The Newton-Raphson method is an iterative root-finding algorithm used to approximate the roots of a real-valued function. It is particularly useful when finding roots of nonlinear equations. The method is based on linear approximation and can converge quickly to a solution if certain conditions are met.

Here's a step-by-step explanation of the Newton-Raphson method:

### Initialization
1. **Initialization**: Choose an initial guess $( x_0 )$ for the root of the function.

2. **Iteration**: Repeat the following steps until a satisfactory approximation is obtained:
   - Calculate the next approximation $( x_{n+1} )$ using the formula:
     $[ x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)} ]$
   - Here, $( f(x) )$ is the function whose root we are trying to find, and $( f'(x) )$ is its derivative.

3. **Stopping Criterion**: The iteration stops when a convergence criterion is met. Common convergence criteria include:
   - The absolute difference between successive approximations is smaller than a predefined tolerance (epsilon), denoted as $( |x_{n+1} - x_n| < \epsilon )$.
   - The function value at the current approximation is smaller than a predefined tolerance, i.e., $( |f(x_n)| < \epsilon )$.
   - A maximum number of iterations is reached.

4. **Output**: The final approximation obtained after convergence or after reaching the maximum number of iterations is considered the root of the function.

### Explanation of the code:
- The code accepts an integer input from the command line (presumably representing the number whose square root is to be found).
- It initializes the variable `t` with the input value `c`.
- Then, it enters a `while` loop where it iteratively refines the approximation of the square root using the Newton-Raphson formula until the condition `abs(t - c / t) > EPSILON` is no longer true.
- In each iteration, it updates the approximation of the square root using the formula `t = (c / t + t) / 2.0`.
- Once the condition for convergence is met, it prints out the final approximation, which is considered the square root of the input value.

This Python script essentially implements the Newton-Raphson method to find the square root of the input number `c` with a given tolerance `EPSILON`.
