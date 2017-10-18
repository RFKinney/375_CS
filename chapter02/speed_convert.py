#this program converts m/s to mph
#By: Ryan Kinney

def main():
    print("This program converts meters per second to miles per hour")
    x = eval(input("What is your speed in m/s?"))
    y = (1)
    if x < 0:
         print("invalid input")
    else:
 # mph = meters/second * 60 seconds/minute * 60 minutes/hour * 0.00062137 miles/meter
        for i in range(y):
            x = x * 60 * 60 * 0.00062137
            print(x)
            print("mph")

main()
