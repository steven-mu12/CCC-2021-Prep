
N = int(input())

messages = []
final_messages = []

for x in range(N):
    coded_message = input()
    split_code = list(coded_message)
    messages.append(split_code)

# decode algorithm
index_pos = 0
index_pos2 = index_pos + 1
counter = 0

for message_x in messages:

    while message_x[index_pos] == message_x[index_pos2]:
        counter = counter + 1
        index_pos = index_pos + 1
        index_pos2 = index_pos2 + 1
    
    decoded_message = []
    decoded_message.append(counter)
    decoded_message.append(" ")
    decoded_message.append(message_x[index_pos])
    decoded_message.append(" \n")

    final_messages.append(decoded_message)

    index_pos = index_pos2
    index_pos2 = index_pos + 1
    
print (final_messages)
    



