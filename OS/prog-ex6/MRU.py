from queue import Queue
from utils import generatePageSequence

num_frame = 10
max_cache_frame = 3
page_sequence = generatePageSequence(num_frame=num_frame, is_random=False)
cache = []
page_fault = 0

mru = []

print(f"Reference sequence: {page_sequence}\n")

for page in page_sequence:
    # every recently refered page will be put at the end of the mru list
    # (as the most recently used)
    mru.append(page)
    if page in cache:
        print("hit!")
        mru.remove(page)
        continue
    if len(cache) == max_cache_frame:
        idx = cache.index(mru.pop(max_cache_frame-1))
        cache[idx] = page
    else:
        cache.append(page)
    page_fault += 1
    print(cache)

print(f"\nNumber of page faults: {page_fault}")