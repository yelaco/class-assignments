from queue import Queue
from utils import generatePageSequence

num_frame = 10
max_cache_frame = 3
page_sequence = generatePageSequence(num_frame=num_frame, is_random=True)
cache = []
page_fault = 0

print(f"Reference sequence: {page_sequence}\n")

for page in page_sequence:
    if page in cache:
        print("hit!")
        continue
    if len(cache) == max_cache_frame:
        cache.pop(0)
    cache.append(page)
    page_fault += 1
    print(cache)

print(f"\nNumber of page fault: {page_fault}")
        