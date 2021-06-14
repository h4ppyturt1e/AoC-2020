from typing import List, Tuple, Dict

real = "day19.txt"
test = "day19test.txt"


def main():
    rules, messages = parse_file(test)
    parse_rules(rules)

def parse_file(filename: str) -> Tuple[List[str], List[str]]:
    with open(filename) as f:
        data = [line.rstrip() for line in f.readlines()]
        rules, messages = data[:data.index("")], data[data.index(""):] # split by first empty line
        [print(x) for x in data]
    return rules, messages 


def parse_rules(rules: List[str]):
    rules = []
    keys = [rule for rule in rules if rule[-1] == "\""]
    
    return






if __name__ == '__main__':
    main()
    