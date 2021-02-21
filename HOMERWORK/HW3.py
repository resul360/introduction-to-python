# #homework3

# Global Ai HUB homework3 19/02/2021


def prime_first(number):
    for i in range(2,number):
        
        if (number % i) == 0:
            break
        else:  
            print(number)
           
def prime_second(number):
    for i in range(2,number):
        
        if (number % i) == 0:
            break
        else:  
            print(number)
        
        
for number in range(0,1000):
 	if 0<=number<500:
         prime_first(number)
 	else:
         prime_second(number)