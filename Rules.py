print ("""
.______      ___________    ____  _______ .______          _______. __       _______      ___      .___  ___.  _______
|   _  \    |   ____\   \  /   / |   ____||   _  \        /       ||  |     /  _____|    /   \     |   \/   | |   ____|
|  |_)  |   |  |__   \   \/   /  |  |__   |  |_)  |      |   (----`|  |    |  |  __     /  ^  \    |  \  /  | |  |__
|      /    |   __|   \      /   |   __|  |      /        \   \    |  |    |  | |_ |   /  /_\  \   |  |\/|  | |   __|
|  |\  \----|  |____   \    /    |  |____ |  |\  \----.----)   |   |  |    |  |__| |  /  _____  \  |  |  |  | |  |____
| _| `._____|_______|   \__/     |_______|| _| `._____|_______/    |__|     \______| /__/     \__\ |__|  |__| |_______|

        Reversi is a 2 player game that is played on a grid of 8 x 8. The goal of Reversi is to have the majority of the discs changed to your colored when the last game piece is placed.
        
        The game pieces are called discs and they all have a side that is white and a side that is dark.
        Players take turns placing discs with the side of their corresponding color, facing up.
        When a player places a disk on the board, all the pieces that are between that player's newly placed disc and any of their previously placed discs, are turned to that player's color.
        When placing your discs on your turn, there has to be at least one piece of the opposite colour between your placed piece and any of your previously placed pieces. Otherwise the move is not valid.
        A move is only valid if one of the opposing player's discs are flipped over, otherwise the turn is passed to the opposing player.
        The placed pieces have to make either a horizontal, vertical or diagonal line with the opposing player's discs to flip any pieces over.

        The game ends when there are no more possible moves to make. The game can end before the entire grid is filled.""")
