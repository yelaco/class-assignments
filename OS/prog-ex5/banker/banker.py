import numpy as np
import pandas as pd

class Banker:
    def __init__(self, n, m, available, maximum, allocation):
        self.num_process = n
        self.num_resource = m
        self.available = np.array(available)
        self.max = np.array(maximum)
        self.allocation = np.array(allocation)
        self.need = self.max - self.allocation

    def request(self, i, req):
        if (req is None):
            return False
        req = np.array(req)
        if not (req <= self.need[i]).all():
            return False, "Request > Need"
        if not (req <= self.available).all():
            return False, "Request > Available"
        old_state = (self.available.copy(), self.allocation[i].copy(), self.need[i].copy())
        self.available = self.available - req
        self.allocation[i] = self.allocation[i] + req
        self.need[i] = self.need[i] - req
        is_safe, respond = self.is_safe()
        if is_safe:
            return True, respond
        else:
            self.available, self.allocation[i], self.need[i] = old_state
            return False, "Safe process sequence not available!"

    def is_safe(self):
        work = self.available.copy()
        finish = [False for i in range(self.num_process)]
        # to save the process sequence that satisfies the safety condition
        safe_seq = ""
        while True:
            cnt = 0;
            for i, finished in enumerate(finish):
                if not finished and all(self.need[i] <= work):
                    work += self.allocation[i]
                    finish[i] = True
                    safe_seq += f" {i}"
                    cnt += 1
            if cnt == 0: break
        if all(finish):
            return True, f"Safe process sequence:{safe_seq}"
        else:
            return False, None

    def run(self, requests):
        print("At time t0\n")
        while len(requests) != 0:
            succeed = []
            for i, req in requests.items():
                self.print_current_state() 
                print("Process P" + str(i) + " requests " + str(req))
                # assume that it is safe at the time t0
                accepted, respond = self.request(i, requests[i])
                if accepted:
                    succeed.append(i)
                    print(f"\n{respond}\n==> Allocate {req} for P{i}")
                else:
                    print(f"\nUnsafe request: {respond}\n==> Process P{i} must wait")
                print('\n-----------------------------------')
                input()
            for i in succeed:
                print(f"* Process P{i} finished -> return {self.allocation[i]}")
                self.available = self.available + self.allocation[i]
                self.allocation[i] = 0
                self.need[i] = 0
                requests.pop(i)
            print('\n-----------------------------------\n')
        print("Done: Banker Algorithm!")

    def print_current_state(self):
        print("<Current state>")
        print("Available: " + str(self.available))
        state = {
            'Allocation': [" ".join([str(e) for e in row]) for row in self.allocation],
            'Need': [" ".join([str(e) for e in row]) for row in self.need],
        }
        df = pd.DataFrame(state)
        print(df, end="\n\n")
