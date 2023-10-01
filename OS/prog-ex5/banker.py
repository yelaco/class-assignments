import numpy as np


class Banker:
    def __init__(self, n, m, available, maximum, allocation):
        self.num_process = n
        self.num_resource = m
        self.available = np.array(available)
        self.max = np.array(maximum)
        self.allocation = np.array(allocation)
        self.need = self.max - self.allocation

    def request(self, i, req):
        if req.any() > self.need[i].any():
            return False
        if req.any() > self.available.any():
            return False
        old_state = (self.available.copy(), self.allocation[i].copy(), self.need[i].copy())
        self.available = self.available - req
        self.allocation[i] = self.allocation[i] + req
        self.need[i] = self.need[i] - req
        if self.is_safe():
            return True
        else:
            self.available, self.allocation[i], self.need[i] = old_state
            return False

    def is_safe(self):
        work = self.available
        finish = [False for i in range(self.num_process)]
        # to save the process sequence that satisfies the safety condition
        print("Process sequence: ", end="")
        while True:
            i = next(filter(lambda i: not finish[i] and self.need[i].all() <= work.all(), range(self.num_process)), None)
            if i is None:
                print("")
                return all(lambda i: finish[i] for i in range(self.num_process))
            else:
                work = work + self.allocation[i]
                finish[i] = True
                print(i, end=" ")

    def run(self, requests):
        for i in range(len(requests)):
            # assume that it is safe at the time t0
            if requests[i] and self.request(i, np.array(requests[i])):
                # print state
                print(requests[i])
                requests[i] = None
                i = 0
        print("Done: Banker Algorithm!")
