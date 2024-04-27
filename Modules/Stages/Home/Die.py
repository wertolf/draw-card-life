'''
This module stores func die()
'''

#classes
from ...Classes.Text   import Label
from ...Classes.Button import LabelButton, drawButtons, moveAndClick

#constants
from ...Locals.Basics  import LIVINGCARDS
from ...Locals.Colors  import BGCOLOR
from ...Locals.Display import CENTERX, CENTERY, DISPLAY, update
from ...Locals.Fonts   import BUTTON, REASON
from ...Locals.Sounds  import DIE, WIN

#functions
from ...Data.LoadSave import savePlayerData
from ...Data.Running  import loadTempPlayer, loadTempUser, updateTempPlayer, updateTempUser

def die(reason):
    user   = loadTempUser()
    player = loadTempPlayer()

    #calculate DustOfFate
    DustOfFate = 0
    DustOfFate += (player['C级卡']*0.01 + player['B级卡']*0.02 + player['S级卡']*0.05)
    DustOfFate += (player['R级卡']*0.1  + player['SR级卡']*0.2 + player['SSR级卡']* 1)
    for card in LIVINGCARDS:
        DustOfFate += player[card]*0.5
    DustOfFate += (player['day']-1)*10
    DustOfFate *= (1+user['fate']['dust']*0.1)

    user['DustOfFate'] += DustOfFate
    updateTempUser(user)

    print('game over.')
    #disable player data so that it is no longer a valid save
    #this will disable LOAD when return to home page
    player['status'] = 'die'
    updateTempPlayer(player)
    savePlayerData(user['username'], player)

    #screen
    DISPLAY.fill(BGCOLOR)
    if reason == 'victory':
        WIN.play()

        filename, size = REASON, 120
        surf = Label(filename, size, text='你获胜了！').get_surf()
        rect = surf.get_rect(centerx=CENTERX, bottom=CENTERY-80)
        DISPLAY.blit(surf, rect)

        filename, size = REASON, 40
        surf = Label(filename, size, text='本局命运尘埃：%.2f' % DustOfFate).get_surf()
        rect = surf.get_rect(centerx=CENTERX, top=CENTERY+40)
        DISPLAY.blit(surf, rect)

        filename, size = BUTTON, 64
        BACK = LabelButton(filename, size, text='返回')
        BACK.config(
            x=(None, CENTERX, None),
            y=(None, None, 800),
            )
        drawButtons(BACK)
        update()

        button = moveAndClick(BACK)
        if button == BACK:
            WIN.stop()
            return
    else:
        DIE.play()

        filename, size = REASON, 120
        surf = Label(filename, size, text=reason).get_surf()
        rect = surf.get_rect(centerx=CENTERX, bottom=CENTERY-80)
        DISPLAY.blit(surf, rect)

        filename, size = REASON, 40
        surf = Label(filename, size, text='本局命运尘埃：%.2f' % DustOfFate).get_surf()
        rect = surf.get_rect(centerx=CENTERX, top=CENTERY+40)
        DISPLAY.blit(surf, rect)

        filename, size = BUTTON, 64
        RIP = LabelButton(filename, size, text='R.I.P.')
        RIP.config(
            x=(None, CENTERX, None),
            y=(None, None, 800),
            )
        drawButtons(RIP)
        update()

        button = moveAndClick(RIP)
        if button == RIP:
            #force DIE to stop
            DIE.stop()
            return
