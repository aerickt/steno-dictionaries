LONGEST_KEY = 2

# binary list of modifiers for first stroke, ctrl = 1, alt = 2, shift = 4, super = 8
modifiers = [
    "TKPWHR",  # no modifier keys, press key alone
    "KHR",  # ctrl
    "THRA",  # alt
    "TKHRA",  # ctrl alt
    "SH",  # shift
    "SKHR",  # ctrl shift
    "STHRA",  # alt shift
    "STKHRA",  # ctrl alt shift
    "KPWR",  # super
    "KPWHR",  # ctrl super
    "TKPWHRA",  # alt super
    "TKPWHRAO",  # ctrl alt super
    "SKPWHR",  # shift super
    "SKPWHRO",  # ctrl shift super
    "STKPWHRA",  # alt shift super
    "STKPWHRAO"  # ctrl alt shift super
]

# list of keys for second stroke
keys = {
    # letters: fingerspelling
    "A": "a",
    "PW": "b",
    "KR": "c",
    "TK": "d",
    "E": "e",
    "SK": "e",  # left hand stroke for E
    "TP": "f",
    "TKPW": "g",
    "H": "h",
    "EU": "i",
    "SKW": "i",  # left hand stroke for I
    "SKWR": "j",
    "K": "k",
    "HR": "l",
    "PH": "m",
    "TPH": "n",
    "O": "o",
    "P": "p",
    "KW": "q",
    "R": "r",
    "S": "s",
    "T": "t",
    "U": "u",
    "WR": "u",  # left hand stroke for U
    "SR": "v",
    "W": "w",
    "KP": "x",
    "KWR": "y",
    "STK": "z",  # simpler stroke for Z
    "STKPW": "z",
    # numbers: AO + binary
    "AO": "0",
    "RAO": "1",
    "WAO": "2",
    "WRAO": "3",
    "KAO": "4",
    "KRAO": "5",
    "KWAO": "6",
    "KWRAO": "7",
    "SAO": "8",
    "SRAO": "9",
    # function keys: F + binary
    "TPR": "f1",
    "TPW": "f2",
    "TPWR": "f3",
    "TKP": "f4",
    "TKPR": "f5",
    "TKPW": "f6",
    "TKPWR": "f7",
    "STP": "f8",
    "STPR": "f9",
    "STPW": "f10",
    "STPWR": "f11",
    "STKP": "f12",
    # numpad keys: asterisk + non-numpad key
    "AO*": "kp_0",
    "RAO*": "kp_1",
    "WAO*": "kp_2",
    "WRAO*": "kp_3",
    "KAO*": "kp_4",
    "KRAO*": "kp_5",
    "KWAO*": "kp_6",
    "KWRAO*": "kp_7",
    "SAO*": "kp_8",
    "SRAO*": "kp_9",
    "PR*": "kp_decimal",  # PeRiod + asterisk
    "PHR*": "kp_add",  # PLus + asterisk
    "PHR": "kp_add",  # PHR isn't used by anything else
    "TKH*": "kp_subtract",  # DasH + asterisk
    "STR*": "kp_multiply",  # STaR + asterisk
    "STR": "kp_multiply",  # STR isn't used by anything else
    "SHR*": "kp_divide",  # SLash + asterisk
    "TPH*": "num_lock",  # Num lock + asterisk
    # symbol keys
    "PR": "period",  # PeRiod
    "KPH": "comma",  # CoMMa
    "SHR": "slash",  # SLash
    "SKHR": "semicolon",  # SemiCoLon
    "KWO": "apostrophe",  # QUOte
    "PWHR": "bracketleft",  # Bracket Left
    "PWR": "bracketright",  # Bracket Right
    "SPWHR": "backslash",  # BackSLash
    "TKH": "minus",  # DasH
    "KWA": "equal",  # eQUAl
    "TKPWR": "grave",  # GRave
    # arrows: PKWR + A (Arrow)
    "PA": "up",
    "WA": "down",
    "KA": "left",
    "RA": "right",
    # navigation keys: arrows + asterisk
    "PA*": "prior",  # page up
    "WA*": "next",  # page down
    "KA*": "home",
    "RA*": "end",
    # misc keys
    "KHR*": "caps_lock",  # Caps Lock
    "SKHR*": "scroll_lock",  # SCroll Lock + asterisk (SKHR taken by semicolon)
    "SP": "space",  # SPace
    "SPWR": "return",  # ENTeR
    "TPW": "tab",  # TaB
    "SPW": "backspace",  # BackSpace
    "TKHR": "delete",  # DeLete
    "SKA": "escape",  # eSCApe
    "STPH": "insert",  # iNSert
    "SKPR": "print",  # SCreen PRint
    "PH*": "menu",  # Menu + asterisk
    # "KPO": "multi_key",  # ComPOse, enable only if you have a compose key
    "TPHO": "" #modifier keys alone
}


def lookup(outline):
    assert len(outline) <= LONGEST_KEY
    str1 = outline[0]
    # KeyError if first stroke is not one of the modifiers
    if str1 not in modifiers:
        raise KeyError
    if len(outline) == 1:
        # above prefixes should do nothing
        return "{#}"

    mods = modifiers.index(str1)  # get index of modifier keys
    # length should be 2
    assert len(outline) == 2
    str2 = outline[1]
    # do nothing if second stroke is SKPH
    if str2 == "SKPH":
        return "{#}"
    if str2 not in keys:
        raise KeyError
    assert str2 in keys
    # get key to press from second stroke
    key = keys.get(str2)

    # add modifiers
    # 8 = super
    if mods & 8 == 8:
        key = "super_l(" + key + ")"
    # 4 = shift
    if mods & 4 == 4:
        key = "shift_l(" + key + ")"
    # 2 = alt
    if mods & 2 == 2:
        key = "alt_l(" + key + ")"
    # 1 = control
    if mods & 1 == 1:
        key = "control_l(" + key + ")"

    # add syntax
    key = "{#" + key + "}"
    # done!
    return key
