'''
This module handles login data saving and loading processes.
'''

#constants
DATA = r'LogIn.txt'

#functions
def loadLoginData():
    print('loading login data...')
    try:
        with open(DATA) as file:
            text = file.read()
            loginList = eval(text)
        print('data loaded.')
        return loginList
    except FileNotFoundError:
        print('data not found.')
        print('creating new data...')
        return []

def saveLoginData(loginList):
    print('saving login data...')
    
    with open(DATA, 'w') as file:
        text = str(loginList)
        file.write(text)
    print('data saved.')
