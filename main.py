import sys

def deleteTemp():
    try:
        from Modules.Data.Delete import deleteTEMP
        deleteTEMP()
    except Exception:
        print('failed to delete TEMP.')
    else:
        print('TEMP deleted.')

if __name__ == '__main__':
    try:
        '''
this try/except statement serves as a basic bug detector
that prevents the application from crashing.
        '''
        ##tools
        from Modules.DebugTools import beforeExit, traceBug

        ##
        print('loading pygame...')
        import pygame
        print('pygame loaded.')
        pygame.init()

        def logo():
            from Modules.Classes.Text   import Label, fade
            from Modules.Locals.Display import CENTERX, CENTERY, DISPLAY
            from Modules.Locals.Fonts   import LOGO

            size, text = 40, 'presented by'
            surf = Label(LOGO, size, text).get_surf()
            rect = surf.get_rect(centerx=CENTERX, bottom=CENTERY)
            DISPLAY.blit(surf, rect)

            size, text = 60, 'OurDreams'
            surf = Label(LOGO, size, text).get_surf()
            rect = surf.get_rect(centerx=CENTERX, top=CENTERY)
            DISPLAY.blit(surf, rect)

            fade(DISPLAY, delay=500)

        # logo()
        from Modules.Stages.Home import home
        home()
    except Exception:
        sys.stderr.write('BUG OCCURED!!!')
        sys.stderr.write('IN GAME:')
        traceBug()
        #beforeExit()
    except SystemExit:
        print('-'*32)
        value = traceBug(print_exc=False)
        sys.stderr.write('SYSTEM EXIT: %s\n' % value)
    finally:
        pygame.quit()

        try:
            from Modules.Data.LoadSave import saveUserData
            from Modules.Data.Running  import loadTempUser
            user = loadTempUser()
            saveUserData(user)
        except Exception:
            print('failed to save user data.')
        else:
            print('user data saved.')

        try:
            from Modules.Data.LoadSave import savePlayerData
            from Modules.Data.Running  import loadTempPlayer
            player = loadTempPlayer()
            savePlayerData(user['username'], player)
        except Exception:
            print('failed to save player data.')
        else:
            print('player data saved.')

        deleteTemp()

