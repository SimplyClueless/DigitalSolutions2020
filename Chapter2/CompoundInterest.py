P = float(input("Enter the principal in 'dollars': "))
R = float(input("Enter the interest rate as a 'decimal': "))
N = float(input("Enter the number of compound repayments per year: "))
T = float(input("Enter the number of years to pay back in 'years': "))

print("Compound interest is", P * (1.0 + R/N) ** (N*T))
