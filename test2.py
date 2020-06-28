firstName = "Kyle";
Pi = 3.1416;
weight = 3071.2;
print("Hello %s" %firstName);   # %s is for inserting strings
''' Hello
    hows it going
    you can have
    multiple
    comment lines'''
# or you can use an octothrope
print("Pi = %0.2f" %3.1416); # %f is for floating numbers
print("Pi = %i" %Pi);           # %i is for rounding whole numbers
print("%i" %Pi);                
print("{:,.2f}".format(1234567890)) # "{:,*number*}".format(...) is for commas inbetween integers
msg = input("Please type a message: ") # Add input
print(msg + " *Success*")
num = int(input("Please enter a value: "))
print(num)
weight = float(input("Old weight: %.2f. Please enter new:" %weight))
print("%0.2f" %weight)
'''=========================================================
    Output:
        Hello Kyle
        Pi = 3.14
        Pi = 3
        3
        1,234,567,890.00
    ========================================================
    Data types:
        floating numbers
        integers     int()
        strings ("") str("")
        Lists []
    ========================================================
    -> /n will insert a new line for a string
    ========================================================
    Terminology:
    __________________________________________________________
        > Computer: A machine designed to perform operations
        > Program: A set of instructions which specify the
                    the operations of a machine
        > Hardware: A collection of all physical compenents of
                    a computer
        > Software: A collection of all programs that run on
                    the hardware
        > Firmware: Programs that are permanently wired into the
                    hardware
        > Memory: RAM (Random Access Memory)
        > Processing: CPU (Central Processing Unit)
            - Controls I/O operations
            - Consists of:
                ~ CU (Control Unit): Fetch and decode memory
                    instructions
                ~ ALU (Arithmetic Logic Unit): Add, subtract, multiply,
                    or divide
        > OS: A colletion of progrmas which manages the computer
            resources (RAM,CPU,Devices,Files). The OS schedules program
            execution, and directs traffic through the computer. The OS
            is the interface between the user and the hardware.
        > Utilities: Progams that are part of the OS which perform
            functions usch as printing files, copying files, listing files
        > Software Tools: Programs that have been written to perform
        common operations such as word processors, and spreadsheets

    ===============================================================
    Software Terminology:
    _______________________________________________________________

    Source Program = Your Code
    
    Object Program = machine language
    
    High-Level Languages: Easy to write programming languages with
        english-like commands (C++, Python, Java)
        
    Mid-Level Languages: C, it is used as a high-level, but provides
        access to low-level routines, and is often used to define programs
        that are converted to assembly language.
        
    Asembly Language: A low level programming language, similar to machine
        language, butinstructions are written in symbolic statements instead
         of binary(ones and zeroes)
         
    Machine Code/Binary: 1010101010110001110001100111010101000001

    Bug: Anything wrong with your program, that stops it from working

    Debugging: Fixing the bugs

    Compiler: A program which translates a compiled language such as
        C, C++ into assembly language

    Interpreter: A program which translates an interpreted language
        such as Python or Java into machine language

    Assembler: A program which translate Assembly Language into Binary
    
    Compile Time Error: Error (Usually Syntax) During Compilation ";"

    Logic/Execution/Run-Time Error: such as division by zero, may cause
        program to terminate. Even if a program appears to work, one must
        carefully check the results using multiple inputs.
============================================================================
METHODOLOGY OF PROBLEM SOLVING:
____________________________________________________________

 1. STATE THE PROBLEM CLEARLY
 2. DESCRIBE THE INPUT AND OUTPUT INFO
 3. WORK THE PROBLEM BY HAND OR CALCULATOR FO R A SIMPLE SET OF DATA
 4. DEVELOP A SOLUTION AND CONVERT IT TO A COMPUTER PROGRAM
 5. TEST THE SOLUTION WITH A VARIETY OF DATA

=======================================================================

    Modularization: Breaking Down a complex problem into easier to solve
        sub-problems called "Modules"

    Functional Module: A module with a specific function
 
    WHAT IS AN ALGORITHM?
        > An algorithm is a finite number of precisely defined steps for
            solving a problem
        > A "recipe" describing what you will do
        > A step-by-step solution to solve a specific problem

=======================================================================
    INPUT: refers to data sent to the computer (Keyboard, Mouse, etc.)

    OUTPUT: data sent out from the computer (Monitor, printer, etc.)

    Arithmetic: Self-Explanotory / + - *

    CONTROL INSTRUCTION: if, else
        EXAMPLE:
            if(X>0)
                Z = X +5;
            else
                Z = X-5;

    DATA is a collection fo info that can be processed
        ~Numeric
        ~Characters
        ~Strings
        
    Source Code – A set of instructions written in a programming
        language that solves a problem. The program or code includes
        the input statements, computational statements, and output
        statements.

    Documentation -  comments which explain/document the code.

    Compiler – Compiles the source code into machine
        language (ones and zeroes) . After compilation, the program
        must be linked correctly and loaded into memory.  This
        process produces the executable code.

    Linker/Loader – builds the executable module and executes
        it (loads it into memory)

    
'''
