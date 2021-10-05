def parse_seatid(id):
    codes = {"F": "0", "B": "1", "L": "0", "R": "1"}
    bin_id = ("").join([codes[s] for s in id[:-1]])
    # could also be done with str.maketrans as reddit told me
    return int(bin_id[:7], 2) * 8 + int(bin_id[7:], 2)


if __name__ == "__main__":
    f = open("Day5input.txt", "r")
    highest_id = 0
    max_id = parse_seatid("BBBBBBBRRR")
    potential_ids = set(range(max_id))
    found_ids = set()
    for line in f:
        seat_id = parse_seatid(line)
        if seat_id > highest_id:
            highest_id = seat_id
        found_ids.add(seat_id)
    print("Highest seat id found: ", highest_id)
    open_seats = potential_ids.difference(found_ids)
    for s in open_seats:
        if s + 1 not in open_seats and s - 1 not in open_seats:
            print("Open Seat in middle ", s)
