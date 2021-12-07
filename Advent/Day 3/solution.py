import copy
input_file = open('input.txt', 'r')

def get_most_or_least_common_bit_in_column(table, column, get_most=True):
    # every row for that column count up the ones and zeroes
    ones = 0
    zeroes = 0
    for row in table:
        # print(row[i])
        if row[column] == "1":
            ones += 1
        else:
            zeroes += 1
    if get_most:
        return 1 if ones >= zeroes else 0
    else:
        return 0 if zeroes <= ones else 1

# user int(x) for x in line.strip if you want them to be integers
# splitting the string might be unnecessary here
table = [[x for x in line.strip()] for line in input_file]

# 2531
# 1564
# 3958484
# iterate through first five column
# for each column go through all rows and see what get the most common and least common bits
most_common_bits = []
least_common_bits = []
# for every column
for i in range(len(table[0])):
    # get the most common bit in the column
    mcb = get_most_or_least_common_bit_in_column(table, i, get_most=True)
    lcb = get_most_or_least_common_bit_in_column(table, i, get_most=False)
    most_common_bits.append(str(mcb))
    # flip most common bit to get least common
    least_common_bits.append(str(lcb))

# From problem: So, the gamma rate is the binary number 10110, or 22 in decimal.
# From problem: The epsilon rate is calculated in a similar way; rather than use the most common bit, the least common bit from each position is used.
# so we treat these strings as binary numbers and get their value in decimal
gamma_rate = int(''.join(most_common_bits),  2)
epslion_rate = int(''.join(least_common_bits), 2)

print(gamma_rate)
print(epslion_rate)
power_consumption = gamma_rate * epslion_rate
print(power_consumption)

def get_oxygen_rating(table):
    # first copy the table since we're going to be modifying it
    report = copy.deepcopy(table)

    # iterate through each column
    for i in range(len(report[0])):
        mcb = get_most_or_least_common_bit_in_column(report, i, get_most=True)
        # print(str(mcb) + ' ', end='')

        # after we get the most common bit, iterate through each row and remove the ones that don't have this bit in that column
        j = 0
        while j < len(report):
            # if the bit in this row matches the most common one, keep it
            if report[j][i] == str(mcb):
                j += 1
                # print("^^^^^^This row was kept^^^^^^")
            else:
                report.pop(j)
                # print(report.pop(j))
                # print('^^^^^This row was removed^^^^^')
    print(report)
    oxygen_generator_rating = int(''.join(report[0]), 2)
    return oxygen_generator_rating

def get_CO2_rating(table):
    # first copy the table since we're going to be modifying it
    report = copy.deepcopy(table)

    # iterate through each column
    # print(len(report[0]))
    for i in range(len(report[0])):
        lcb = get_most_or_least_common_bit_in_column(report, i, get_most=False)

        # after we get the most common bit, iterate through each row and remove the ones that don't have this bit in that column
        j = 0
        while j < len(report):
            # if the bit in this row matches the most common one, keep it
            #print(lcb)
            #print(report[j])
            # input()
            if report[j][i] == str(lcb):
                j += 1
                #print("^^^^^^This row was kept^^^^^^")
            else:
                report.pop(j)
                #print(report.pop(j))
                #print('^^^^^This row was removed^^^^^')
        if len(report) == 1:
            break
    print(report)
    CO2_rating = int(''.join(report[0]), 2)
    return CO2_rating

O2 = get_oxygen_rating(table)
print(O2)
CO2 = get_CO2_rating(table)
print(CO2)
print(O2 * CO2)

