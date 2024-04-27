'''
This module stores useful functions.
'''

def getRect(surface, x, y):
    '''x, y are tuples (left, centerx, right), (top, centery, bottom).'''
    left, centerx, right = x
    top, centery, bottom = y
    rect = surface.get_rect()
    #if x == (None, None, None) and y == (None, None, None):
        #rect is by default set to the left top corner of DISPLAY

    #only one of three will be assigned
    if left   != None: rect.left = left
    if centerx!= None: rect.centerx = centerx
    if right  != None: rect.right = right

    #only one of three will be assigned
    if top    != None: rect.top = top
    if centery!= None: rect.centery = centery
    if bottom != None: rect.bottom = bottom

    return rect
