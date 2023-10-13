import random



def main():

    userNumber = prompt()

    generatedNumber = random.randint(1,20)

    while True:
        if(compareValues(generatedNumber, userNumber)==True):
            print("You win!")
            break
        else:
            print("Try again")
            userNumber = int(prompt())

    


def prompt():

    userInput = input("Guess the number I thought between 1 and 20!: ")

    
    while not(userInput.isnumeric()) :
        userInput = input("Please enter only integer numbers: ")

    int(userInput)  

    while (1< int(userInput) >20):  
        userInput = int(input("Number out of range (1-20)!"))
          

    return int(userInput)



def compareValues(numberGenerated, numberUser):
    return numberGenerated == numberUser


if __name__ == "__main__": main()