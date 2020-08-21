"""CPU functionality."""

import sys

# filename = sys.argv[1]
# print('SYS PRINT', sys.argv)
SP = 7
class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256
        self.reg = [0] * 8
        self.reg[SP] = 0xF4
        self.pc = 0

        # Flags
        self.E = None
        self.L = None
        self.G = None

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

        # if len(sys.argv) < 2:
        #     print("usage: cpu.py progname")
        #     sys.exit(1)

        with open(filename) as f:
            for line in f:
                line = line.split('#')
                line = line[0].strip()

                if line == '':
                    continue
                try:
                    value = int(line, 2)

                except ValueError:
                    continue

                self.ram[address] = value

                address += 1
        
        # except FileNotFoundError:
        #     print(f'That file does not exist')
        #     sys.exit()


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        if op == "MUL":
            self.reg[reg_a] *= self.reg[reg_b]
        else:
            raise Exception("Unsupported ALU operation")

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
        self.reg[operand_1] = product 

    def add(self, operand_1, operand_2):
        num1 = self.reg[operand_1]
        num2 = self.reg[operand_2]
        total_sum = num1 + num2
        self.reg[operand_1] = total_sum

    def push(self):
        # 1. Decrement the `SP`.
        self.reg[SP] -= 1
        operand_1 = self.ram_read(self.pc + 1)
        # 2. Copy the value in the given register to the address pointed to by `SP`.
        self.ram[self.reg[SP]] = self.reg[operand_1]
    
    def pop(self):
        operand_1 = self.ram_read(self.pc + 1)
        # 1. Copy the value from the address pointed to by `SP` to the given register.
        self.reg[operand_1] = self.ram_read(self.reg[SP])
        # 2. Increment the SP
        self.reg[SP] += 1
    
    def call(self):
        ret_address = self.pc + 2
        reg_index = self.ram_read(self.pc + 1)

        sub_address = self.reg[reg_index]
        # PUSH return_address
        self.reg[SP] -= 1
        self.ram[self.reg[SP]] = ret_address

        # call the subroutine
        self.pc = sub_address

    def ret(self):
        # Pop the return addr off the stack
        return_add = self.reg[SP]
        # set the pc to return_address
        self.pc = self.ram_read(return_add)
        self.reg[SP] += 1

    def comp(self, operand_1, operand_2):
        if self.reg[operand_1] == self.reg[operand_2]:
            self.E = 1
        else:
            self.E = 0

        if self.reg[operand_1] < self.reg[operand_2]:
            self.L = 1
        else:
            self.L = 0

        if self.reg[operand_1] > self.reg[operand_2]:
            self.G = 1
        else:
            self.G = 0

    def jmp(self):
        # storing the address of a given register in operand_1 variable
        operand_1 = self.ram_read(self.pc + 1)
        # Set the `PC` to the address stored in the given register.
        self.pc = self.reg[operand_1]

    def jeq(self):
        if self.E == 1:
            self.jmp()
        else:
            self.pc +=2

    def jne(self):
        if self.E == 0:
            self.jmp()
        else:
            self.pc += 2
        


    def run(self):
        """Run the CPU."""
        HLT = 0b00000001
        LDI = 0b10000010
        PRN = 0b01000111

        MUL = 0b10100010
        ADD = 0b10100000
        
        POP = 0b01000110
        PUSH = 0b01000101
        CALL = 0b01010000
        RET = 0b00010001

        CMP = 0b10100111
        JMP = 0b01010100
        JEQ = 0b01010101
        JNE = 0b01010110

        running = True
        while running:
            # instruction register = MDR(pc)
            ir = self.ram_read(self.pc)
            # self.load(sys.argv[1])
            
            # op 1 = REGISTER
            operand_1 = self.ram_read(self.pc + 1)
            # op 2 = VALUE in REG
            operand_2 = self.ram_read(self.pc + 2)

            if ir == HLT: # HALT
                running = False

            if ir == LDI: # SET_VAL of REGISTER to INT
                self.ldi(operand_1, operand_2)

            if ir == PRN: # PRINT_NUM
                self.prn(self.reg[operand_1])

            if ir == MUL:
                self.mul(operand_1, operand_2)
            
            if ir == ADD:
                self.add(operand_1, operand_2)
            
            if ir == POP:
                self.pop()

            if ir == PUSH:
                self.push()

            if ir == CALL:
                self.call()
            
            if ir == RET:
                self.ret()

            if ir == CMP:
                self.comp(operand_1, operand_2)
            
            if ir == JMP:
                self.jmp()

            if ir == JEQ:
                self.jeq()

            if ir == JNE:
                self.jne()

            instruction_sets_pc = (ir >> 4) & 1
            # check to see if 0b00010000 is False
            if instruction_sets_pc == 0:
                num_of_args = ir >> 6
                size_of_instruction = num_of_args + 1
                self.pc += size_of_instruction




