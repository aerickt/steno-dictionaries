dict = {
    '1': 'S',
    '2': 'T',
    '3': 'P',
    '4': 'H',
    '5': 'A',
    '6': 'F',
    '7': 'P',
    '8': 'L',
    '9': 'T',
    '0': 'O',
    'E': 'E',
    'U': 'U'
}


LONGEST_KEY = 1

def lookup(key):
    if len(key) != 1:
        raise KeyError
    if key[0] == "RA*U":
        return "{plover:end_solo_dict}{^`}"
    if key[0] == "R5*U":
        return "{plover:end_solo_dict}"
    if key[0] == "*":
        return "=undo"
    stroke = key[0]

    if '#' in stroke or any(char.isdigit() for char in stroke):
        for (i, j) in dict.items():
            stroke = stroke.replace(i, j)
        stroke = "#" + stroke

    return f"{{:stitch:{stroke}:/}}"
