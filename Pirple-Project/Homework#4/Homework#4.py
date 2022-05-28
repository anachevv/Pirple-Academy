my_unique_list = ['5']


def add_function(my_unique_list, number):
    number = input("Type a number: \n")
    for number in my_unique_list:
        if number not in my_unique_list:
            my_unique_list.append(number)
            print("The number that you just typed wasn't in my list until now. It has be already added in.")
            print(my_unique_list)
            continue
        
        elif number in my_unique_list:
            print(input("This number is already in my list. Type another one: \n"))
            continue


add_function(my_unique_list, "Is it done correctly?")
