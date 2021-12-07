# Submarine with functions that follows the rules as described in part 1 of the problem
# added backward function in case the second part would have needed it (for future proofing the class)
class Submarine:
    def __init__(self, starting_horizontal_pos=0, starting_depth=0,):
        self.horizontal_pos = starting_horizontal_pos
        self.depth = starting_depth
        self.initial_position = [starting_horizontal_pos, starting_depth]

    def forward(self, distance):
        self.horizontal_pos += distance

    def backward(self, distance):
        self.forward(-distance)

    def up(self, distance):
        self.depth -= distance
        if self.depth < 0:
            self.depth = 0

    def down(self, distance):
        self.depth += distance

# Submarine with functions as described in part 2 of the problem
class SubmarineV2:
    def __init__(self, starting_horizontal_pos=0, starting_depth=0,):
        self.horizontal_pos = starting_horizontal_pos
        self.depth = starting_depth
        self.initial_position = [starting_horizontal_pos, starting_depth]
        self.aim = 0

    def forward(self, distance):
        self.horizontal_pos += distance
        self.depth += self.aim * distance

    def backward(self, distance):
        self.forward(-distance)

    def up(self, adjustment):
        self.aim -= adjustment

    def down(self, adjustment):
        self.aim += adjustment