if __name__ == "__main__":
    # Part 1
    f = open('Day2input.text', 'r')
    valid_pwds = 0
    for line in f:
        l = line.split(' ')
        pwd_dict = {}
        for c in l[2]:
            if c in pwd_dict.keys():
                pwd_dict[c]+=1
            else:
                pwd_dict[c]=1
        lims = l[0].split('-')
        target_letter = l[1][0]
        if target_letter in pwd_dict.keys():
            if pwd_dict[target_letter] >= int(lims[0]) and pwd_dict[target_letter] <= int(lims[1]):
                valid_pwds+=1
                print(lims, target_letter, l[2])
    print(valid_pwds, " valid passwords found.")
    f.close()

    # Part 2
    f = open('Day2input.text', 'r')
    valid_pwds = 0
    for line in f:
        l = line.split(' ')
        targets = l[0].split('-')
        target_letter = l[1][0]
        hit_count=0
        for t in targets:
            if l[2][int(t)-1]==target_letter:
                hit_count+=1
        if hit_count==1:
            valid_pwds+=1
            print(targets, target_letter, l[2])
    print(valid_pwds, " valid passwords found.")
    f.close()
