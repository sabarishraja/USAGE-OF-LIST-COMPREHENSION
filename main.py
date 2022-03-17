#PYTHON PROGRAM TO PRINT THE SAME NUMBERS IN BOTH THE FILES
with open("file1.txt") as file_1:
    file_12 = file_1.readlines()
with open("file2.txt") as file_2:
    file_21 = file_2.readlines()    
result = [int(num) for num in file_12 if num in file_21]
# Write your code above 👆
print(result)

