"""
    Name: Implement strStr()
    Source: Daily Coding Problem 
    Link: https://leetcode.com/problems/implement-strstr/
    Description:
        This problem was asked by Google.
        The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.
        Hint: The basic equation of a circle is x2 + y2 = r2.
"""

import random
import time
from typing import Tuple



def estimatePI(radius: float) -> float:
    estimation = 4
    points_in = 1
    points_total = 1
    t_end = time.time() + 10    

    while time.time() <= t_end:
        point = randomPoint((-1 * radius, radius), (-1 * radius, radius), 3)
        x = point[0]
        y = point[1]
        if x**2 + y**2 <= radius**2:
            # print("inside:", str(x), str(y))
            points_in += 1
        else:
            # print("outside:", str(x), str(y))
            pass
        points_total += 1
        estimation = 4 * (points_in/points_total)
        print(round(estimation, 3), "Number of Points:", points_total)
    print("\n---\nEstimation completed")
    print("Result:", estimation)

def randomPoint(x_bound: Tuple[float], y_bound: Tuple[float], accuracy: int) -> Tuple[float]:
    x_cor = round(random.uniform(x_bound[0], x_bound[1]), accuracy)
    y_cor = round(random.uniform(y_bound[0], y_bound[1]), accuracy)

    return(x_cor, y_cor)

estimatePI(1)