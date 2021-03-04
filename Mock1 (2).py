
#input and array setup

n = int(input())
array = []
counter = 0
array_pos = 0
position = 0

x = input()
array = x.split()

for item in array:
    item = int(item)
    array[array_pos] = item
    array_pos = array_pos + 1

#code

for number in array:
    if number == array[0]:
        position = position + 1
    
    elif number < array[position - 1]:
        while number < array[position - 1]:
            number = number + 1
            counter = counter + 1

        array[position] = number
        position = position + 1
        
    else:
        position = position + 1

print (counter)