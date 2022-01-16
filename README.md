# Steno Dictionaries
An alternate set of dictionaries for Plover theory.

## plover-base.json
This dictionary is intended to replace Plover's main.json that comes by default. It's not intended to be as extensive (hence **base**) but it should hopefully be more consistent and easier to use, especially as it does not contain any misstrokes.

> There are still some stacking misstrokes for phrases with multiple strokes, but that shouldn't affect learning basic words and being familiar with the theory

While the majority of Plover theory have been left untouched, there are several additions to the underlying theory that make this a little problematic if one were to switch to this dictionary after being accustomed to main.json. With that said, there are still many similarities and many briefs that have been kept in this dictionary.

Using a textbook such as Learn Plover! should work just fine with this dictionary, as long as one also reads this documentation.

### About this dictionary

#### Compound words
Compound words are always written with the asterisk on the first stroke of the second word. For example, to write the word "storybooks" would be as `STOR/KWREU/PWAO*BG/-S`.

Examples:
 - `KAOE/PWAO*RD` → keyboard
 - `TEGT/PWAO*BG` → textbook
 - `PHOUS/PA*D` → mousepad

#### Proper nouns
Proper nouns are always written with the number key on the first stroke. Everything else is written with the same rules.
 - `#A/HREU/SA` → Alyssa
 - `#PWOB` → Bob
 - `#PAOE/TER` → Peter

> Unfortunately, entries using the number key will not be displayed as I have above, but rather with numbers. So viewing the dictionary you would see `350ER/TER` instead of `#PAOE/TER`.

> I'm not sure if this is a good idea; it feels rather clunky, and I've only been trying this out for a few days so this may change.

#### Movement keys
This dictionary contains arrow key movements and a few selecting movements. By pressing down `STPH` on the left hand, the `-RPBG` cluster becomes arrow keys. `-FR` chorded together would be home, and `-LG` would be end. Pageup and pagedown resemble arrows pointing up and down respectively `-RPG` and `-FBL`.

By pressing `STPH*` instead, the shift modifier is used together with the movement keys in order to select text.

To move word by word (equivalent to pressing `Ctrl+Shift` and left/right), `-RB` and `-BG` are used. I don't know how this works on Macs, but my understanding is the something else has to be used that's not `Ctrl`.

#### Commands and keyboard shortcuts
Many of the commands from main.json have stayed the same.
 - `KPA` → capitalize the next word
 - `KPA*` → capitalize the next word and supress the next space
 - `HRO*ER` → uncapitalize the next word

Retroactive commands have also been added.
 - `KA*PD` → capitalize the last word
 - `HRO*ERD` → uncapitalize the last word

Common keyboard keys have also carried over from main.json.
 - `R-R` → enter/return (capitalization of next word depends on previous punctuation)
 - `#R-R` → `Shift+Enter`
 - `PW-FP` → backspace one character
 - `PW*FP` → backspace one word (`Ctrl+Backspace`; this will have to be changed on Macs)
 - `TKHRE` → delete one character
 - `TKHR*E` → delete one word (`Ctrl+Delete`; this will have be changed on Macs)
 - `TA*B` → `Tab`
 - `#TAB` → `Shift+Tab`

#### Punctuation
 - `H-F` → `?` question mark
 - `KW-PL` → `?` shape can be thought of rising inflection as if asking a question
 - `TP-BG` → `!` shape can be thought of as falling inflection when exclaiming
 - `TP-PL` → `.` period
 - `P-P` → `.` period with no space on either side (when writing decimals)
 - `KW-BG` → `,` comma
 - `KW-GS` → `"` opening quotation mark
 - `KW*GS` → `"` closing quotation mark
 - `KH-FG` → `\`` opening backtick
 - `KH*FG` → `\`` closing backtick
 - `PREPB` → `(` opening parenthesis
 - `PR*EPB` → `)` closing parenthesis
 - `TPR-BGT` → `{` opening French bracket
 - `TPR*BGT` → `}` closing French bracket
 - `PWR-BGT` → `[` opening bracket
 - `PWR*BGT` → `]` closing bracket
 - `KHR-PB` → `:` colon with no spacing
 - `STPH-FPLT` → `:` regular colon with a space on the right
 - `STPH*FPLT` → `;` regular semicolon with a space on the right
 - `TR*PL` → `™` trademark symbol with a space on the right

For symbols beyond these where you might require different spacing and capitalization, I recommend [Emily's symbols dictionary](https://github.com/EPLHREU/emily-symbols).

#### Right hand number pad
> The conventional number system will not work with this dictionary. You will have to delete all entries containing the glue operator and a number (e.g. `{&8}`) if you want to use the conventional number system.

With this system, pressing the number key will turn `-FRPBLG` into a keypad of sorts. The bottom three keys are 1, 2, and 3 (from left to right) while the top three keys are 7, 8, 9 and chording two keys in a column will get 4, 5, and 6 (from left to right). If the `E` key is used in the stroke, 0 will be appended to whatever digit is being chorded. The `U` key will append a 00 on the digit, and `EU` will append a 000 on the digit.

Examples:
 - `#-G/#-R/-FR/#-R/#-PB/#-L` → 314159
 - `#EB` → 20
 - `#UPB`→ 500

> I highly recommend mapping the top `S-` key to the number key to make it easier to stroke. This also opens up the possibility for more briefs. This makes it much easier to use and decreases hesitation as to which finger to use to hit the number key.

#### Fingerspelling with periods
In addition to normal fingerspelling, using `-FPLT` of `*` will put a period after the letter. `*FPLT` will capitalize the word.

Examples:
 - `PW*FPLT/KR*FPLT/*EFPLT` → B.C.E.
 - `AFPLT/P-FPLT/P-FPLT/HR-FPLT/EFPLT` → a.p.p.l.e.

> Planning on using `-RBGS` for fingerspelling with hyphens (stitching) but this requires the plover-stitching plugin.

#### Phonetics and orthography
There are only a few changes:
 - `*PL` is always used as the -mp cluster (never `-FRP`)
 - `-P` by itself can be used to "add on" Ps
    - `HEL/-P` → help
    - This rule is used very rarely, and is not guaranteed to be consistent
 - "or" sound is always used with `OR`
    - `OER` is never used to represent this phonetically
 - `KWR` is used in certain diphthongs such as:
    - `SREUD/KWROE` → video
    - `AEUR/KWRA` → area
    - `EUPB/SOPL/TPHEU/KWRA` → insomnia
    - `AOE/KWRAL/TEU` → reality
    - Essentially, if the vowel can be approximated with "Y", it is used
    - This is the same as Plover's main.json, but I still figure it's worth mentioning
 - `KHUR` is always used for the "chur" sound
    - In main.json, there are many inconsistent ways to write a word such as "culture"
        - `KUL/KHAOUR`, `KUL/TAOUR`, `KUL/KHUR`, `KUL/TUR`, etc
    - In this dictionary, culture is written as `KUL/KHUR`
    - Other examples:
        - `HREBG/KHUR` → lecture
        - `KAP/KHUR` → capture
        - `PHA/KHUR` → mature

#### Breaking up multisyllable words
main.json relies on a lot of dropping unstressed vowels in order to break up words which is also used in this dictionary. Words such as "memorize" benefit from a rule like this as the middle syllable is essentially dropped, leaving it unambiguous as to where to break it up: `PHEPL/RAOEUZ`. This dictionary also includes some entries where unstressed vowels haven't been dropped, but it is recommended to not use these as they may not be complete.

If it is still ambiguous as to where a syllable break starts (even if unstressed vowels have been dropped) then the rule is to carry each syllable as far as possible so that every stroke can start with a consonant. Consonants are also never doubled (`TKPWHROR/REU` (glory) would not be valid). I refer to this as the "normal" splitting method.

Examples:
 - `TPOE/TPHE/TEUBG` → phonetic
 - `PEUBG/KHUR` → picture
 - `KAL/KAOU/HRAEU/TOR` → calculator
 - `RE/KOG/TPHEUGS` → recognition
 - `ABG/TEUF` → active

These would not be valid ways of breaking up a word:
 - `RAPBD/OPL` (random) ❌
 - `KAOEB/ORD` (keyboard) ❌
 - `HRAPT/OP` (laptop) ❌

However, some words will not be able to be broken up like this such as words starting with vowels. These are handled exactly the same, except that it is acceptable for the first stroke to begin with a vowel. I still categorize this under the "normal" splitting method.

Examples:
 - `EUPL/POR/TAPBT` → important
 - `OE/PWAEU` → obey
 - `ABG/SES` → access

It is also important to use prefixes and suffixes whenever possible to break up words. Many entries containing prefixes and suffixes exist in the dictionary. However, given the nature of how Plover handles suffixes, writing words using these strokes that aren't defined in the dictionary will not show up when using the lookup tool.

Examples:
 - `HRAOBG/SKWRUP` → lookup
 - `HRERPB/*ER` → learner
 - `KOP/KWREU` → copy

Some words will also be able be stroked using suffix strokes, even if whatever was previously stroked is is not a word. This may be because some strokes would be too short and would cause word boundary issues.

Examples:
 - `UT/*ER` → utter (as opposed to `U/TER`)
 - `ED/EUGS` → edition (as opposed to `E/TKEUGS`)
 - `HR*ET/*ER` → leather
 - `ALD/*ER` → alder
 - `KEUT/KWREU` → kitty (as opposed to `KEU/TEU`)

> Whenever `KWREU` can be used, always default to that instead (like in the "kitty").

If there are two vowels next to each other that have to be represented in two strokes, `KWR` is used as a linker between the vowels.

Examples:
 - `AOEU/KWROE/HREU` → aioli
 - `PAOE/KWRA/TPHOE` → piano

If there is no other way to break up a word so that every non-prefix, non-suffix, and non-starting stroke begins with a vowel, `KWR` is used instead as a linker.

Examples:
 - `ER/KWROR` → error
 - `PHEUR/KWROR` → mirror (can't double the R, and `PHEU` is "my")
 - `ES/KWRAEU` → essay (can't double the S, and `E` is too short by itself).

This `KWR` linker is also used if the "normal" splitting method will result in word boundary errors as well as if prefixes and suffixes cannot be used.

Examples:
 - `KOL/KWREBGT` → collect
    - The "normal" splitting method would use `KO/HREBGT`, but `KO` is the brief for "could" and `HREBGT` is the brief for "elect"
        - "collect" vs "could elect"

In general, every word in the dictionary will have at least one of these ways to break up a word. You may use whichever method makes the most sense for a given word

However, I would recommend using anything other than the "normal" method to break up words as the others are not available for all words.

Here are some examples of how not to break up a word:
 - `TERPL/KWRAOEUT` (termite) ❌
    - It is not necessary to use `KWR` as the "normal" method works just fine
    - Instead use `TER/PHAOEUT`
 - `EBGS/SAOED` (exceed) ❌
    - `-BGS` already contains the "ks" sound, and the S in the second stroke repeats a consonant
    - Instead use `EBG/SAOED` or `EBGS/KWRAOED`
 - `TPRAFRPB/AOEUZ` (franchise) ❌
    - "Normal" splitting method works in this scenario
    - Instead use `TPRAPB/KHAOEUS` or `TPRAPB/KHAOEUZ`

#### Suffixes and prefixes
 - Since we cannot double consonants, `KWREU` is default for adding "-y"
    - `KEUT/KWREU` → kitty
    - `STOR/KWREU` → story
 - `OER` is always used for "-ory" suffix
    - `SA/TEUS/TPABGT/OER` → satisfactory
 - `-PB` is the "-en" suffix
    - `HRAOEUT/-PB` → lighten
    - `SOFT/-PB` → soften
 - `-PBT` is the "-ent" suffix
    - `A/STREUPBG/-PBT` → astringent
    - `STAOUD/-PBT` → student
    - `AOE/TPEURB/-PBT` → efficient
 - `-PLT` is the "-ment" suffix
 - Words ending in "-ous" and "-us" always use `KWRUS` or some variation
    - `STAOU/PEPB/TKUS` → stupendous
    - `RAOEUT/KWRUS` → righteous
    - `KHAOEUT/KHUS` → righteous
 - `-LT` for the "-let" suffix
    - `A/PHAOU/-LT` → amulet
    - `STAR/-LT` → starlet
 - `EUFT/EUBG` and `ST-BG` are preferred for "-istic"
    - `RAEL/EUFT/EUBG` → realistic
    - `A/TPHA/KROPB/ST-BG` → anachronistic

## plover-uk.json
Soon™
