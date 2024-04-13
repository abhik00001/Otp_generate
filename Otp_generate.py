import math
import random

def generateOTP(num):
    otp =""
    for i in range(0,num):
        otp += str(math.floor(random.random()*10))
    return otp

otp = generateOTP(6)
print(otp)
def confirmOTP(user,otp):
    if user == otp:
        print("valid")
    elif len(user) < 6 or len(user)>6:
        print("Enter 6 digit code")
    else:
        print("invalid")

user = input("Enter OTP: ")
confirmOTP(user,otp)
