import random

def generatePageSequence(num_frame: int, is_random: bool):
    if not is_random:
        return [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5] 
    out = []
    for i in range(20):
        out.append(int(random.random() * num_frame))
    return out