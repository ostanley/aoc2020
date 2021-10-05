def parse_rules(rule_str):
    rule_dict = {}
    rules = rule_str.split("\n")
    for rule in rules:
        limits = rule.split(": ")[1].split(" or ")
        rule_dict[rule.split(": ")[0]] = []
        for limit in limits:
            rule_dict[rule.split(": ")[0]].append([int(x) for x in limit.split("-")])
    return rule_dict


def assign_field(value_assigned, position, position_dict):
    for k, v in position_dict.items():
        if value_assigned in v or position == k:
            v.remove(value_assigned)
    return value_assigned, position_dict


class Ticket:
    def __init__(self, rules_dict, values):
        self.rules = rules_dict
        self.fields = values

    def check_validity(self):
        invalid_sum = 0
        for f in self.fields:
            valid = False
            rules = self.rules.values()
            for rule in rules:
                if f in range(rule[0][0], rule[0][1] + 1) or f in range(
                    rule[1][0], rule[1][1] + 1
                ):
                    valid = True
                    break
            if not valid:
                invalid_sum += f
        return invalid_sum

    def get_field(self, position):
        return self.fields[position]

    def field_in_rule(self, position, rule):
        if (
            rule[0][0] <= self.fields[position] <= rule[0][1]
            or rule[1][0] <= self.fields[position] <= rule[1][1]
        ):
            return True
        else:
            return False


if __name__ == "__main__":
    file = "Day16input.txt"

    with open(file, "r") as f:
        file = f.read()

    rule_dict = parse_rules(file.split("\n\n")[0])
    other_tickets = file.split("\n\n")[2].strip().split("\n")[1:]

    invalid_sum = 0
    ticket_list = []
    count = 0
    for ticket in other_tickets:
        fields = [int(x) for x in ticket.split(",")]
        t = Ticket(rule_dict, fields)
        error = t.check_validity()
        if error == 0:
            count += 1
            ticket_list.append(t)
        invalid_sum += error

    print(f"{invalid_sum} errors found, {len(ticket_list)} tickets valid")

    field_len = len(ticket_list[1].fields)
    position_dict = {}
    for position in range(field_len):
        position_dict[position] = []
        for label, rule in rule_dict.items():
            valid_rule = True
            for ticket in ticket_list:
                if not ticket.field_in_rule(position, rule):
                    valid_rule = False
                    break
            if valid_rule:
                position_dict[position] += [label]

    final_positions = [""] * field_len
    while len(position_dict.keys()) > 0:
        for k, v in position_dict.items():
            if len(v) == 1:
                final_positions[k], position_dict = assign_field(v[0], k, position_dict)
                del position_dict[k]
                break

    your_ticket = [
        int(x) for x in file.split("\n\n")[1].strip().split("\n")[1].split(",")
    ]
    ticket_value = 1
    for i in range(field_len):
        if "departure" in final_positions[i]:
            ticket_value *= your_ticket[i]

    print(f"Final ticket value: {ticket_value}")
