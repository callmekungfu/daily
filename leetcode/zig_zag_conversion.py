def convert(s: str, numRows: int) -> str:
    if numRows == 1:
        return s
    rows = []
    current_row = 0
    going_down = False

    for i in range(0, min(numRows, len(s))):
        rows.append("")

    for char in s:
        rows[current_row] += char
        if (current_row == 0 or current_row == numRows - 1):
            going_down = not going_down
        add = -1
        if (going_down):
            add = 1
        current_row += add
    
    result = ""
    for row in rows:
        result += row
    return result
while True:
    print(convert(input("str: "), int(input("row:"))))
