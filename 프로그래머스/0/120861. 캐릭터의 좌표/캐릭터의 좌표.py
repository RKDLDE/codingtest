def solution(keyinput, board):
    x, y = 0, 0
    limit_x = board[0] // 2
    limit_y = board[1] // 2

    for i in keyinput:
        if i == "left":
            x -= 1
        elif i == "right":
            x += 1
        elif i == "up":
            y += 1
        elif i == "down":
            y -= 1
        
        if abs(x) > limit_x:
            x = limit_x if x > 0 else -limit_x
        if abs(y) > limit_y:
            y = limit_y if y > 0 else -limit_y
    
    return [x, y]