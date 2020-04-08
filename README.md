##LFA project



###Basically you put input in input.in in this format:

nrStates nrTrans InitialState
1stState Fin(0 or 1)
2ndState FinOrNot
.....
nThState FinOrNot
state Trans state  -> for all transtions

1. LFAproject1.py is the first project
    * Two ways of execution:
        1. No graphics -> no terminal arguments
        1. With graphics -> terminal argv: 1 [TimeBetweenTests] [TimeBetweenTransitions] ([]-optional)
    * Checks if a word passes the automat testing
1. LFAproject2.py is the second project (T7)
    * Has the same stuffs as project 1 for terminal arguments
    * To launch project 2 use the terminal argument 2
    * Takes the FA and visually transforms it in a RE


###Requirements:
1. tkinter(graphics.py) which can be installed by
    * pip install /path-to-tar
    * pip install (-e) /path-to-file
1. Recommended to have linux! xD

