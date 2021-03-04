

small_treats = int(input())
medium_treats = int(input())
large_treats = int(input())

happiness = small_treats + medium_treats * 2 + large_treats * 3

if happiness >= 10:
    print ("happy")
else:
    print ("sad")

happiness = 0
