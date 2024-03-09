# Jeff's phrasing dictionary for Plover.

# See README.md for instructions on how the system works.

import re

LONGEST_KEY = 1

PARTS_MATCHER = re.compile(
    r'(S?T?K?P?W?H?R?)(A?O?)-?(\*?)(E?U?)(F?)(R?P?B?L?G?T?S?D?Z?)'
)

TO_BE = {
    "present": {
        None: " are",
        "root": " be",
        "1ps": " am",
        "3ps": " is",
        "present-participle": " being",
        "past-participle": " been",
    },
    "past": {
        None: " were",
        "root": " be",
        "1ps": " was",
        "3ps": " was",
        "present-participle": " being",
        "past-participle": " been",
    },
}

TO_HAVE = {
    "present": {
        None: " have",
        "3ps": " has",
        "present-participle": " having",
        "past-participle": " had",
    },
    "past": {
        "root": " have",
        None: " had",
        "present-participle": " having",
        "past-participle": " had",
    }
}

THERE_SUFFIXES = {
    "": True,
    "D": True,                                                # Past tense
    "B": True, "BT": True, "BD": True, "BTD": True,           # Be (a)
    "BG": True, "BGD": True,                                  # Come
    "G": True, "GD": True,                                    # Go
    "PZ": True, "PDZ": True,                                  # Happen
    "T": True, "TD": True, "TS": True, "TSDZ": True,          # Have (to)
    "LZ": True, "LZD": True,                                  # Live
    "PL": True, "PLT": True, "PLD": True, "PLTD": True,       # May (have)
    "PBLGS": True, "PBLGTS": True,                            # Must (have)
    "PBLGSZ": True, "PBLGTSDZ": True,                         # Just
    "RPG": True, "RPGD": True, "RPGT": True, "RPGTD": True,   # Need (to)
    "RLG": True, "RLGD": True,                                # Really
    "PLS": True, "PLSZ": True, "PLTS": True, "PLTSDZ": True,  # Seem (to)
    "Z": True, "DZ": True, "TZ": True, "TDZ": True,           # Use (to)
}

NON_PHRASE_STROKES = {
    "STHR": True,        # "is there"
    "STHRET": True,      # "stiletto"
    "STHREUPLT": True,   # "stimulate"
    "STPHREFPLT": True,  # "investment in"

    "SKPUR": True,       # "and you're" -- rather than "and you run"
    "SKPUL": True,       # "and you'll" -- rather than "and you look"
    "SKPEUT": True,      # "and it"     -- rather than "and I have"

    "SKP*": True,        # {&&}
}

STARTERS = {
    # Map of stroke -> word, verb-form, valid enders
    #  * 'b' for blank
    #  * '1p', '2p', '3p' for 1st, 2nd, 3rd person
    #  * 'p/s' for plural/singular
    "SWR": ("I", "1ps", None),
    "KPWR": ("you", "2p", None),
    "KWHR": ("he", "3ps", None),
    "SKWHR": ("she", "3ps", None),
    "KPWH": ("it", "3ps", None),
    "TWR": ("we", "1pp", None),
    "TWH": ("they", "3pp", None),
    "STKH": ("this", "3ps", None),
    "STWH": ("that", "3ps", None),
    "STHR": ("there", "3ps", THERE_SUFFIXES),
    "STPHR": ("there", "3pp", THERE_SUFFIXES),
    "STKPWHR": ("", "b3ps", None),
    "STWR": ("", "b3pp", None),
}

SIMPLE_STARTERS = {
    "STHA": (" that", None),
    "STPA": (" if", None),
    "SWH": (" when", None),
    "SWHA": (" what", None),
    "SWHR": (" where", None),
    "SWHO": (" who", None),
    "SWHAO": (" why", None),

    "SPWH": (" but", None),
    "STPR": (" for", None),

    # Remove the entry below if you don't want "and" phrases.
    "SKP": (" and", None),
}

SIMPLE_PRONOUNS = {
    "E": ("he", "3ps", None),
    "*E": ("she", "3ps", None),
    "U": ("you", "2p", None),
    "*U": ("they", "3pp", None),
    "EU": ("I", "1ps", None),
    "*EU": ("we", "1pp", None),
    "*": ("it", "3ps", None),
}

SIMPLE_STRUCTURES = {
    "": ("* !", True, None),
    "F": ({tense: {form: "* !" + TO_HAVE[tense][form] for form in TO_HAVE[tense]} for tense in TO_HAVE}, True, "past-participle"),
}

MIDDLES = {
    # Map of stroke -> (map[tense][verb-form](string, verb-form)
    "": {"present": {None: (" do", "root"), "3ps": (" does", "root")}, "past": (" did", "root")},
    "*": {"present": {None: (" don't", "root"), "3ps": (" doesn't", "root")}, "past": (" didn't", "root")},
    "A": {"present": (" can", "root"), "past": (" could", "root")},
    "A*": {"present": (" can't", "root"), "past": (" couldn't", "root")},
    "O": {"present": (" shall", "root"), "past": (" should", "root")},
    "O*": {"present": (" shall not", "root"), "past": (" shouldn't", "root")},
    "AO": {"present": (" will", "root"), "past": (" would", "root")},
    "AO*": {"present": (" won't", "root"), "past": (" wouldn't", "root")},
}

# `!` represents the starter
# `*` represents the middle
#
# (format, use-middle-verb-form, updated-verb-form)
STRUCTURE_EXCEPTIONS = {
    "": ("!", False, None),

    # To make reverse look-ups work correctly, longer results must be listed first

    "*E": ({"present": {None: "! aren't", "1ps": "! am not", "3ps": "! isn't"}, "past": {None: "! weren't", "1ps": "! wasn't", "3ps": "! wasn't"}}, False, "present-participle"),
    "E": ({"present": {None: "! are", "1ps": "! am", "3ps": "! is"}, "past": {None: "! were", "1ps": "! was", "3ps": "! was"}}, False, "present-participle"),
    "*F": ({"present": {None: "! haven't", "3ps": "! hasn't"}, "past": "! hadn't"}, False, "past-participle"),
    "F": ({"present": {None: "! have", "3ps": "! has"}, "past": "! had"}, False, "past-participle"),
    "*EF": ({"present": {None: "! haven't been", "3ps": "! hasn't been"}, "past": "! hadn't been"}, False, "present-participle"),
    "EF": ({"present": {None: "! have been", "3ps": "! has been"}, "past": "! had been"}, False, "present-participle"),

    # The following alternate definitions cause phrases to use contracted forms, e.g.:
    #
    # * `I am going to` -> `I'm going to`
    # * `I have gone to` -> `I've gone to`
    #
    # To use contracted forms, uncomment out the next 6 definitions.
    #
    # "*E": ({"present": {None: "! are not", "1ps": "!'m not", "2p": "!'re not", "3ps": "! isn't", "1pp": "!'re not", "3pp": "!'re not", "b3pp": "! are not"}, "past": {None: "! weren't", "1ps": "! wasn't", "3ps": "! wasn't"}}, False, "present-participle"),
    # "E": ({"present": {None: "! are", "1ps": "!'m", "2p": "!'re", "3ps": "!'s", "b3ps": "! is", "1pp": "!'re", "3pp": "!'re", "b3pp": "! are"}, "past": {None: "! were", "1ps": "! was", "3ps": "! was"}}, False, "present-participle"),
    # "*F": ({"present": {None: "! haven't", "3ps": "! hasn't"}, "past": "! hadn't"}, False, "past-participle"),
    # "F": ({"present": {None: "! have", "1ps": "!'ve", "2p": "!'ve", "3ps": "!'s", "b3ps": "! has", "1pp": "!'ve", "3pp": "!'ve", "b3pp": "! have"}, "past": {None: "! had", "1ps": "!'d", "2p": "!'d", "3ps": "!'d", "1pp": "!'d", "3pp": "!'d", "b3pp": "! had"}}, False, "past-participle"),
    # "*EF": ({"present": {None: "! haven't been", "3ps": "! hasn't been"}, "past": "! hadn't been"}, False, "present-participle"),
    # "EF": ({"present": {None: "! have been", "1ps": "!'ve been", "2p": "!'ve been", "3ps": "!'s been", "b3ps": "! has been", "1pp": "!'ve been", "3pp": "!'ve been", "b3pp": "! have been"}, "past": {None: "! had been", "1ps": "!'d been", "2p": "!'d been", "3ps": "!'d been", "b3ps": "! had been", "1pp": "!'d been", "3pp": "!'d been", "b3pp": "! had been"}}, False, "present-participle"),

    # This is an old system that used 'U' for inverting have/be.
    # It's been commented out as the never/still/just
    # "*EU": ({"present": {None: " aren't !", "1ps": " am ! not", "3ps": " isn't !"}, "past": {None: " weren't !", "1ps": " wasn't !", "3ps": " wasn't !"}}, False, "present-participle"),
    # "EU": ({"present": {None: " are !", "1ps": " am !", "3ps": " is !"}, "past": {None: " were !", "1ps": " was !", "3ps": " was !"}}, False, "present-participle"),
    # "*UF": ({"present": {None: " haven't !", "3ps": " hasn't !"}, "past": " hadn't !"}, False, "past-participle"),
    # "UF": ({"present": {None: " have !", "3ps": " has !"}, "past": " had !"}, False, "past-participle"),
    # "*EUF": ({"present": {None: " haven't ! been", "3ps": " hasn't ! been"}, "past": " hadn't ! been"}, False, "present-participle"),
    # "EUF": ({"present": {None: " have ! been", "3ps": " has ! been"}, "past": " had ! been"}, False, "present-participle"),

    "EU": ("! still", False, None),
    "EUF": ("! never", False, None),
    "UF": ("! just", False, None),

    # Special cases for empty starters.
    # - infinitive forms.
    "STWRU": ("to", False, "root"),
    "STWR*U": ("not to", False, "root"),
    "STKPWHRU": ("to", False, "root"),
    "STKPWHR*U": ("not to", False, "root"),
}

ALWAYS = {None: "* !", "b3ps-root": "* always", "b3pp-root": "* always"}

STRUCTURES = {
    "": ("!*", True, None),
    "*": ("!*", True, None),

    "*E": ({tense: {form: "!*" + TO_BE[tense][form] for form in TO_BE[tense]} for tense in TO_BE}, True, "present-participle"),
    "E": ({tense: {form: "!*" + TO_BE[tense][form] for form in TO_BE[tense]} for tense in TO_BE}, True, "present-participle"),
    "*EF": ({tense: {form: "!*" + TO_HAVE[tense][form] + " been" for form in TO_HAVE[tense]} for tense in TO_HAVE}, True, "present-participle"),
    "EF": ({tense: {form: "!*" + TO_HAVE[tense][form] + " been" for form in TO_HAVE[tense]} for tense in TO_HAVE}, True, "present-participle"),
    "*F": ({tense: {form: "!*" + TO_HAVE[tense][form] for form in TO_HAVE[tense]} for tense in TO_HAVE}, True, "past-participle"),
    "F": ({tense: {form: "!*" + TO_HAVE[tense][form] for form in TO_HAVE[tense]} for tense in TO_HAVE}, True, "past-participle"),

    "*EU": ("! still*", True, None),
    "EU": ("!* still", True, None),
    "*EUF": ("!* even", True, None),
    "EUF": ("!* never", True, None),

    "*U": ({"present": ALWAYS, "past": ALWAYS}, True, None),
    "U": ({"present": ALWAYS, "past": ALWAYS}, True, None),
    "*UF": ("! just*", True, None),
    "UF": ("!* just", True, None),
} 

ENDERS = {
    "": ("present", ""),
    "D": ("past", ""),

    # RB: To ask
    "RB": ("present", {None: " ask", "3ps": " asks", "present-participle": " asking", "past-participle": " asked"}),
    "RBD": ("past", {None: " asked", "root": " ask", "present-participle": " asking", "past-participle": " asked"}),

    # B: To be (a)
    "B": ("present", TO_BE["present"]),
    "BT": ("present", {key: TO_BE["present"][key] + " a" for key in TO_BE["present"]}),
    "BD": ("past", TO_BE["past"]),
    "BTD": ("past", {key: TO_BE["past"][key] + " a" for key in TO_BE["past"]}),

    # RPBG: To become (a)
    "RPBG": ("present", {None: " become", "3ps": " becomes", "present-participle": " becoming", "past-participle": " become"}),
    "RPBGT": ("present", {None: " become a", "3ps": " becomes a", "present-participle": " becoming a", "past-participle": " become a"}),
    "RPBGD": ("past", {None: " became", "root": " become", "present-participle": " becoming", "past-participle": " become"}),
    "RPBGTD": ("past", {None: " became a", "root": " become a", "present-participle": " becoming a", "past-participle": " become a"}),

    # BL - To believe (that)
    "BL": ("present", {None: " believe", "3ps": " believes", "present-participle": " believing", "past-participle": " believed"}),
    "BLT": ("present", {None: " believe that", "3ps": " believes that", "present-participle": " believing that", "past-participle": " believed that"}),
    "BLD": ("past", {None: " believed", "root": " believe", "present-participle": " believing", "past-participle": " believed"}),
    "BLTD": ("past", {None: " believed that", "root": " believe that", "present-participle": " believing that", "past-participle": " believed that"}),

    # RBLG - To call
    "RBLG": ("present", {None: " call", "3ps": " calls", "present-participle": " calling", "past-participle": " called"}),
    "RBLGD": ("past", {None: " called", "root": " call", "present-participle": " calling", "past-participle": " called"}),

    # BGS - Can - Auxiliary verb
    # These do not combine naturally with middle/structures.
    "BGS": ("present", " can"),
    "BGSZ": ("past", " could"),

    # RZ - To care
    "RZ": ("present", {None: " care", "3ps": " cares", "present-participle": " caring", "past-participle": " cared"}),
    "RDZ": ("past", {None: " cared", "root": " care", "present-participle": " caring", "past-participle": " cared"}),

    # PBGZ - To change
    "PBGZ": ("present", {None: " change", "3ps": " changes", "present-participle": " changing", "past-participle": " changed"}),
    "PBGDZ": ("past", {None: " changed", "root": " change", "present-participle": " changing", "past-participle": " changed"}),

    # BG - To come (to)
    "BG": ("present", {None: " come", "3ps": " comes", "present-participle": " coming", "past-participle": " come"}),
    "BGT": ("present", {None: " come to", "3ps": " comes to", "present-participle": " coming to", "past-participle": " come to"}),
    "BGD": ("past", {None: " came", "root": " come", "present-participle": " coming", "past-participle": " come"}),
    "BGTD": ("past", {None: " came to", "root": " come to", "present-participle": " coming to", "past-participle": " come to"}),

    # RBGZ - To consider
    "RBGZ": ("present", {None: " consider", "3ps": " considers", "present-participle": " considering", "past-participle": " considered"}),
    "RBGDZ": ("past", {None: " considered", "root": " consider", "present-participle": " considering", "past-participle": " considered"}),

    # RP - To do (it)
    "RP": ("present", {None: " do", "3ps": " does", "present-participle": " doing", "past-participle": " done"}),
    "RPT": ("present", {None: " do it", "3ps": " does it", "present-participle": " doing it", "past-participle": " done it"}),
    "RPD": ("past", {None: " did", "root": " do", "present-participle": " doing", "past-participle": " done"}),
    "RPTD": ("past", {None: " did it", "root": " do it", "present-participle": " doing it", "past-participle": " done it"}),

    # PGS: To expect (that)
    "PGS": ("present", {None: " expect", "3ps": " expects", "present-participle": " expecting", "past-participle": " expected"}),
    "PGTS": ("present", {None: " expect that", "3ps": " expects that", "present-participle": " expecting that", "past-participle": " expected that"}),
    "PGSZ": ("past", {None: " expected", "root": " expect", "present-participle": " expecting", "past-participle": " expected"}),
    "PGTSDZ": ("past", {None: " expected that", "root": " expect that", "present-participle": " expecting that", "past-participle": " expected that"}),

    # LT - To feel (like)
    "LT": ("present", {None: " feel", "3ps": " feels", "present-participle": " feeling", "past-participle": " felt"}),
    "LTS": ("present", {None: " feel like", "3ps": " feels like", "present-participle": " feeling like", "past-participle": " felt like"}),
    "LTD": ("past", {None: " felt", "root": " feel", "present-participle": " feeling", "past-participle": " felt"}),
    "LTSDZ": ("past", {None: " felt like", "root": " feel like", "present-participle": " feeling like", "past-participle": " felt like"}),

    # PBLG - To find (that)
    "PBLG": ("present", {None: " find", "3ps": " finds", "present-participle": " finding", "past-participle": " found"}),
    "PBLGT": ("present", {None: " find that", "3ps": " finds that", "present-participle": " finding that", "past-participle": " found that"}),
    "PBLGD": ("past", {None: " found", "root": " find", "present-participle": " finding", "past-participle": " found"}),
    "PBLGTD": ("past", {None: " found that", "root": " find that", "present-participle": " finding that", "past-participle": " found that"}),

    # RG: To forget (to)
    "RG": ("present", {None: " forget", "3ps": " forgets", "present-participle": " forgetting", "past-participle": " forgotten"}),
    "RGT": ("present", {None: " forget to", "3ps": " forgets to", "present-participle": " forgetting to", "past-participle": " forgotten to"}),
    "RGD": ("past", {None: " forgot", "root": " forget", "present-participle": " forgetting", "past-participle": " forgotten"}),
    "RGTD": ("past", {None: " forgot to", "root": " forget to", "present-participle": " forgetting to", "past-participle": " forgotten to"}),

    # GS: To get (to)
    "GS": ("present", {None: " get", "3ps": " gets", "present-participle": " getting", "past-participle": " got"}),
    "GTS": ("present", {None: " get to", "3ps": " gets to", "present-participle": " getting to", "past-participle": " got to"}),
    "GSZ": ("past", {None: " got", "root": " get", "present-participle": " getting", "past-participle": " got"}),
    "GTSDZ": ("past", {None: " got to", "root": " get to", "present-participle": " getting to", "past-participle": " got to"}),

    # GZ: To give
    "GZ": ("present", {None: " give", "3ps": " gives", "present-participle": " giving", "past-participle": " given"}),
    "GDZ": ("past", {None: " gave", "root": " give", "present-participle": " giving", "past-participle": " given"}),

    # G: To go (to)
    "G": ("present", {None: " go", "3ps": " goes", "present-participle": " going", "past-participle": " gone"}),
    "GT": ("present", {None: " go to", "3ps": " goes to", "present-participle": " going to", "past-participle": " gone to"}),
    "GD": ("past", {None: " went", "root": " go", "present-participle": " going", "past-participle": " gone"}),
    "GTD": ("past", {None: " went to", "root": " go to", "present-participle": " going to", "past-participle": " gone to"}),

    # T - To have (to)
    "T": ("present", {None: " have", "3ps": " has", "present-participle": " having", "past-participle": " had"}),
    "TS": ("present", {None: " have to", "3ps": " has to", "present-participle": " having to", "past-participle": " had to"}),
    "TD": ("past", {None: " had", "root": " have", "present-participle": " having", "past-participle": " had"}),
    "TSDZ": ("past", {None: " had to", "root": " have to", "present-participle": " having to", "past-participle": " had to"}),

    # PZ - To happen
    "PZ": ("present", {None: " happen", "3ps": " happens", "present-participle": " happening", "past-participle": " happened"}),
    "PDZ": ("past", {None: " happened", "root": " happen", "present-participle": " happening", "past-participle": " happened"}),

    # PG - To hear (that)
    "PG": ("present", {None: " hear", "3ps": " hears", "present-participle": " hearing", "past-participle": " heard"}),
    "PGT": ("present", {None: " hear that", "3ps": " hears that", "present-participle": " hearing that", "past-participle": " heard that"}),
    "PGD": ("past", {None: " heard", "root": " hear", "present-participle": " hearing", "past-participle": " heard"}),
    "PGTD": ("past", {None: " heard that", "root": " hear that", "present-participle": " hearing that", "past-participle": " heard that"}),

    # RPS - To hope (to)
    "RPS": ("present", {None: " hope", "3ps": " hopes", "present-participle": " hoping", "past-participle": " hoped"}),
    "RPTS": ("present", {None: " hope to", "3ps": " hopes to", "present-participle": " hoping to", "past-participle": " hoped to"}),
    "RPSZ": ("past", {None: " hoped", "root": " hope", "present-participle": " hoping", "past-participle": " hoped"}),
    "RPTSDZ": ("past", {None: " hoped to", "root": " hope to", "present-participle": " hoping to", "past-participle": " hoped to"}),

    # PLG - To imagine (that)
    "PLG": ("present", {None: " imagine", "3ps": " imagines", "present-participle": " imagining", "past-participle": " imagined"}),
    "PLGT": ("present", {None: " imagine that", "3ps": " imagines that", "present-participle": " imagining that", "past-participle": " imagined that"}),
    "PLGD": ("past", {None: " imagined", "root": " imagine", "present-participle": " imagining", "past-participle": " imagined"}),
    "PLGTD": ("past", {None: " imagined that", "root": " imagine that", "present-participle": " imagining that", "past-participle": " imagined that"}),

    # PBLGSZ - Just
    "PBLGSZ": ("present", " just"),
    "PBLGTSDZ": ("past", " just"),

    # PBGS - To keep
    "PBGS": ("present", {None: " keep", "3ps": " keeps", "present-participle": " keeping", "past-participle": " kept"}),
    "PBGSZ": ("past", {None: " kept", "root": " keep", "present-participle": " keeping", "past-participle": " kept"}),

    # PB: To know (that)
    "PB": ("present", {None: " know", "3ps": " knows", "present-participle": " knowing", "past-participle": " known"}),
    "PBT": ("present", {None: " know that", "3ps": " knows that", "present-participle": " knowing that", "past-participle": " known that"}),
    "PBD": ("past", {None: " knew", "root": " know", "present-participle": " knowing", "past-participle": " known"}),
    "PBTD": ("past", {None: " knew that", "root": " know that", "present-participle": " knowing that", "past-participle": " known that"}),

    # RPBS - To learn (to)
    "RPBS": ("present", {None: " learn", "3ps": " learns", "present-participle": " learning", "past-participle": " learned"}),
    "RPBTS": ("present", {None: " learn to", "3ps": " learns to", "present-participle": " learning to", "past-participle": " learned to"}),
    "RPBSZ": ("past", {None: " learned", "root": " learn", "present-participle": " learning", "past-participle": " learned"}),
    "RPBTSDZ": ("past", {None: " learned to", "root": " learn to", "present-participle": " learning to", "past-participle": " learned to"}),

    # LGZ - To leave
    "LGZ": ("present", {None: " leave", "3ps": " leaves", "present-participle": " leaving", "past-participle": " left"}),
    "LGDZ": ("past", {None: " left", "root": " leave", "present-participle": " leaving", "past-participle": " left"}),

    # LS - To let
    "LS": ("present", {None: " let", "3ps": " lets", "present-participle": " letting", "past-participle": " let"}),
    "LSZ": ("past", {None: " let", "present-participle": " letting", "past-participle": " let"}),

    # BLG - To like (to)
    "BLG": ("present", {None: " like", "3ps": " likes", "present-participle": " liking", "past-participle": " liked"}),
    "BLGT": ("present", {None: " like to", "3ps": " likes to", "present-participle": " liking to", "past-participle": " liked to"}),
    "BLGD": ("past", {None: " liked", "root": " like", "present-participle": " liking", "past-participle": " liked"}),
    "BLGTD": ("past", {None: " liked to", "root": " like to", "present-participle": " liking to", "past-participle": " liked to"}),

    # LZ - To live
    "LZ": ("present", {None: " live", "3ps": " lives", "present-participle": " living", "past-participle": " lived"}),
    "LDZ": ("past", {None: " lived", "root": " live", "present-participle": " living", "past-participle": " lived"}),

    # L - To look
    "L": ("present", {None: " look", "3ps": " looks", "present-participle": " looking", "past-participle": " looked"}),
    "LD": ("past", {None: " looked", "root": " look", "present-participle": " looking", "past-participle": " looked"}),

    # LG - To love (to)
    "LG": ("present", {None: " love", "3ps": " loves", "present-participle": " loving", "past-participle": " loved"}),
    "LGT": ("present", {None: " love to", "3ps": " loves to", "present-participle": " loving to", "past-participle": " loved to"}),
    "LGD": ("past", {None: " loved", "root": " love", "present-participle": " loving", "past-participle": " loved"}),
    "LGTD": ("past", {None: " loved to", "root": " love to", "present-participle": " loving to", "past-participle": " loved to"}),

    # RPBL - To make (a)
    "RPBL": ("present", {None: " make", "3ps": " makes", "present-participle": " making", "past-participle": " made"}),
    "RPBLT": ("present", {None: " make a", "3ps": " makes a", "present-participle": " making a", "past-participle": " made a"}),
    "RPBLD": ("past", {None: " made", "root": " make", "present-participle": " making", "past-participle": " made"}),
    "RPBLTD": ("past", {None: " made a", "root": " make a", "present-participle": " making a", "past-participle": " made a"}),

    # PL - Auxiliary verb may (be)
    # These do not combine naturally with middle/structures.
    "PL": ("present", " may"),
    "PLT": ("present", " may be"),
    "PLD": ("past", " might"),
    "PLTD": ("past", " might be"),

    # PBL - To mean (to)
    "PBL": ("present", {None: " mean", "3ps": " means", "present-participle": " meaning", "past-participle": " meant"}),
    "PBLT": ("present", {None: " mean to", "3ps": " means to", "present-participle": " meaning to", "past-participle": " meant to"}),
    "PBLD": ("past", {None: " meant", "root": " mean", "present-participle": " meaning", "past-participle": " meant"}),
    "PBLTD": ("past", {None: " meant to", "root": " mean to", "present-participle": " meaning to", "past-participle": " meant to"}),

    # PBLS - To mind
    "PBLS": ("present", {None: " mind", "3ps": " minds", "present-participle": " minding", "past-participle": " minded"}),
    "PBLSZ": ("past", {None: " minded", "root": " mind", "present-participle": " minding", "past-participle": " minded"}),

    # PLZ - To move
    "PLZ": ("present", {None: " move", "3ps": " moves", "present-participle": " moving", "past-participle": " moved"}),
    "PLDZ": ("past", {None: " moved", "root": " move", "present-participle": " moving", "past-participle": " moved"}),

    # PBLGS - Auxiliary verb must (be)
    # These do not combine naturally with middle/structures.
    "PBLGS": ("present", " must"),
    "PBLGTS": ("present", " must be"),

    # RPG: To need (to)
    "RPG": ("present", {None: " need", "3ps": " needs", "present-participle": " needing", "past-participle": " needed"}),
    "RPGT": ("present", {None: " need to", "3ps": " needs to", "present-participle": " needing to", "past-participle": " needed to"}),
    "RPGD": ("past", {None: " needed", "root": " need", "present-participle": " needing", "past-participle": " needed"}),
    "RPGTD": ("past", {None: " needed to", "root": " need to", "present-participle": " needing to", "past-participle": " needed to"}),

    # PS: To put (it)
    "PS": ("present", {None: " put", "3ps": " puts", "present-participle": " putting", "past-participle": " put"}),
    "PTS": ("present", {None: " put it", "3ps": " puts it", "present-participle": " putting it", "past-participle": " put it"}),
    "PSZ": ("past", {None: " put", "root": " put", "present-participle": " putting", "past-participle": " put"}),
    "PTSDZ": ("past", {None: " put it", "root": " put it", "present-participle": " putting it", "past-participle": " put it"}),

    # RS - To read
    "RS": ("present", {None: " read", "3ps": " reads", "present-participle": " reading", "past-participle": " read"}),
    "RSZ": ("past", {None: " read", "root": " read", "present-participle": " reading", "past-participle": " read"}),

    # RLG - really
    "RLG": ("present", " really"),
    "RLGD": ("past", " really"),

    # RL - To recall
    "RL": ("present", {None: " recall", "3ps": " recalls", "present-participle": " recalling", "past-participle": " recalled"}),
    "RLD": ("past", {None: " recalled", "root": " recall", "present-participle": " recalling", "past-participle": " recalled"}),

    # RLS - To realize (that)
    "RLS": ("present", {None: " realize", "3ps": " realizes", "present-participle": " realizing", "past-participle": " realized"}),
    "RLTS": ("present", {None: " realize that", "3ps": " realizes that", "present-participle": " realizing that", "past-participle": " realized that"}),
    "RLSZ": ("past", {None: " realized", "root": " realize", "present-participle": " realizing", "past-participle": " realized"}),
    "RLTSDZ": ("past", {None: " realized that", "root": " realize that", "present-participle": " realizing that", "past-participle": " realized that"}),

    # RPL - To remember (that)
    "RPL": ("present", {None: " remember", "3ps": " remembers", "present-participle": " remembering", "past-participle": " remembered"}),
    "RPLT": ("present", {None: " remember that", "3ps": " remembers that", "present-participle": " remembering that", "past-participle": " remembered that"}),
    "RPLD": ("past", {None: " remembered", "root": " remember", "present-participle": " remembering", "past-participle": " remembered"}),
    "RPLTD": ("past", {None: " remembered that", "root": " remember that", "present-participle": " remembering that", "past-participle": " remembered that"}),

    # RPLS: To remain
    "RPLS": ("present", {None: " remain", "3ps": " remains", "present-participle": " remaining", "past-participle": " remained"}),
    "RPLSZ": ("past", {None: " remained", "root": " remain", "present-participle": " remaining", "past-participle": " remained"}),

    # R - To run
    "R": ("present", {None: " run", "3ps": " runs", "present-participle": " running", "past-participle": " run"}),
    "RD": ("past", {None: " ran", "root": " run", "present-participle": " running", "past-participle": " run"}),

    # BS - To say (that)
    "BS": ("present", {None: " say", "3ps": " says", "present-participle": " saying", "past-participle": " said"}),
    "BTS": ("present", {None: " say that", "3ps": " says that", "present-participle": " saying that", "past-participle": " said that"}),
    "BSZ": ("past", {None: " said", "root": " say", "present-participle": " saying", "past-participle": " said"}),
    "BTSDZ": ("past", {None: " said that", "root": " say that", "present-participle": " saying that", "past-participle": " said that"}),

    # S - To see
    "S": ("present", {None: " see", "3ps": " sees", "present-participle": " seeing", "past-participle": " seen"}),
    "SZ": ("past", {None: " saw", "root": " see", "present-participle": " seeing", "past-participle": " seen"}),

    # BLS - To set
    "BLS": ("present", {None: " set", "3ps": " sets", "present-participle": " setting", "past-participle": " set"}),
    "BLSZ": ("past", {None: " set", "root": " set", "present-participle": " setting", "past-participle": " set"}),

    # PLS - To seem (to)
    "PLS": ("present", {None: " seem", "3ps": " seems", "present-participle": " seeming", "past-participle": " seemed"}),
    "PLTS": ("present", {None: " seem to", "3ps": " seems to", "present-participle": " seeming to", "past-participle": " seemed to"}),
    "PLSZ": ("past", {None: " seemed", "root": " seem", "present-participle": " seeming", "past-participle": " seemed"}),
    "PLTSDZ": ("past", {None: " seemed to", "root": " seem to", "present-participle": " seeming to", "past-participle": " seemed to"}),

    # RBL - shall - Auxiliary verb
    # These do not combine naturally with middle/structures.
    "RBL": ("present", " shall"),
    "RBLD": ("past", " should"),

    # RBZ - To show
    "RBZ": ("present", {None: " show", "3ps": " shows", "present-participle": " showing", "past-participle": " shown"}),
    "RBDZ": ("past", {None: " showed", "root": " show", "present-participle": " showing", "past-participle": " shown"}),

    # RBT - To take
    "RBT": ("present", {None: " take", "3ps": " takes", "present-participle": " taking", "past-participle": " taken"}),
    "RBTD": ("past", {None: " took", "root": " take", "present-participle": " taking", "past-participle": " taken"}),

    # BLGT - To talk -- conflict with like to.
    # "BLGT": ("present", {None: " talk", "3ps": " talks", "present-participle": " talking", "past-participle": " talked"}),
    # "BLGTD": ("past", {None: " talked", "root": " talk", "present-participle": " talking", "past-participle": " talked"}),

    # RLT - To tell
    "RLT": ("present", {None: " tell", "3ps": " tells", "present-participle": " telling", "past-participle": " told"}),
    "RLTD": ("past", {None: " told", "root": " tell", "present-participle": " telling", "past-participle": " told"}),

    # PBG - To think (that)
    "PBG": ("present", {None: " think", "3ps": " thinks", "present-participle": " thinking", "past-participle": " thought"}),
    "PBGT": ("present", {None: " think that", "3ps": " thinks that", "present-participle": " thinking that", "past-participle": " thought that"}),
    "PBGD": ("past", {None: " thought", "root": " think", "present-participle": " thinking", "past-participle": " thought"}),
    "PBGTD": ("past", {None: " thought that", "root": " think that", "present-participle": " thinking that", "past-participle": " thought that"}),

    # RT - To try (to)
    "RT": ("present", {None: " try", "3ps": " tries", "present-participle": " trying", "past-participle": " tried"}),
    "RTS": ("present", {None: " try to", "3ps": " tries to", "present-participle": " trying to", "past-participle": " tried to"}),
    "RTD": ("past", {None: " tried", "root": " try", "present-participle": " trying", "past-participle": " tried"}),
    "RTSDZ": ("past", {None: " tried to", "root": " try to", "present-participle": " trying to", "past-participle": " tried to"}),

    # RPB - To understand (the)
    "RPB": ("present", {None: " understand", "3ps": " understands", "present-participle": " understanding", "past-participle": " understood"}),
    "RPBT": ("present", {None: " understand the", "3ps": " understands the", "present-participle": " understanding the", "past-participle": " understood the"}),
    "RPBD": ("past", {None: " understood", "root": " understand", "present-participle": " understanding", "past-participle": " understood"}),
    "RPBTD": ("past", {None: " understood the", "root": " understand the", "present-participle": " understanding the", "past-participle": " understood the"}),

    # Z - To use
    "Z": ("present", {None: " use", "3ps": " uses", "present-participle": " using", "past-participle": " used"}),
    "DZ": ("past", {None: " used", "root": " use", "present-participle": " using", "past-participle": " used"}),
    # TZ -- Special case
    "TZ": ("present", " used to"),
    "TDZ": ("past", " used to"),

    # P: To want (to)
    "P": ("present", {None: " want", "3ps": " wants", "present-participle": " wanting", "past-participle": " wanted"}),
    "PT": ("present", {None: " want to", "3ps": " wants to", "present-participle": " wanting to", "past-participle": " wanted to"}),
    "PD": ("past", {None: " wanted", "root": " want", "present-participle": " wanting", "past-participle": " wanted"}),
    "PTD": ("past", {None: " wanted to", "root": " want to", "present-participle": " wanting to", "past-participle": " wanted to"}),

    # RBGS - will - Auxiliary verb
    # These do not combine naturally with middle/structures.
    "RBGS": ("present", " will"),
    "RBGSZ": ("past", " would"),

    # RBS - To wish (to)
    "RBS": ("present", {None: " wish", "3ps": " wishes", "present-participle": " wishing", "past-participle": " wished"}),
    "RBTS": ("present", {None: " wish to", "3ps": " wishes to", "present-participle": " wishing to", "past-participle": " wished to"}),
    "RBSZ": ("past", {None: " wished", "root": " wish", "present-participle": " wishing", "past-participle": " wished"}),
    "RBTSDZ": ("past", {None: " wished to", "root": " wish to", "present-participle": " wishing to", "past-participle": " wished to"}),

    # RBG - To work (on)
    "RBG": ("present", {None: " work", "3ps": " works", "present-participle": " working", "past-participle": " worked"}),
    "RBGT": ("present", {None: " work on", "3ps": " works on", "present-participle": " working on", "past-participle": " worked on"}),
    "RBGD": ("past", {None: " worked", "root": " work", "present-participle": " working", "past-participle": " worked"}),
    "RBGTD": ("past", {None: " worked on", "root": " work on", "present-participle": " working on", "past-participle": " worked on"}),
}


def lookup(key):
    starter_lookup, middle_lookup, structure_lookup, ender_lookup = determine_parts(key[0])

    starter, verb_form, _ = starter_lookup
    tense, verb = ender_lookup
    middle_word, middle_verb_form = lookup_data(middle_lookup, tense, verb_form)
    structure_format, use_middle_verb_form, structure_verb_update = lookup_data(structure_lookup, tense, verb_form)

    original_verb_form = verb_form
    if use_middle_verb_form and middle_verb_form:
        verb_form = middle_verb_form

    middle_phrase = lookup_data(structure_format, tense, original_verb_form+"-"+verb_form).replace(
        '*', middle_word, 1).replace('!', starter)

    if structure_verb_update:
        verb_form = structure_verb_update

    ending = lookup_data(verb, verb_form)
    if ending == None:
        raise KeyError

    return middle_phrase + ending

def determine_parts(stroke):
    if stroke in NON_PHRASE_STROKES:
        raise KeyError

    match = PARTS_MATCHER.match(stroke)
    starter_key, v1, star, v2, f, ender_key = match.groups()
    if not match:
        raise KeyError

    ender_lookup = ENDERS.get(ender_key)
    if not ender_lookup:
        raise KeyError

    # Check short form first.
    simple_starter_lookup = SIMPLE_STARTERS.get(starter_key + v1)
    simple_pronoun_lookup = SIMPLE_PRONOUNS.get(star + v2)
    if simple_starter_lookup and simple_pronoun_lookup:
        simple_structure = SIMPLE_STRUCTURES[f]
        return simple_pronoun_lookup, simple_starter_lookup, simple_structure, ender_lookup

    # Full form lookup.
    starter_lookup = STARTERS.get(starter_key)
    if not starter_lookup:
        raise KeyError

    _, _, valid_enders = starter_lookup
    if valid_enders and ender_key not in valid_enders:
        raise KeyError

    middle_lookup = MIDDLES[v1 + star]

    structure_lookup = STRUCTURE_EXCEPTIONS.get(starter_key + v1 + star + v2 + f)
    if not structure_lookup:
        structure_lookup = STRUCTURE_EXCEPTIONS.get(v1 + star + v2 + f)
    if not structure_lookup:
        structure_lookup = STRUCTURES[star + v2 + f]

    return starter_lookup, middle_lookup, structure_lookup, ender_lookup


def lookup_data(data, *keys):
    for key in keys:
        data = _lookup_data(data, key)
    return data

def _lookup_data(data, key):
    if type(data) is not dict:
        return data

    result = data.get(key)
    if result != None:
        return result

    if '-' in key:
        key = key.split('-')[1]
        result = data.get(key)
        if result != None:
            return result

    if key[0] == 'b':
        result = data.get(key[1:])
        if result != None:
            return result

    return data.get(None)

# Proper reverse lookup support.
#
# This will show phrasing strokes in Plover's suggestions window.


REVERSE_STARTERS = {"": {"": True}}
REVERSE_MIDDLES = {}
REVERSE_STRUCTURES = {}
REVERSE_ENDERS = {}

for key in STARTERS:
    word = STARTERS[key][0]
    REVERSE_STARTERS.setdefault(word, {})
    REVERSE_STARTERS[word][key] = "full"

for key in SIMPLE_PRONOUNS:
    word = SIMPLE_PRONOUNS[key][0]
    REVERSE_STARTERS.setdefault(word, {})
    REVERSE_STARTERS[word][key] = "simple"

POSSIBLE_REVERSE_MATCH = re.compile(r"[a-zI ']+")
HYPHEN_OMIT_PATTERN = re.compile(r"[AO*EU-]")


def add_reverse_middles(stroke, data, form):
    if type(data) is dict:
        for k in data:
            add_reverse_middles(stroke, data[k], form)
        return

    word = data[0].strip()

    REVERSE_MIDDLES.setdefault(form, {})
    REVERSE_MIDDLES[form].setdefault(word, {})
    REVERSE_MIDDLES[form][word][stroke] = True


def add_reverse_structures(stroke, data, form):
    if type(data) is dict:
        for k in data:
            add_reverse_structures(stroke, data[k], form)
        return

    word = data.strip()

    REVERSE_STRUCTURES.setdefault(form, {})

    REVERSE_STRUCTURES[form].setdefault(word, {})
    REVERSE_STRUCTURES[form][word][stroke] = form

    # To lookup empty starters, have entries that don't include '!'
    word = word.replace('!', '').strip()
    REVERSE_STRUCTURES[form].setdefault(word, {})
    REVERSE_STRUCTURES[form][word][stroke] = form


def add_reverse_enders(stroke, data):
    if type(data) is dict:
        for k in data:
            add_reverse_enders(stroke, data[k])
        return

    word = data.strip()
    REVERSE_ENDERS.setdefault(word, {})
    REVERSE_ENDERS[word][stroke] = True


for key in MIDDLES:
    add_reverse_middles(key, MIDDLES[key], "full")

for key in SIMPLE_STARTERS:
    add_reverse_middles(key, SIMPLE_STARTERS[key], "simple")

for key in STRUCTURE_EXCEPTIONS:
    add_reverse_structures(key, STRUCTURE_EXCEPTIONS[key][0], "full")

for key in STRUCTURES:
    add_reverse_structures(key, STRUCTURES[key][0], "full")

for key in SIMPLE_STRUCTURES:
    add_reverse_structures(key, SIMPLE_STRUCTURES[key][0], "simple")

for key in ENDERS:
    add_reverse_enders(key, ENDERS[key][1])


def add_verb_stroke(prefix, suffix):
    # This check prevents adding in extra '-' when it will cause issues in lookup().
    if HYPHEN_OMIT_PATTERN.search(prefix) or HYPHEN_OMIT_PATTERN.search(suffix):
        return prefix + suffix

    return prefix + '-' + suffix


def reverse_match(result, full_text, stroke):
    try:
        if lookup([stroke]).strip() == full_text:
            result.append((stroke,))
    except KeyError:
        pass


def reverse_verb_match(result, full_text, text, prefix):
    if text not in REVERSE_ENDERS:
        return

    prefix = prefix.replace('**', '*', 1)
    for stroke in REVERSE_ENDERS[text]:
        reverse_match(result, full_text, add_verb_stroke(prefix, stroke))


def reverse_structure_match(result, full_text, text, prefix, form):
    words = text.split(' ')
    for i in range(len(words)+1):
        phrase = ' '.join(words[:i])
        if phrase not in REVERSE_STRUCTURES[form]:
            continue

        for structure_stroke in REVERSE_STRUCTURES[form][phrase]:
            remainder = text.replace(phrase, '', 1).strip()
            stroke = add_verb_stroke(prefix, structure_stroke)
            reverse_verb_match(result, full_text, remainder, stroke)


def reverse_middle_match(result, full_text, text, prefix, form):
    for word in REVERSE_MIDDLES[form]:
        if word in text:
            r = text.replace(word, '*', 1)
            r = r.replace(' *', '*')
            for s in REVERSE_MIDDLES[form][word]:
                stroke = add_verb_stroke(s, prefix) if form == "simple" else add_verb_stroke(prefix, s)
                reverse_structure_match(result, full_text, r, stroke, form)

    reverse_structure_match(result, full_text, text, prefix, form)


def reverse_lookup(text):
    if not POSSIBLE_REVERSE_MATCH.fullmatch(text):
        return []

    # Maximum phrase is 7 words, so early out if being asked for the stroke
    # for more.
    words = text.split(' ')
    if len(words) > 7:
        return []

    result = []

    for word in REVERSE_STARTERS:
        if word == "":
            continue

        if word in text:
            remainder = re.sub("\\b%s\\b" % word, '!', text, 1)
            strokes = REVERSE_STARTERS[word]
            for stroke in strokes:
                reverse_middle_match(result, text, remainder, stroke, strokes[stroke])

    # Testing for empty starters
    for stroke in REVERSE_STARTERS['']:
        reverse_middle_match(result, text, text, stroke, "full")

    return result

