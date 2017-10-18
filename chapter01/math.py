import math

def main():
    print("This program illustrates a half-life function")
    x = eval(input("Enter starting amount:"))
    print("What is the half-life of the element?")
    y = eval(input("Enter the half life power"))
    for i in range(y):
            x = x * pow(1 / 2, y)
            print(x)

main()
