#In this function we will introduce to the user my name and what the rest of the program will do.
def introduction():
    print("***********************************************************************************")
    print("Hello! My name is []")
    print("This program will ask you for 3 numbers")
    print("It will give you the average of the 3 numbers and compare them to the average")
    print("There is a 3 number special combination. Can you guess it?")
    print("Good Luck!")
    print("***********************************************************************************")

#This function takes the paramaters from the main function of the number input. Then they will compute the average of the three numbers to the 3rd decimal.
def find_average(num_1, num_2, num_3):
    average = (((num_1 + num_2 + num_3) / 3 ))
    print (f'The average is {average:.3f}')
    return average
 
#We are comparing the average to all the input the user puts     
def compare_to_average(num_1, num_2, num_3,average):
    #we have a variable that takes whatever is equal to the average gains one to the variable
    equal_to_average = 0 
    #if the inputs is equal to the average add towards the counter
    for total in (num_1, num_2, num_3):
        if total == average:
            print(f'Number {total} is equal to the average')
            equal_to_average += 1
        elif total < average:
            print(f'Number {total} is below then the average')
        else:
            print(f'Number {total} is above then the average')

    print(f'{equal_to_average} value(s) is equal to the average')

#This is a funtion that asks the user for input of numbers and takes the funtions of other
def main():
    #first the introduction is shown
    introduction()
    #there is a special combination which is 1,2,3 that the user has to guess to break the loop
    special_combination = {1,2,3}
    count_to_sets = 0 
    #While the loop is true the user is asked for a loop till the user guesses the special combination
    while True:
        num_1 = (int(input("Enter a number: ")))
        num_2 = (int(input("Enter a number: ")))
        num_3 = (int(input("Enter a number: ")))
        num_input = {num_1,num_2,num_3}
        #once the user guesses the special combination then a message is played 
        if num_input == special_combination:
            count_to_sets += 1
            print("***********************************************************************************")
            print("Congradulations! You got the special combination!")
            print(f'The amount of times it took you to guess is {count_to_sets}')
            print(f'The Entered three numbers are: {num_1} , {num_2} , {num_3}')
            average = find_average(num_1, num_2, num_3)
            compare_to_average(num_1, num_2, num_3, average)
            print("***********************************************************************************")
            break
        #if the user gets to 10 the program stops and a message is played 
        else:
            count_to_sets += 1
            #This prints out a message of the average and the numbers being compared to the average and the anmount of times the sets have printed
            print("***********************************************************************************")
            print(f'The original three numbers are: {num_1} , {num_2} , {num_3}')
            average = find_average(num_1, num_2, num_3)
            compare_to_average(num_1, num_2, num_3, average)
            print("***********************************************************************************")
    
    
main()
