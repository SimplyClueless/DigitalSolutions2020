R = float(input("Enter the length of a row in 'feet': "))
E = float(input("Enter the amount of space for end post assembly in 'feet': "))
S = float(input("Enter the space between the vines in 'feet': "))
V = (R - 2*E) / S

print("The number of grapvines is",V // 1)