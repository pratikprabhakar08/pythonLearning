''' 
Python function named  chessboard(n) that prints a chessboard pattern
e.g.
.#.#.#.#
#.#.#.#.
.#.#.#.#
#.#.#.#.
.#.#.#.#
#.#.#.#.
.#.#.#.#
#.#.#.#.
'''
def chessboard(n):
    pattern1= '.#'
    pattern2= '#.'
    columnRange= n//2
    for row in range(0, n):
        for col in range(columnRange, n):
            if row%2 != 0:
                chessboard = pattern1 *columnRange+"."
            else:
                chessboard = pattern2 *columnRange+"#"
            print(chessboard,"",end="")
        print("")
