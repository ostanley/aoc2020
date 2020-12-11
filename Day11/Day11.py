import numpy as np


def check_seat(seat_map, center, tolerance):
    if center == 'L':
        if np.sum(seat_map == '#') == 0:
            return '#'
        else:
            return 'L'
    elif center == '#':
        if np.sum(seat_map == '#') <= tolerance:
            return '#'
        else:
            return 'L'
    else:
        return '.'


def get_seat_subsection_part1(seat_map, r, c):
    return seat_map[max(r-1, 0):min(r+2, seat_map.shape[0]),
                    max(c-1, 0):min(c+2, seat_map.shape[1])]


def get_seat_subsection_part2(seat_map, r, c):
    seat_subsection = np.full([3, 3], fill_value='.', dtype='str')
    seat_subsection[1, 1] = seat_map[r, c]
    seat_subsection[1, 0] = find_closest(reversed(seat_map[r, :c]))
    seat_subsection[1, 2] = find_closest(seat_map[r, c+1:])
    seat_subsection[0, 1] = find_closest(reversed(seat_map[:r, c]))
    seat_subsection[2, 1] = find_closest(seat_map[r+1:, c])

    diagonal = np.diag(seat_map, k=c-r)
    seat_subsection[0, 0] = find_closest(reversed(diagonal[:min(r, c)]))
    seat_subsection[2, 2] = find_closest(diagonal[min(r, c)+1:])

    c = seat_map.shape[1]-c-1
    diagonal2 = np.diag(np.fliplr(seat_map), k=c-r)
    seat_subsection[0, 2] = find_closest(reversed(diagonal2[:min(r, c)]))
    seat_subsection[2, 0] = find_closest(diagonal2[min(r, c)+1:])
    return seat_subsection


def find_closest(line):
    try:
        return next(i for i in line if i != '.')
    except:
        return '.'


def sit_down(seat_map, seat_fcn, tolerance):
    new_seat_map = seat_map.copy()
    seats_occupied = 0
    for r in range(seat_map.shape[0]):
        for c in range(seat_map.shape[1]):
            if seat_map[r, c] == '.':
                continue
            new_seat_map[r, c] = check_seat(seat_fcn(seat_map, r, c), seat_map[r, c], tolerance)
            if new_seat_map[r, c] == '#':
                seats_occupied += 1
    return seats_occupied, new_seat_map


def main(input, seat_fcn, tolerance):
    seat_map = input.copy()
    seats_occupied = 0
    post_seats_occupied = np.prod(seat_map.shape)
    count = 0

    while seats_occupied != post_seats_occupied:
        seats_occupied = post_seats_occupied
        post_seats_occupied, seat_map = sit_down(seat_map, seat_fcn, tolerance)
        count += 1

    print(f'Seat map stabilized after {count} rounds.',
          f'{post_seats_occupied} seats occupied in steady state.')


if __name__ == '__main__':
    file = 'Day11input.txt'
    with open(file, 'r') as f:
        input = np.array([list(l.strip()) for l in f.readlines()])

    main(input, get_seat_subsection_part1, 4)
    main(input, get_seat_subsection_part2, 5)
