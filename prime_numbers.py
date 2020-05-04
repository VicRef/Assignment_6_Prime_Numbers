import os
clear = lambda: os.system("clear")

print(chr(27)+'[2j')
print('\033c')
print('\x1bc')

clear()




# Task : Print the prime numbers which are between 1 to entered limit number (n).

# You can use a nested for loop.
# Collect all these numbers into a list
# The desired output for n=100 :

# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
# list_prime_numbers = list()
        # print("i: ", i, " j: ", j, "    i % j: ", i % j)


# half_of_the_user_input = user_input // 2
# print("user_input: ", user_input, "     half_of_the_user_input: ", half_of_the_user_input)



#     is_prime = False
#     x = int(input("sayı gir: "))
#     for i in range(2, x // 2):
#         if not (x % i):
#             is_prime = True
#             break
#     if not is_prime: print(x, "is_prime")
#     else:        print(x, "not prime")



# while True:
#     is_prime = False
#     x = int(input("sayı gir: "))
#     for i in range(2, x):
#         if not (x % i):
#             is_prime = True
#             break
#     if not is_prime: print(x, "is_prime")
#     else:        print(x, "not prime")


user_input = int(input("Enter an upper limit: "))
list_prime_numbers = list()
total_iteration_number = 0          # (optional) for checking the code optimization

for outher_loop in range(2, user_input):
    is_prime = False
    total_iteration_number += 1
    for inner_loop in range(2, outher_loop):
        total_iteration_number += 1
        if not (outher_loop % inner_loop):
            is_prime = True
            break
    if not is_prime: 
        list_prime_numbers.append(outher_loop) 

print(list_prime_numbers)
print("total iteration number: ", total_iteration_number)


# (almost) same code with less iteration
user_input = int(input("Enter an upper limit: "))
list_prime_numbers = list()
total_iteration_number = 0          # (optional) for checking the code optimization

for outher_loop in range(2, user_input):
    is_prime = False
    total_iteration_number += 1
    max_range_for_inner_loop = (outher_loop // 2) + 1       # decreasing the iterations
    for inner_loop in range(2, max_range_for_inner_loop):
        total_iteration_number += 1
        if not (outher_loop % inner_loop):
            is_prime = True
            break
    if not is_prime: 
        list_prime_numbers.append(outher_loop) 

print(list_prime_numbers)
print("total iteration number: ", total_iteration_number)


# user_input = int(input("Enter an upper limit: ")) + 1
# list_prime_numbers = list()

# for outher_loop in range(2, user_input):
#     is_prime = False

#     for inner_loop in range(2, (outher_loop // 2)):

#         if not (outher_loop % inner_loop):
#             is_prime = True
#             break
    
#     if not is_prime: 
#         list_prime_numbers.append(outher_loop) 

# print(list_prime_numbers)


# for i in range(1, user_input):
#     half_of_index_i = i // 2
#     j = 2
#     prime_number = False
#     (i % j)
#     print(end="")

#     while not (prime_number) and (j < half_of_index_i):
#         if (i % j): 
#             prime_number = True
            
#         j += 1
        

#     if prime_number: 
#         print(i, "is prime")
#     else:
#         print(i, "not prime")

#     if half_of_the_user_input + 1 >= i:      # is_prime = True



















# user_input = 55

# is_prime = False

# print(9 % 2)
# print(9 % 3)
# print(9 % 4)
# print(9 % 5)


# for i in range(2, 2):
#     print("öööö")
# v = 4
# h = (v // 2) + 1
# p = ((v + 1) // 2)
# print(h, p)

# for i in range(1, user_input):
#     is_prime = False
#     half_of_the_user_input = ((i + 1) // 2)                         # print("   i: ", i, "    half_of_the_user_input: ", half_of_the_user_input, end="")
#     if half_of_the_user_input + 1 >= i:                             # is_prime = True
#         list_prime_numbers.append(i)                                # print("   is_prime: ", i)
#     else:
#         for j in range(2, half_of_the_user_input + 1):            
#             if (i % j) == 0:
#                 is_prime = True
#             else: 
#                 is_prime = False


#     if is_prime:
#         list_prime_numbers.append(i)



                # print("before break")
                # break

            # print("after break out if")
    # print("   i = ", i, "   j = ", j, "   is_prime = ", is_prime)


# print(list_prime_numbers)
    # if is_prime:
    #     print("prime:     ", i)


    # for j in range(1, (i // 2) + 1):
    #     if (i % j):
    #         print(i, " is prime")
    #         break




    # if is_prime:
    #     print("prime:     ", i)
#     # else:
#         print("not prime: ", i)

# print("end of the prog...")