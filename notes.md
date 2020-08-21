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
   Registers    |   RAM
-----------------------------
R0: 10          |   FF: 00
R1: M2P         |   FE: 00
R2: 5           |   .
.               |   .
.               |   .
R7: F3          |   F4: 00  
                |   F3: R0  <---- SP
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

# `CALL register`

Calls a subroutine (function) at the address stored in the register.

1. The address of the ***instruction*** _directly after_ `CALL` is
   pushed onto the stack. This allows us to return to where we left off when the subroutine finishes executing.
2. The PC is set to the address stored in the given register. We jump to that location in RAM and execute the first instruction in the subroutine. The PC can move forward or backwards from its current location.

# `RET`

Return from subroutine.

Pop the value from the top of the stack and store it in the `PC`.

# `ADD registerA registerB`

Add the value in two registers and store the result in registerA.

# `CMP registerA registerB`

Compare the values in two registers.

* If they are equal, set the Equal `E` flag to 1, otherwise set it to 0.

* If registerA is less than registerB, set the Less-than `L` flag to 1,
  otherwise set it to 0.

* If registerA is greater than registerB, set the Greater-than `G` flag
  to 1, otherwise set it to 0.

# `JMP register`

Jump to the address stored in the given register.

Set the `PC` to the address stored in the given register.

# `JEQ register`

If `equal` flag is set (true), jump to the address stored in the given register.

# `JNE register`

If `E` flag is clear (false, 0), jump to the address stored in the given
register.

