#this program calculates the average test scores based on inputs from the user

def main():

    print("This program calculates the average of your tests.")
    score = input("what's the score?")
    total = 0
    while score != "":
            print(score)
            total = total + eval(score)
            score = input("what's the next score? (press enter to quit)")
            n = 1
            n = n + 1
            average = total / n

    print("your average is:",average,"%")

main()
