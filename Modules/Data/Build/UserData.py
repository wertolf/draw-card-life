'''
This module constructs the default player and user data.
'''

from ...Locals.Basics import USER

def buildUserData(username):
    print('-'*32)
    print('constructing user data...')

    userDict = USER.copy()
    userDict['username'] = username

    print('user data constructed.')
    return userDict
