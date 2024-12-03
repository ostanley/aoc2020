from collections import Counter
from core.file_reader import yield_line
import numpy as np

def determine_safety(report):
    diffs = np.diff(report)
    if sum(abs(diffs) > 3) > 0 or sum(abs(diffs) < 1) > 0: 
        return False
    elif Counter(np.sign(diffs)).values()>0 and len(Counter(np.sign(diffs)).keys())>1:
        return False    
    return True

def iterate_for_safety(report):
    for i,_ in enumerate(report):
        if determine_safety(report[:i]+report[i+1:]):
            return True
    return False
    

if __name__ == "__main__":
    file = "Day02/Day02testinput.txt"

    safe_count = 0
    damp_safe_count = 0
    for i, line in enumerate(yield_line(file)):
        safe_count += int(determine_safety([int(l) for l in line.split(" ")]))
        damp_safe_count += int(iterate_for_safety([int(l) for l in line.split(" ")]))

    print("Part 1: {}".format(safe_count))
    print("Part 2: {}".format(damp_safe_count))