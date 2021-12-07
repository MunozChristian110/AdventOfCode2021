import submarine

# for solution to part 1 instantiate submarine.Submarine() instead
the_endurance = submarine.SubmarineV2()
moves = {"forward": the_endurance.forward,
         "down": the_endurance.down,
         "up": the_endurance.up}

input = open('input.txt', 'r')

for line in input:
    command = line.split(' ')
    moves[command[0]](int(command[1]))

print(the_endurance.depth)
print(the_endurance.horizontal_pos)

print(the_endurance.depth * the_endurance.horizontal_pos)