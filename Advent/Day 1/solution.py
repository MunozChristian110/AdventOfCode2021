input = open('input.txt', 'r')
data = [int(i) for i in input]

def get_increases(data):
    # starting depth_increases at -1 because the first one doesnt count
    # but it will increment this variable
    depth_increases = -1
    previous_depth = 0
    for depth in data:
        if depth > previous_depth:
            depth_increases += 1
        previous_depth = depth

    print(depth_increases)

def get_window_sums(data):
    # start with an empty list
    sums = []
    current_index = -1
    for depth in data:
        # append the new element and increase current index
        sums.append(depth)
        current_index += 1
        # next try adding this depth to the previous to elements if possible
        if current_index - 1 >= 0:
            sums[current_index-1] += depth
        if current_index - 2 >= 0:
            sums[current_index-2] += depth
    # remove the last two entries as they won't have a "3 length sliding window"
    sums.pop()
    sums.pop()
    return sums

get_increases(get_window_sums(data))