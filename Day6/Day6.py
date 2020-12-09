def get_declarations(line):
    declarations = set()
    for c in line:
        declarations.update(c)
    return declarations


def compare_declarations(lines):
    if len(lines) == 1:
        return get_declarations(lines[0])
    declarations = get_declarations(lines[0])
    for l in lines[1:]:
        declarations = declarations.intersection(declarations, get_declarations(l))
    return declarations


def main():
    with open('Day6input.txt', 'r') as f:
        file = f.read()

    file = file.split('\n\n')

    items_declared = 0
    items_declared_group = 0
    for l in file:
        items_declared += len(get_declarations(l.replace('\n', '')))
        items_declared_group += len(compare_declarations(l.strip('\n').split('\n')))
    print(f'There are {items_declared} items among the passengers')
    print(f'There are {items_declared_group} common items among the passenger groups')


if __name__ == '__main__':
    main()
