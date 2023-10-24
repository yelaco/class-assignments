from detection import Detector

if __name__ == '__main__':
    num_process = 5
    num_resource = 3
    Available = [0, 0, 0]
    Allocation = [
        [0, 1, 0],
        [2, 0, 0],
        [3, 0, 3],
        [2, 1, 1],
        [0, 0, 2]
    ]
    Request = [
        [0, 0, 0],
        [2, 0, 2],
        [0, 0, 0],
        [1, 0, 0],
        [0, 0, 2],
    ]

    assert num_resource == len(Available), \
        "Number of resource doesn't match the number declared"
    assert num_process == len(Allocation), \
        "Number of process doesn't match the number declared"

    detector = Detector(num_process, num_resource, Available, Allocation, Request)
    detector.run()