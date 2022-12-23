#lists_and_dictionaries.py
#Need to practice how to find the highetst value in a list

list01 = [12, 25, 84, 196, 74, 15 ,16, 99]

list02 = [54, 92, 74, 65, 32, 91, 65, 44]

#The long way*********************************************

highest_number01 = 0
highest_number02 = 0

lowest_number01 = 0
lowest_number02 = 0

for i in range(len(list01)):
    if list01[i] > highest_number01:
        highest_number01 = list01[i]

for i in range(len(list02)):
    if list02[i] > highest_number02:
        highest_number02 = list02[i]

print(f"Using a For Loop, the highest number in list01 is {highest_number01}.")

print(f"Using a For Loop, he highest number in list02 is {highest_number02}.")

#The easy way********************************************
print('\n')
highest_number01 = max(list01)
print(f"Using the Max Function, the highest number in {list01} is {highest_number01}.")

highest_number02 = max(list02)
print(f"Using the Max Function, the highest number in {list02} is {highest_number02}.")

print('\n')

lowest_number01 = min(list01)
print(f"Using the Min Function, the lowest number in {list01} is {lowest_number01}.")

lowest_number02 = min(list02)
print(f"Using the Min Function, the lowest number in {list02} is {lowest_number02}.")


#Need to practice how to find the highetst value in a dictionary

dict01 = {
    "Andy": 10,
    "Timmy": 12,
    "Johnny": 18,
    "Bobby": 11,
    "Annie": 16,
    }

oldest_kid = 0
kid_name = ""

for key, value in dict01.items():
    if value > oldest_kid:
        oldest_kid = value
        kid_name = key

print('\n')
print(f"Using a For Loop, the oldest kid in the dictionary:\n{dict01}\nis {kid_name}, who is {oldest_kid} years old.")