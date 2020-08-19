"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256
        self.reg = [0] * 8
        self.pc = 0

    # ram_read takes in the Mem Address Register
    # MAR contains address that's being read/written to
    def ram_read(self, MAR):
        # sets Mem Data Register to the MAR 
        # MDR contains address that was read || the data to write
        MDR = self.ram[MAR]
        # return the value stored there
        return MDR

    # ram_write should accept value to write (MAR) & address to write to (MDR)
    def ram_write(self, MAR, MDR):
        self.ram[MAR] = MDR

    def load(self, filename):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        # program = [
        #     # From print8.ls8
        #     0b10000010, # LDI R0,8
        #     0b00000000, # REGISTER
        #     0b00001000, # VALUE 
        #     0b01000111, # PRN R0
        #     0b00000000,
        #     0b00000001, # HLT
        # ]
        if len(sys.argv) != 2:
            print("usage: cpu.py progname")
            sys.exit(1)

        try:
            with open(path) as f:
                for line in f:
                    line = line.strip()
                    temp = line.split()

                    if len(temp) == 0:
                        continue
                    if temp[0][0] == '#':
                        continue

                    try:
                        self.ram[address] = int(temp[0], 2)

                    except ValueError:
                        print(f'Invalid number: {temp[0]}')
                        sys.exit(1)
                    
                    address += 1
        except FileNotFoundError:
            print(f"Couldn't open {sys.argv[1]}")
            sys.exit(2)

        if address == 0:
            print('Program was empty!')
            sys.exit(3)

        # for instruction in program:
        #     self.ram[address] = instruction
        #     address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    # Set the value of a register to an integer
    #              REG #       VALUE
    def ldi(self, operand_1, operand_2):
        # store a value in a register 
        #   register[register # to store the value in] = the value itself
        self.reg[operand_1] = operand_2

    # Print numeric value stored in the given register
    def prn(self, operand_1):
        print(operand_1)

    def mul(self, operand_1, operand_2):
        num1 = self.reg[operand_1]
        num2 = self.reg[operand_2]
        product = num1 * num2
        print(product)


    def run(self):
        """Run the CPU."""
        HLT = 0b00000001
        LDI = 0b10000010
        PRN = 0b01000111
        MUL = 0b10100010

        running = True
        while running:
            # instruction register = MDR(pc)
            ir = self.ram_read(self.pc)
            operand_1 = self.ram_read(self.pc + 1)
            operand_2 = self.ram_read(self.pc + 2)

            if ir == HLT: # HALT
                running = False

            if ir == LDI: # SET_VAL of REGISTER to INT
                self.ldi(operand_1, operand_2)

            if ir == PRN: # PRINT_NUM
                self.prn(self.reg[operand_1])

            if ir == MUL:
                self.mul(operand_1, operand_2)

            num_of_args = ir >> 6
            size_of_instruction = num_of_args + 1
            self.pc += size_of_instruction


