import numpy as np
import pandas as pd

class Detector:
    def __init__(self, n, m, available, allocation, request):
        self.num_process = n
        self.num_resource = m
        self.available = np.array(available)
        self.allocation = np.array(allocation)
        self.request = np.array(request)
        
    def run(self):
        self.print_current_state()
        work = self.available.copy()
        finish = [all(self.request[i] == 0) for i in range(self.num_process)]
        # to save the process sequence that satisfies the safety condition
        already_finished = []
        for i, finished in enumerate(finish):
            if (finished):
                already_finished.append(i)
        safe_seq = ""
         
        while (True):
            cnt = 0
            for i, finished in enumerate(finish):
                if i in already_finished:
                    work += self.allocation[i]
                    already_finished.remove(i)
                    safe_seq += f" {i}"
                    cnt += 1
                if not finished and all(self.request[i] <= work):
                    work += self.allocation[i]
                    finish[i] = True
                    safe_seq += f" {i}"
                    cnt += 1
            if (cnt == 0): break

        if all(finish):
            print(f"Safe process sequence:{safe_seq}\n==> System keeps running")
        else:
            print(f"No safe sequence is found\n==> System in deadlock")
        

    def print_current_state(self):
        print("<Current state>")
        print("Available: " + str(self.available))
        state = {
            'Allocation': [" ".join([str(e) for e in row]) for row in self.allocation],
            'Request': [" ".join([str(e) for e in row]) for row in self.request],
        }
        df = pd.DataFrame(state)
        print(df, end="\n\n")