import re

def line_to_dict(line):
    id_dict = {}
    if line == "\n":
        return id_dict
    for pair in line.split(" "):
        id_dict[pair.split(":")[0]]=pair.split(":")[1]
        if id_dict[pair.split(":")[0]][-1:]=="\n":
            id_dict[pair.split(":")[0]] = id_dict[pair.split(":")[0]][:-1]
    return id_dict

def check_int(num, bounds):
    return bounds[0] <= int(num) <= bounds[1]

def check_ecl(value):
    return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def check_passport(passport, part):
    valid = True
    key_count = 0
    for key, value in passport.items():
        if key=='cid':
            continue
        if part==1:
            key_count+=1
            continue
        elif key=='pid':
            key_count+=1
            if not value.isdecimal() or len(value)!=9:
                valid = False
        elif key=='ecl':
            key_count+=1
            valid = check_ecl(value)
        elif key=='hcl':
            key_count+=1
            if len(value)==7:
                valid = bool(re.search('#[0-9a-f]{6,}', value))
            else:
                valid = False
        elif key=='hgt':
            key_count+=1
            if value[-2:]=='cm':
                valid = check_int(value[:-2], [150, 193])
            elif value[-2:]=='in':
                valid = check_int(value[:-2], [59, 76])
            else:
                valid = False
        elif key=='eyr':
            key_count+=1
            valid = check_int(value, [2020, 2030])
        elif key=='iyr':
            key_count+=1
            valid = check_int(value, [2010, 2020])
        elif key=='byr':
            key_count+=1
            valid = check_int(value, [1920, 2002])
        if not valid:
            return valid

    if key_count!=7:
        valid = False
    return valid

if __name__ == '__main__':
    fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
    f = open('Day4input.text', 'r')
    valid1 = 0
    valid2 = 0
    id = {}
    lines = f.readlines()
    lines.append("\n") #this is cheating I think but I am out of ideas
    for line in lines:
        if line!="\n":
            id.update(line_to_dict(line))
        else:
            valid1+=check_passport(id, 1)
            valid2+=check_passport(id, 2)
            id = {}
    print("Part 1: ", valid1, " ids found")
    print("Part 2: ", valid2, " ids found")
