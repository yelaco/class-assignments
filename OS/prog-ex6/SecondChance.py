from utils import generatePageSequence

num_frame = 10
max_cache_frame = 3
page_sequence = generatePageSequence(num_frame=num_frame, is_random=False)
cache = []
page_fault = 0

refs = [0 for i in range(max_cache_frame)]

print(f"Reference sequence: {page_sequence}\n")

for page in page_sequence:
    if page in cache:
        print("hit!")
        refs[cache.index(page)] = 1
        continue
    if len(cache) == max_cache_frame:
        while page not in cache:
            for idx in range(len(cache)):
                if refs[idx] == 0:
                    cache[idx] = page
                    break
                else:
                    refs[idx] -= 1
    else:
        cache.append(page)
    print(cache)
    page_fault += 1

print(f"\nNumber of page faults: {page_fault}")
        