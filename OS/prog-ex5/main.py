from banker import Banker

if __name__ == '__main__':
    num_process = 5
    num_resource = 3
    Available = [10, 5, 7]
    Max = [
        [7, 5, 3],
        [3, 2, 2],
        [9, 0, 2],
        [2, 2, 2],
        [4, 3, 3],
    ]
    Allocation = [
        [0, 1, 0],
        [2, 0, 0],
        [3, 0, 2],
        [2, 1, 1],
        [0, 0, 2],
    ]

    assert num_resource == len(Available), \
        "Number of resource doesn't match the number declared"
    assert num_process == len(Max) and num_process == len(Allocation), \
        "Number of process doesn't match the number declared"

    banker = Banker(num_process, num_resource, Available, Max, Allocation)
    requests = [
        [1, 0, 2],
        [3, 3, 0],
        [0, 2, 0],
    ]
    banker.run(requests)

