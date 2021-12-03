from typing import List


def read_input_file(file_name: str = './input.txt') -> List[str]:
    with open(file_name) as file:
        return [line.rstrip() for line in file.readlines()]


def forward_command(position, units, first_part=True):
    position['horizontal_position'] += units
    if not first_part:
        position['depth'] += position['aim'] * units


def depth_down_command(position, units, first_part=True):
    if first_part:
        position['depth'] += units
    else:
        position['aim'] += units


def depth_up_command(position, units, first_part=True):
    if first_part:
        position['depth'] -= units
    else:
        position['aim'] -= units


command_to_position_map = {
    "forward": forward_command,
    "down": depth_down_command,
    "up": depth_up_command,
}


def dive(first_part=True):
    position = {"horizontal_position": 0, "depth": 0, "aim": 0}
    commands = read_input_file()
    for c in commands:
        command, units = c.split()
        command_to_position_map[command](position, int(units), first_part)
    return position['depth'] * position['horizontal_position']


if __name__ == "__main__":
    print(f'depth * horizontal_position => {dive()}')
    print(
        f'depth * horizontal_position using aim calculation=> {dive(first_part=False)}')
