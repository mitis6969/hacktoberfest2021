def countepay(Hours=0,Rate=0) :                               #default arguments
    if Hours>40 :                                             #indentation is necessary
        hrs=Hours-40.0
        pay=40*Rate + hrs*Rate*1.5
    else :
        pay=Hours*Rate
    return pay

# Hours =float( input("Enter the hours : "))
# Rate = float(input("Enter the rate : "))                    #can write like this when there is no exception case

Hours = input("Enter the hours : ")
Rate = input("Enter the rate : ")
try :                                                         #First see that wether statements in try are possible if not then execute statements in except
    Hours = float(Hours)
    Rate = float(Rate)
except :
    Hours=-1
    Rate=-1

if Hours<0 :
    print('You have entered wrong inputs')
elif Rate<0 :
    print('You have entered wrong inputs')
else :
    p = countepay(Hours,Rate)
    print('pay',p)

print()
input("Press any key to continue........")
