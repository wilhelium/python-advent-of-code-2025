import re

def main():
    start_value = 50
    number_of_zeros = 0

    with open("input.txt", "r") as file:
        current_number = start_value
        for line in file:
            match = re.search('(\\D)(\\d*)',line)
            current_number = new_start_value(int(current_number),match.group(1),int(match.group(2)))
            if current_number == 0:
                number_of_zeros += 1

    print(f'Answer:', number_of_zeros)

def new_start_value(current_postion: int, direction: str, distance: int) -> int:
    match direction:
        case 'R':
            return (current_postion + distance)%100
        case 'L':
            return (current_postion - distance + 100)%100

if __name__ == "__main__":
    main()
