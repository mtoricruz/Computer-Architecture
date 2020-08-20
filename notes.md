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

        if len(temp) == 0:
            continue
        if temp[0] == '#':
            continue
        
        try:
            memory[address] = int(temp[0], 2)

        except ValueError:
            print(f'Invalid number: {temp[0]}')
            sys.exit(1)

        address += 1

# Day 3

'SP' = Stack Pointer [Register 7] aka R7

If you run `python3 ls8.py examples/stack.ls8` you should see the output:

```
2
4
1
```
R0: 1           |   FF: 00
R1: 22          |   FE: 00
R2: 5           |   .
.               |   .
.               |   .
R7: F4          |   F4: 00 <---- SP  
                |   F3: 00
                |   F2: 00
                |   F1: 00



# Quick Glossary:

# `PUSH register`

Push the value in the given register on the stack.

1. Decrement the `SP`.
2. Copy the value in the given register to the address pointed to by
   `SP`.

# `POP register`

Pop the value at the top of the stack into the given register.

1. Copy the value from the address pointed to by `SP` to the given register.
2. Increment `SP`.

# `LDI register immediate`

Set the value of a register to an integer.

# `PRN register` pseudo-instruction

Print numeric value stored in the given register.

Print to the console the decimal integer value that is stored in the given
register.

# `MUL registerA registerB` 
*This is an instruction handled by the ALU.*

Multiply the values in two registers together and store the result in registerA.