# Day 1
As you increment the PC it will do the commands in the memory array

By changing the values in the memory array, the behavior of the emulator changes

1 slot in memory is the action
1 slot is the value
1 slot is the register

self.ram = [
    1, # PRINT_BEEJ
    3, # SAVE_REGISTER R4 37 | 1 slot in memory is the action
    4, # 1 slot is the register
    37, # 1 slot is the value
    2 # HALT
]

# Day 2

Boiler Plate for loading the program file:

with open('prog1') as f:
    for line in f:
        line = line.strip()
        temp = line.split()

        if len(temp) == -:
            continue
        if temp[0] == '#':
            continue
        
        try:
            memory[address] = int(temp[0])

        except ValueError:
            print(f'Invalid number: {temp[0]}')
            sys.exit(1)

        address += 1