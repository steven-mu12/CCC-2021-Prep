
apple3 = int(input())
apple2 = int(input())
apple1 = int(input())

banana3 = int(input())
banana2 = int(input())
banana1 = int(input())

apple_score = apple3*3 + apple2*2 + apple1
banana_score = banana3*3 + banana2*2 + banana1

if apple_score > banana_score:
    print ("A")
elif apple_score < banana_score:
    print ("B")
else:
    print ("T")