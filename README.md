Compiler Project

A Python-based simulation of a basic compiler that demonstrates core phases of compiler design including lexical analysis, syntax handling, and parsing techniques using a GCD-based input program.
---

Overview

This project was developed as part of a **group assignment** to understand how a compiler processes source code step-by-step. It mimics essential compiler phases such as tokenization, symbol table creation, and parsing using a simplified grammar.
The system takes a structured input program and processes it to analyze correctness and structure.
---

Features

- 🔍 **Lexical Analysis**
  - Breaks input into tokens (keywords, identifiers, operators, numbers)
  - Detects invalid tokens

- 📊 **Symbol Table Generation**
  - Stores unique symbols with their categories

- 📐 **FIRST and FOLLOW Sets**
  - Displays predefined FIRST and FOLLOW sets for grammar understanding

- 🔄 **Shift-Reduce Parsing**
  - Simulates parsing process step-by-step
  - Shows stack, input buffer, and actions (SHIFT / REDUCE)

- ❌ **Error Handling**
  - Stops parsing when invalid tokens are detected
  ---
  
How It Works

1. User enters a program (GCD logic in this case)
2. The compiler performs **tokenization**
3. A **symbol table** is generated
4. FIRST and FOLLOW sets are displayed
5. A **shift-reduce parser** processes the tokens
6. Final result shows whether parsing is successful or not
---

Project Structure
│
├── gcd.py # Main compiler implementation
├── Source input.txt # Sample input program
└── README.md # Project documentation
---

How to Run

1. Install required dependency:
   ```bash
  pip install tabulate
2. Run the program:
    python3 gcd.py
3. Enter the input program manually OR use the sample input provided.

Technologies Used
Python
Regular Expressions (re)
Tabulate Library (for formatted tables)

👥 Team Contribution
This is a group project, and the work was collaboratively completed:
Design of compiler structure and logic
Implementation of lexical analysis and parsing
Testing using GCD-based input program
Documentation and output formatting


🎯 Learning Outcomes
Understanding phases of a compiler
Hands-on experience with tokenization and parsing
Implementation of basic grammar concepts
Exposure to error detection in compilers

📌 Future Enhancements
Add parse tree visualization
Support more complex grammar rules
Build a GUI or web interface
Improve error messages and recovery mechanisms
