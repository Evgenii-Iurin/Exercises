

# ========= Solution with recursion =========

def bitCounting(digit):
    if digit == 1:
        return digit
    elif digit == 0:
        return digit
    else:
        return bitCounting(digit // 2) + bitCounting(digit % 2)

print(bitCounting(123))



# # ========= The usual solution =========

def bitCounting(digit):
    res = 0;
    while not digit == 0:
        res += digit % 2
        digit = digit // 2
    return res

print(bitCounting(123))
