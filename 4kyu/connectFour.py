def who_is_winner(lst):
    board = [[] for _ in range(7)]
    for m in lst:
        m = m.split('_')
        i = 'ABCDEFG'.index(m[0])
        board[i] += [m[1]]
        if check_is_four(board, i, len(board[i])-1):
            return m[1]
    return 'Draw'


def check_is_four(board, i0, j0):
    p = board[i0][j0]
    for d in [(0,1), (1,0), (1, 1), (-1, 1)]:
        i, j = i0, j0
        for k in [-1, 1]:
            n = 0
            while True:
                i += k*d[0]
                j += k*d[1]
                if not (0 <= i < len(board) and 0 <= j < len(board[i]) and board[i][j] == p):
                    break
                n += 1
            
        if n >= 4:
            return True
        
    return False
