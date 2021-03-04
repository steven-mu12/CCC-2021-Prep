
# Input and insert into list 
L = int(input())

final_list = []

for x in range(L):
    value = input()
    listed_value = value.split(" ")

    final_list.append(listed_value)

# Decode

for listed in final_list:
    number_part = listed[0]
    char_part = listed[1]

    message = int(number_part) * char_part

    print (message)