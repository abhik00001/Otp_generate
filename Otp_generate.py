# print("GPA calculator")

# points = {
#     "A+":5.0,
#     "A":4.0,
#     "A-":3.4,
#     "B+":3.0,
#     "B":2.6,
#     "B-":2.0,
#     "C+":1.8,
#     "C":1.2,
#     "C-":1.0,
#     "F":0.0
# }

# courses = 0
# total_points =0
# done =False
# while not done:
#     grade = input("Enter a grade: ").capitalize()
#     if grade == "":
#         done=True
#     elif grade not in points:
#         print("Enter Valid Grade")
#     else:
#         courses += 1
#         total_points += points[grade]
# if courses>0:
#     print("Num of GPA is{0:.2}".format(total_points/courses))

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