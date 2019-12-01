initial_state = '####....#...######.###.#...##....#.###.#.###.......###.##..##........##..#.#.#..##.##...####.#..##.#'

transitions = {
    '..#..':  '.',
    '#.#.#':  '#',
    '#.###':  '#',
    '.##..':  '.',
    '#.#..':  '#',
    '.#.#.':  '#',
    '.###.':  '#',
    '.####':  '#',
    '##...':  '#',
    '#.##.':  '#',
    '#..##':  '#',
    '....#':  '.',
    '###.#':  '.',
    '#####':  '#',
    '.....':  '.',
    '..#.#':  '.',
    '.#...':  '#',
    '##.#.':  '.',
    '.#.##':  '#',
    '..##.':  '.',
    '#...#':  '.',
    '##.##':  '#',
    '...#.':  '.',
    '#..#.':  '.',
    '..###':  '.',
    '.##.#':  '.',
    '#....':  '.',
    '.#..#':  '#',
    '####.':  '.',
    '...##':  '#',
    '##..#':  '.',
    '###..':  '.',
}
padding_left = 20
padding_right = 110
transitions = {k: v for k, v in transitions.items()}
initial = ['.']*padding_left + list(initial_state) + ['.']*padding_right

state = initial
# print(''.join(state))
for gen in range(100):
    next_chain = []
    for i in range(2, len(initial) - 2):
        slice = state[i-2:i+3]
        transition = transitions[''.join(slice)] if ''.join(
            slice) in transitions else '.'
        next_chain.append(transition)
    state = ['.', '.'] + next_chain + ['.', '.']

# p1
print(sum((i-padding_left) for i, v in enumerate(state) if v == '#'))  # adds up to 3528

# p2
# at around generation ~100 a pattern is formed
# there are 32 flowers and they just move to the right one step per gen
# the count increased by 32 every gen


def calc_gt_100(gen):
    return 3528 + 32*(gen-100)


print(calc_gt_100(50000000000))
