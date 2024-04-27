'''

'''
#built-in modules
import random

#constants
from ...Locals.Basics import ATTRS, DECK, LIVINGCARDS, PLAYER

#functions
from copy import deepcopy

def buildPlayerData(user):
    print('-'*32)
    print('constructing player data...')
    #reset player data
    player = deepcopy(PLAYER)
    #caution：use PLAYER.copy()，rather than PLAYER itself
    #otherwise starting a second game will not be possible
    
    ##acquire attributes
    #player['sttrs'] is a medis in order to get non-repeated attributes
    player['attrs'] = deepcopy(ATTRS)
    for i in range(5):
        attr = random.choice(player['attrs'])
        player['attrs'].remove(attr)
        exec('player[\'attr%d\'] = attr' % (i+1))
        
    #using player['attrs'] by the way to simplize codes below
    player['attrs'] = (player['attr1'], player['attr2'], player['attr3'], player['attr4'], player['attr5'])

    ##acquire deck
    player['deck'] = deepcopy(PLAYER['deck'])
    player['deck'] += ['食物卡']*5*user['fate']['food']
    player['deck'] += ['水卡']*5*user['fate']['water']
    player['deck'] += ['维生素卡', '抗生素卡', '抗感染卡', '镇静剂卡']*user['fate']['medi']
    player['deck'] += ['SSR级卡']*3*user['fate']['ssr'] #ssr is used twice

    times = 5 #how many times P increases, we do not need to guarantee each time P is increased to the same extend
    if '肥宅' in player['attrs']:
        '''increase P in getting food.'''
        for i in range(times):
            player['deck'].append('食物卡')
    if '酒鬼' in player['attrs']:
        '''increase P in getting water.'''
        for i in range(times):
            player['deck'].append('水卡')
    if '贝爷' in player['attrs']:
        '''increase P in getting living cards.'''
        for i in range(times):
            player['deck'] += LIVINGCARDS
    if '骰王' in player['attrs']:
        times *= (user['fate']['ssr']+1) #the second time ssr appears
        for i in range(times):
            if i % 5 == 0:
                '''P(C) should be larger than P(B).'''
                player['deck'].remove('B级卡')
            else:
                player['deck'].remove('C级卡')
            player['deck'].append('SSR级卡')

    print('player data constructed.')
    return player
