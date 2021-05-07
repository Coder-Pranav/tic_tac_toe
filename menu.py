from tic_tac_main import tic_tac_run
import nuke

menu = nuke.menu('Nuke')
menu.addCommand('tic_tac', lambda: tic_tac_run())