# A factorial, denoted by an exclamation point ( ! ), 
# is the product of all positive integers less than or equal to a given non-negative integer. 
# For example, the factorial of 5 (written as 5!) is 5 * 4 * 3 * 2 * 1 = 120. 
# The factorial of 0 (0!) is defined as 1

#-------------0! & 1!--------------------------

'''def factorial (a):
    return 1 '''


#-------------2! & 3!--------------------------
'''def factorial (a):
    if a < 2 :
        result = 1
    else :
        result = a * (a-1)
    return result '''
        
#-------------4!--------------------------  

def factorial (a):
    if a < 2 :
        result = 1
    else :
        product = 1 
        for i in range(1,a+1):
            product*=i
            result = product
        
    return result 

