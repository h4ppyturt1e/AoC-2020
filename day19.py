from typing import List, Tuple, Dict

real = "day19.txt"
test = "day19test.txt"


def parse_file(filename: str) -> Tuple[List[str], List[str]]:
    with open(filename) as f:
        data = [line.rstrip() for line in f.readlines()]
        rules, messages = data[:data.index("")], data[data.index(""):] # split by first empty line
        # [print(x) for x in data]
    print()
    return rules, messages


def parse_rules(rules: List[str]) -> Dict:
    rule_dict = {}
    for i, rule in enumerate(rules):
        item = rule.split(": ")[1].strip("\"")
        if '|' in item:
            item = item.split('|')
            item = [phrase.split() for phrase in item]
            rule_dict[str(i)] = item
        else:
            rule_dict[str(i)] = item.split()

    [print(i, ":", rule_dict[i]) for i in rule_dict]

    return rule_dict


def get_format(rule_dict, key, result):
    cur_rule = rule_dict[key]
    for sub_rule in cur_rule:
        if len(sub_rule) != 1:
            for rule in sub_rule:




def main():
    rules, messages = parse_file(test)
    rule_dict = parse_rules(rules)
    get_format(rule_dict, '3', "")

if __name__ == '__main__':
    main()
