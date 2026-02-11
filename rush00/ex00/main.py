from checkmate import checkmate
#R K B K Q B K R
#P P P P P P P P
#. . . . . . . .
#. . . . . . . .
#. . . . . . . .
#. . . . . . . .
#P P P P P P P P
#R K B Q K B K R 

#board
def main():
    board = """\
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . . 
. . . . . . . . 
"""

    checkmate(board)

#เชื่อม
if __name__ == "__main__":
    main()
