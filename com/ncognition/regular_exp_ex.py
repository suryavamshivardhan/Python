import re

def regular_exp_ex():
    exp = '[a-zA-Z1-9_.]*@[a-zA-Z1-9-]*.(com)'
    input_string = input('please enter the email address ...')
    result = re.match(exp,input_string)
    print('match output is : ',result)

    input_string1 = "there is rain in spain"
    result1 = re.findall(r'\br[a-z]*',input_string1)
    print('findall output is : ',result1)

regular_exp_ex()
