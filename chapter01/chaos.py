# File: chaos.py
# A simple program illustrating chaotic behavior

def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    print("how many times do you want to loop?")
    y = eval(input("Enter the number of times you want to loop: "))
    for i in range(y):
            x = 3.9 * x * (1 - x)
            print(i + 1, ":", x)

main()
