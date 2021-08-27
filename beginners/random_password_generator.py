""" This file is create and managed by Tahir Iqbal
    ----------------------------------------------
       It can be use only for education purpose
"""

import random
string = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
#input your pasword len
passlen = int(input())
password =  "".join(random.sample(string,passlen))
print(password)

