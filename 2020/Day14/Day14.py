import re


def update_mask(l):
    mask_str = l.split(' = ')[1]
    mask = [0]*len(mask_str)
    values = [0]*len(mask_str)
    for c in range(len(mask_str)):
        if mask_str[c] == 'X':
            mask[c] = 1
        else:
            values[c] = int(mask_str[c])
    mask = int("".join(str(x) for x in mask), 2)
    values = int("".join(str(x) for x in values), 2)
    return mask, values


def update_mem(l, mask, values, mem):
    ints = [int(x) for x in re.findall(r'\d+', l)]
    mem[ints[0]] = ints[1] & mask | values
    return mem


def update_addresses(l, mask, values, mem):
    ints = [int(x) for x in re.findall(r'\d+', l)]
    address = ints[0] | values
    mask = list(bin(mask)[2:].zfill(36))
    address = list(bin(address)[2:].zfill(36))
    addresses = set(get_address_list(address.copy(), mask.copy()))
    for a in addresses:
        mem[int(a, 2)] = ints[1]
    return mem


def get_address_list(address, mask):
    addresses = []
    for c in range(len(mask)):
        if mask[c] == '1':
            mask[c] = '0'
            address[c] = '1'
            addresses.append("".join(address))
            addresses += get_address_list(address.copy(), mask.copy())
            address[c] = '0'
            addresses.append("".join(address))
            addresses += get_address_list(address.copy(), mask.copy())
            break
    return addresses


def read_in_docking_program(file, func):
    mem = {}
    mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    values = [0]*len(mask)
    with open(file, 'r') as f:
        for l in f.readlines():
            if l[:4] == 'mask':
                mask, values = update_mask(l.strip())
            elif l[:4] == 'mem[':
                mem = func(l.strip(), mask, values, mem)

    total_sum = 0
    for k, v in mem.items():
        total_sum += v
    print(f'Total sum is {total_sum}')


if __name__ == '__main__':
    file = 'Day14input.txt'

    read_in_docking_program(file, update_mem)
    read_in_docking_program(file, update_addresses)
