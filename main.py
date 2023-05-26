romen_numeral = {"I": 1, "V": 5, "X": 10, "XL": 40, "L": 50, "XC": 90, "C": 100, "CD": 400, "D": 500, "CM": 900,
                 "M": 1000,"V̅": 5000}

error_number = ["", 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7',
                '8', '9']

max_repeat = 4
repeated_number = {}

# CONVERT ROMEN
def converter(input):
    var = (len(input) - 1)
    if len(input) == 1:
        if input in romen_numeral.keys():
            print(romen_numeral[input])
    else:
        a = 0
        a = a + romen_numeral[input[var]]
        while var > 0:
            var = var - 1
            if romen_numeral[input[var]] >= romen_numeral[input[var + 1]]:
                a = a + romen_numeral[input[var]]
            else:
                a = a - romen_numeral[input[var]]
        return a

# CHECK ROMEN NUMERAL
def check_number(input):
    if romen_input in error_number:
        return False
    for num in romen_input:
        if num not in repeated_number:
            repeated_number[num] = 1
        else:
            repeated_number[num] += 1
        if repeated_number[num] > max_repeat:
            return False
    return True

# START TO CONVERT
while True:
    romen_input = input("Romen Numeral: ")
    if check_number(romen_input):
        try:
            result = converter(romen_input)
            print(result)
        except:
            print("Please try again!")
            continue
    else:
        print("Please check Romen numeral!")