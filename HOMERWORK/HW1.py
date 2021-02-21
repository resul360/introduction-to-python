# homework1
# Global Ai HUB homework1 17/02/2021
# square matrix
import random

# n=int(input("Please enter matrix dimension: "))
n=3
my_matrix=[[0 for x in range(n)] for x in range(n)]

for i in range(int(n)):
    for j in range(int(n)):
        number=random.randint(0,100)
        my_matrix[i][j]=number

print(my_matrix)
        