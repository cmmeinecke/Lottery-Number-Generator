#Lottery number generator program by Caitlin Meinecke CST 150

#Import random module to use for random numbers
import random

#Create main function
def main():
    #Generate the lottery number by calling lottery_number_generator function
    lottery_numbers = lottery_number_generator()

    #Display the lottery numbers on same line and use for loop
    print("The lottery numbers are:", end=' ')
    for number in lottery_numbers:
        print(number, end='')
        
#Create function to generate random lottery numbers        
def lottery_number_generator():
    #Create an empty list to store the lottery numbers
    lottery_numbers = []

    #Use for loop so that it iterates 7 times for 7 numbers
    for i in range(7):
        #Generate a random number between 0 and 9
        number = random.randint(0, 9)
        #Append each number to a list element
        lottery_numbers.append(number)
    
    #Return the lottery numbers list
    return lottery_numbers

#Conditionally execute main function
if __name__ == '__main__':
    main()

