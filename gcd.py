from tabulate import tabulate
import re

print("\n===== SIMPLE COMPILER (GCD PROGRAM) =====")

# ================= USER INPUT =================
print("Enter your program (type END on a new line to finish):")
lines = []
while True:
    line = input()
    lines.append(line)
    if line.strip() == "END":
        break

program = "\n".join(lines)

# ================= KEYWORDS =================
keywords = {"BEGIN","END","INTEGER","READ","FOR","PRINT","IF","ENDIF","TO","DO","THEN"}
operators = {":=", "+", ",", "==", "MOD"}

# ================= TOKENIZATION =================
token_table = []
symbol_table = []
symbol_dict = {}
tokens = []
invalid_tokens = []
token_id = 1

# 🔥 capture ALL including invalid
raw_tokens = re.findall(r':=|==|\w+|[^\s\w]', program)

for word in raw_tokens:
    if word in keywords:
        token_type = "KEYWORD"
    elif word in operators:
        token_type = "OPERATOR"
    elif word.isdigit():
        token_type = "NUMBER"
    elif word.isidentifier():
        token_type = "IDENTIFIER"
    else:
        token_type = "INVALID"
        invalid_tokens.append(word)

    tokens.append(word)
    token_table.append([token_type, word, token_id])

    if word not in symbol_dict:
        symbol_dict[word] = token_type
        symbol_table.append([word, token_type])

    token_id += 1

# ================= PRINT TABLES =================
print("\nTOKEN TABLE:")
print(tabulate(token_table, headers=["Type","Lexeme","ID"], tablefmt="fancy_grid"))

print("\nSYMBOL TABLE:")
print(tabulate(symbol_table, headers=["Symbol","Category"], tablefmt="fancy_grid"))

# ================= FIRST =================
print("\nFIRST SET:")
first = [
    ["program","BEGIN"],
    ["stmt_list","INTEGER, IDENTIFIER, FOR, IF, PRINT, READ, ε"],
    ["stmt","INTEGER, IDENTIFIER, FOR, IF, PRINT, READ"],
    ["assignment","IDENTIFIER"],
    ["expr","IDENTIFIER, NUMBER"]
]
print(tabulate(first, headers=["Non-Terminal","FIRST"], tablefmt="fancy_grid"))

# ================= FOLLOW =================
print("\nFOLLOW SET:")
follow = [
    ["program","$"],
    ["stmt_list","END, ENDIF"],
    ["stmt","INTEGER, IDENTIFIER, FOR, IF, PRINT, READ, END"],
    ["assignment","INTEGER, IDENTIFIER, FOR, IF, PRINT, END"],
    ["expr","TO, ==, END, ENDIF"]
]
print(tabulate(follow, headers=["Non-Terminal","FOLLOW"], tablefmt="fancy_grid"))

# ================= SHIFT-REDUCE PARSING =================
print("\nSHIFT-REDUCE PARSING TABLE:\n")

stack = ["$"]
input_tokens = tokens + ["$"]
index = 0
steps = []
step_no = 1
error_flag = False

def trim(lst, width=45):
    text = " ".join(lst)
    return text[:width] + ("..." if len(text) > width else "")

while index < len(input_tokens):

    current = input_tokens[index]

    # ❌ STOP if invalid token
    if current not in keywords and current not in operators \
       and not current.isidentifier() and not current.isdigit() and current != "$":

        action = f"ERROR: invalid token '{current}'"
        steps.append([step_no, trim(stack), trim(input_tokens[index:]), action])
        error_flag = True
        break

    # SHIFT
    stack.append(current)
    action = f"SHIFT '{current}'"
    index += 1

    # ================= REDUCE RULES =================

    # IDENTIFIER := NUMBER → assignment
    if len(stack) >= 3:
        if (stack[-3].isidentifier() and stack[-3] not in keywords and
            stack[-2] == ":=" and stack[-1].isdigit()):
            
            handle = stack[-3:]
            stack = stack[:-3]
            stack.append("assignment")
            action = f"REDUCE {handle} → assignment"

    # NUMBER → expr
    elif len(stack) >= 1:
        if stack[-1].isdigit():
            handle = [stack[-1]]
            stack[-1] = "expr"
            action = f"REDUCE {handle} → expr"

    # IDENTIFIER → expr (not keyword)
    elif len(stack) >= 1:
        if stack[-1].isidentifier() and stack[-1] not in keywords:
            handle = [stack[-1]]
            stack[-1] = "expr"
            action = f"REDUCE {handle} → expr"

    steps.append([
        step_no,
        trim(stack),
        trim(input_tokens[index:]),
        action
    ])
    step_no += 1

# ================= PRINT TABLE =================
print(tabulate(
    steps,
    headers=["Step","Stack","Input Buffer","Action"],
    tablefmt="fancy_grid",
    maxcolwidths=[5,45,45,45]
))

# ================= FINAL RESULT =================
if error_flag:
    print("\n❌ PARSING FAILED (UNSUCCESSFUL PARSING)")
else:
    print("\n✅ PARSING COMPLETED SUCCESSFULLY")