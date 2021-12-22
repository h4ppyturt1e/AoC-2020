from typing import List, Tuple, Dict

real = "day19.txt"
test = "day19test.txt"


def parse_file(filename: str) -> Tuple[List[str], List[str]]:
    with open(filename) as f:
        data = [line.rstrip() for line in f.readlines()]
        rules, messages = data[:data.index("")], data[data.index(""):] # split by first empty line
        [print(x) for x in data]
    print()
    return rules, messages


def parse_rules(rules: List[str]):
    rule_dict = {}
    for i, rule in enumerate(rules):
        if rule[-1] != "\"":
            item = rule.split(": ")[1].strip("\"")
        else:
            item = rule.split(": ")[1]
        rule_dict[i] = item

    [print(i, ":", rule_dict[i]) for i in rule_dict]

    # keys = [rule for rule in rules if rule[-1] == "\""]
    return


def main():
    rules, messages = parse_file(test)
    parse_rules(rules)


if __name__ == '__main__':
    main()
