def bouncing_ball(h, bounce, window):
    if 0 < bounce < 1 and h > 0 and window < h:
        count = 1
        b = bounce * h
        while b > window:
            count += 2
            h = b
            b = bounce * h
        return count
    else:
        return -1

bouncing_ball(30, 0.75, 1.5)

bouncing_ball(3, 1, 1.5)