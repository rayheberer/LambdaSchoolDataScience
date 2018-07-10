def reward(R, gamma):
    total_R = 0
    reward = R
    
    for _ in range(1000):
        total_R += reward
        reward *= gamma

    return total_R