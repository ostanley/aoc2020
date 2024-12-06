from core.file_reader import yield_line
from collections import defaultdict

def add_rule(line, rules):
    a, b = line.split('|')
    rules[a]['after'].append(b)
    rules[b]['before'].append(a)
    return rules

def check_sheets(line, rules):
    values = line.split(',')
    for i, val in enumerate(values):
        if set(rules[val]['before']).intersection(values[i+1:]) or set(rules[val]['after']).intersection(values[:i]):
            return 0
    return int(values[(len(values)-1)/2])

def fix_sheets(line, rules):
    values = line.split(',')
    repaired_line = [values[0]]
    for n in values[1:]:
        new_pos = 0
        test_line=[n] + repaired_line
        while check_sheets(','.join(test_line), rules) == 0:
            test_line = repaired_line[:new_pos] + [n] + repaired_line[new_pos:]
            new_pos += 1
        repaired_line=test_line
        print(repaired_line)
    return int(repaired_line[(len(repaired_line)-1)/2])
        
        
if __name__=="__main__":
    file = 'Day05/Day05input.txt'

    middle_sum = 0
    repaired_sum = 0
    rules = defaultdict(lambda: {'before':[], 'after':[]})
    for line in yield_line(file):
        if '|' in line:
            rules = add_rule(line, rules)
        if line=="":
            print(rules)
        elif ',' in line:
            result = check_sheets(line, rules)
            if result==0:
                repaired_sum += fix_sheets(line, rules)
            else:
                middle_sum += result

    print("Part 1: ", middle_sum)
    print("Part 2: ", repaired_sum)