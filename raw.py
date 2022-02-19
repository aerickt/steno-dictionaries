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
  return f"{{:stitch:{key[0]}:/}}"
