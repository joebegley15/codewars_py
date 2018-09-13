def bouncingBall(h, bounce, window):
    total = 0
    if bounce >= 1 or bounce <= 0:
        return -1
    while (h > window):
        total += 2
        h *= bounce
    return total - 1