from utils import generatePageSequence

num_frame = 10
max_cache_frame = 3
page_sequence = generatePageSequence(num_frame=num_frame, is_random=True)
cache = []
page_fault = 0

mfu = [0 for i in range(num_frame)]
fifo = []

print(f"Reference sequence: {page_sequence}\n")

for page in page_sequence:
    mfu[page] += 1
    if page in cache:
        print("hit!")
        continue
    if len(cache) == max_cache_frame:
        min_freq = max([mfu[p] for p in cache])
        removing_page = 0
        for i, p in enumerate(fifo):
            if mfu[p] == min_freq:
                removing_page = p
                fifo.pop(i)
                break
        mfu[removing_page] = 0
        cache[cache.index(removing_page)] = page
    else:
        cache.append(page)
    fifo.append(page)
    page_fault += 1
    print(cache)

print(f"\nNumber of page faults: {page_fault}")