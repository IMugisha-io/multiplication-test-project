# write a tax calculator that calculates tax using the following brackets
#If earnings < 12000 per year, pay no tax
#then with earnings between 12,000 and 36,000 pay 20% tax
#then with earnings greater than 36000 per year, pay 40% tax
#Use a test first approach.  Commit at least after every passing test.

#---------- <12000---------------------
'''def taxcalculator (a):
    return 0 '''

#----------  20 % brackert ---------------------
'''def taxcalculator (a):
    if a < 12000:
        result = 0
    else: 
       result = a * 0.20

    return result '''

#----------  a > 36,000 ; 40%  brackert ---------------------
def taxcalculator (a):
    if a < 12000:
        result = 0
    elif a <  36001 :
        result = a * 0.20
    else : 
        result = a * 0.4

    return result