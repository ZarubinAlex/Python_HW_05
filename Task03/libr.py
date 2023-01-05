
def encode(data):
    encoding = ''
    prev_char = ''
    count = 1
    if not data: return ''
    for char in data:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encoding += str(count) + prev_char
        return encoding

def code(data):
    coding = ''
    prev_char = ''
    count = ''
    if not data: return ''
    for char in data:
        if char != prev_char:
            if prev_char:
                if prev_char.isdigit():
#                    print(f'{count + prev_char} шт. - {char}')
                    for i in range(int(count + prev_char)):
                        coding += char
            count = ''
            prev_char = char
        else:
            count += prev_char
    else:
        return coding
