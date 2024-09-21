from queue import Queue
from utils import generatePageSequence
import random

def generatePageSequence(num_frame: int, is_random: bool):
    if not is_random:
        return [7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1] 
    out = []
    for i in range(20):
        out.append(int(random.random() * num_frame))
    return out

num_frame = 10 # page numbers (range from 0 to 9)
max_cache_frame = 4 # number of page frames (vary from 1 to 7)

page_sequence = generatePageSequence(num_frame=num_frame, is_random=True)
cache = []
page_fault = 0

lru = []

print(f"Reference sequence: {page_sequence}")
print(f"Current number of page frame: {max_cache_frame} (edit in source code)\n")

for page in page_sequence:
    # every recently refered page will be put at the end of lru list
    # (as the most recently used)
    print(f"current page: {page} -> ", end="")
    lru.append(page)
    if page in cache:
        print(f"hit! -> {cache}")
        lru.remove(page)
        continue
    if len(cache) == max_cache_frame:
        idx = cache.index(lru.pop(0))
        cache[idx] = page
    else:
        cache.append(page)
    page_fault += 1
    print(f"page fault! -> {cache}")

print(f"\nNumber of page faults: {page_fault}")