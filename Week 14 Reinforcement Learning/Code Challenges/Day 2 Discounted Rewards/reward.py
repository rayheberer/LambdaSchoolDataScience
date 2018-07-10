def reward(R, gamma):
    total_R = 0
    reward = R
    
    epsilon = 0.00001
    while abs(reward) > epsilon:
        total_R += reward
        reward *= gamma

    return total_R