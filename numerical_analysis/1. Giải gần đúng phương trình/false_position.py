import numpy as np


def false_position(init_p_0: float, init_p_1: float, TOL: float, N_0: int):
    """
    INPUT initial approximations p0 , p1 ; tolerance TOL; maximum number of iterations N0 .
    OUTPUT approximate solution p or message of failure.
    """
    assert (
        f(init_p_0) * f(init_p_1) < 0
    ), f"f({init_p_0}) * f({init_p_1}) must be negative"
    print("\nStart iterating...")
    p_0 = init_p_0
    p_1 = init_p_1
    q_0 = f(p_0)
    q_1 = f(p_1)
    i = 2
    try:
        while i <= N_0:
            p = p_1 - q_1 * (p_1 - p_0) / (q_1 - q_0)
            print(f"p_{i-1} = {p}")
            if abs(p - p_1) < TOL:
                print(f"\nThe result is {p}")
                return
            i += 1
            q = f(p)
            if q * q_1 < 0:
                p_0 = p_1
                q_0 = q_1
            p_1 = p
            q_1 = q

        print(f"\nMethod failed after {N_0} iterations")
    except OverflowError:
        print(f"\nMethod diverged after {i-1} iterations")
    print("The procedure was unsuccessful.")


def f(x: float) -> float:
    return np.cos(x) - x


if __name__ == "__main__":
    print(
        "False Position: To ﬁnd a solution to f(x) = 0 given the continuous function f on the interval [p_0,p_1] where f(p_0) and f(p_1) have opposite signs"
    )
    p_0 = float(input("p_0 = "))
    p_1 = float(input("p_1 = "))
    tol = float(input("tolerance = "))
    num_iters = int(input("max num iterations = "))

    false_position(p_0, p_1, tol, num_iters)
