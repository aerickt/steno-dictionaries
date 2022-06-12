# Steno Dictionaries
My personal steno dictionaries.
 - [commands.json](#commandsjson)
 - [movement.modal](#movementmodal)
 - [plover-base.json](#plover-basejson)
 - [plover-uk.json](#plover-ukjson)
 - [raw.py](#rawpy)
 - [rh-numpad.json](#rh-numpadjson)
 - [uni-number-reversals.json](#uni-number-reversalsjson)

## commands.json
This dictionary contains all main movement, keyboard shortcuts, and Plover commands that I use.

### Dictionary contents
 - [Movement keys](#Movement-keys)
 - [Commands and keyboard shortcuts](#Commands-and-keyboard-shortcuts)

#### Movement keys
By pressing down `STPH` on the left hand, the `-RPBG` cluster becomes arrow keys. `-FR` chorded together would be home, and `-LG` would be end. Pageup and pagedown resemble arrows pointing up and down respectively `-RPG` and `-FBL`.

By pressing `STPH*` instead, the shift modifier is used together with the movement keys in order to select text.

To move word by word (equivalent to pressing `Ctrl+Shift` and left/right), `-RB` and `-BG` are used. On macOS, `Alt+Shift` is used instead so that will have to be changed.

#### Commands and keyboard shortcuts
Many of the commands from main.json have stayed the same.
 - `KPA` → capitalize the next word
 - `KPA*` → capitalize the next word and supress the next space
 - `HRO*ER` → uncapitalize the next word
 - `TK-LS` → supress the next space

Retroactive commands have also been added.
 - `KA*PD` → capitalize the last word
 - `HRO*ERD` → uncapitalize the last word
 - `TK-FPS` → remove the last space

Common keyboard keys have also carried over from main.json.
 - `R-R` → enter/return (capitalization of next word depends on previous punctuation)
 - `#R-R` → `Shift+Enter`
 - `PW-FP` → backspace one character
 - `PW*FP` → backspace one word (`Ctrl+Backspace`; change to `Alt+Backspace` on macOS)
 - `TKHRE` → delete one character
 - `TKHR*E` → delete one word (`Ctrl+Delete`; change to `Alt+Delete` on macOS)
 - `TA*B` → `Tab`
 - `#TAB` → `Shift+Tab`

For writing every single keyboard shortcut possible, I recommend [Emily's modifiers dictionary](https://github.com/EPLHREU/emily-modifiers).

## movement.modal
This is a modal dictionary that is an extension to the [movement keys in my commands.json dictionary](#Movement-keys).

After the [modal dictionary plugin](https://github.com/Kaoffie/plover_modal_dictionary) has been installed from the plugins manager, ensure Plover has been restarted and the plugin is enabled (configure → plugins). Next add the dictionary above whichever dictionary contains the default movement strokes.

Using this dictionary for movement keys is exactly the same as those in [commands.json](#Movement-keys), however every successive movement stroke after the first does not need to contain the `STPH` cluster.

Examples:
 - `STPH-G/-G/-G/-G` → arrow key to the right 4 times
 - `STPH*R/*R/*R` → select 3 characters to the left
 - `STPH-BG/-BG/-BG` → move to the right by 3 words

## plover-base.json
This dictionary is intended to replace Plover's `main.json` that comes by default. It's not intended to be nearly as extensive (hence **base**) but it should hopefully be more consistent and easier to use, especially as it does not contain any misstrokes.

While the majority of Plover theory have been left untouched, there are several additions to the underlying theory that make this a little problematic if one were to switch to this dictionary after being accustomed to main.json.

> While I believe this dictionary follows more rigorous rules (especially with regard to syllable splitting) this is still my personal dictionary and is subject to mistakes. If you spot any bad entries, please let me know!

> I'm currently at 79,000 entries. I started with a word list of the most common 3000 English words and later went through a more complete word list alphabetically up until the letter M. I have stopped moving alphabetically through the word list and I am only adding entries randomly at this point.

I've written a little bit about my motivations for creating a new dictionary over on my [website](https://aerick.ca/steno/dictionary-building) if you'd like a summary of this project.

### Dictionary contents
 - [Compound words](#Compound-words)
 - [Proper nouns](#Proper-nouns)
 - [Movement keys, keyboard shortcuts, commands](#movement-keys-keyboard-shortcuts-commands)
 - [Punctuation](#Punctuation)
 - [Right hand number pad](#Right-hand-number-pad)
 - [Fingerspelling](#Fingerspelling)
 - [Phonetics and orthography](#Phonetics-and-orthography)
 - [Breaking up multisyllable words](#Breaking-up-multisyllable-words)
 - [Exceptions to syllable breaks](#Exceptions-to-syllable-breaks)
 - [Prefixes and suffixes](#Prefixes-and-suffixes)
 - [Conflict resolution](#Conflict-resolution)

#### Compound words
Compound words are always written with the asterisk on the first stroke of the second word.
 - `KAOE/PWAO*RD` → keyboard
 - `TEGT/PWAO*BG` → textbook
 - `PHOUS/PA*D` → mousepad
 - `STOR/KWREU/PWAO*BG/-S` → storybooks

> This rule is more relaxed with proper nouns

#### Proper nouns
Proper nouns are always written with the number key on the first stroke. Everything else is written with the same rules.
 - `#A/HREU/SA` → Alyssa
 - `#PWOB` → Bob
 - `#PAOE/TER` → Peter
 - `#AP/-L` → Apple
 - `#AUS/TRAEUL/KWRA` → Australia
 - `HART/PHAPB` → Hartman

> I highly recommend mapping the top `S-` key to the number key to make it easier to stroke. This also opens up the possibility for more briefs and decreases hesitation when deciding which finger to use for the number key.

> Unfortunately, entries using the number key will not be displayed as I have above, but rather with numbers. So viewing the dictionary you would see `350ER/TER` instead of `#PAOE/TER`.

#### Movement keys, keyboard shortcuts, commands
See [commands.json](#commandsjson) as plover-base.json contains this dictionary by default.

#### Punctuation
 - `H-F` → `?` question mark
 - `KW-PL` → `?` shape can be thought of rising inflection as if asking a question
 - `TP-BG` → `!` shape can be thought of as falling inflection when exclaiming
 - `TP-PL` → `.` period
 - `P-P` → `.` period with no space on either side (when writing decimals)
 - `KW-BG` → `,` comma
 - `KW-GS` → `"` opening quotation mark
 - `KW*GS` → `"` closing quotation mark
 - `KH-FG` → `` ` `` opening backtick
 - `KH*FG` → `` ` `` closing backtick
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
> The conventional number system does not work in plover-base.json. You will have to delete all entries containing the glue operator and a number (e.g. `{&8}`) if you want to use the conventional number system.

plover-base.json has this system by default. See [rh-numpad.json](rh-numpadjson).

#### Fingerspelling
In addition to normal fingerspelling with `*`, using `-FPLT` of `*` will put a period after the letter. `*FPLT` will capitalize the word. `-RBGS` is used for stitching (requires `plover-stitching` plugin).

Examples:
 - `PW*FPLT/KR*FPLT/*EFPLT` → B.C.E.
 - `AFPLT/P-FPLT/P-FPLT/HR-FPLT/EFPLT` → a.p.p.l.e.
 - `PW*RBGS/KR*RBGS/*ERBGS` → B-C-E
 - `ARBGS/P-RBGS/P-RBGS/HR-RBGS/ERBGS` → a-p-p-l-e

Stroking `-FPLT` and `-RBGS` n times will stitch the n words with periods and hyphens retroactively.

Examples
 - `AP/-L/-FPLT` → a.p.p.l.e
 - `PHEU/TPHAEUPL/S/#TOD/-RBGS/-RBGS/-RBGS/-RBGS` → M-y n-a-m-e i-s T-o-d-d

> Note: stroking `-FPLT` does not leave a trailing period.

#### Phonetics and orthography
The main principles of Plover theory have been left unchanged and Learn Plover! or Art of Chording are fully compatible with this dictionary (apart from word breaks as well as suffixes and prefixes). The following list includes changes I've made as well as any rules or tips not necessarily mentioned in any main learning resources for stock Plover.
 - `*PL` is used as the -mp cluster intsead of `-FRP`
 - Ending syllables that fall out of steno order
    - `-P` ends syllables with a p sound
       - `HEL/-P` → help
    - `-L` ends syllables with an l
       - `STRAPBG/-L` → strangle
    - `-PL` ends syllables with m
       - `HEL/-PL` → helm
    - Any other ending sounds use asterisk
       - `PHUL/*FP` → mulch
       - `TKEL/*F` → delve
       - `HREUPL/*F` → lymph
       - Briefer outlines also exist that use inversions or compound clusters
 - `OR` is used for the "or" sound
    - `OER` is only used in briefs and suffix sounds
 - `KWR` is used in certain diphthongs such as:
    - `SREUD/KWROE` → video
    - `AEUR/KWRA` → area
    - `EUPB/SOPL/TPHEU/KWRA` → insomnia
    - `RAOE/KWRAL/TEU` → reality
    - `#PHAR/KWROE` → Mario
    - `HAUP/KWRA` → haupia
       - You may find entries such as `HAU/PEU/KWRA` → haupia; these are not recommended as they may be incomplete
    - Essentially, if the vowel can be approximated with "Y", it is used
 - `KHUR` is always used for the "chur" sound
    - In main.json, there are many inconsistent ways to write a word such as "culture"
        - `KUL/KHAOUR`, `KUL/TAOUR`, `KUL/KHUR`, `KUL/TUR`, etc
    - In this dictionary, culture is written only as `KUL/KHUR`
    - Other examples:
        - `HREBG/KHUR` → lecture
        - `KAP/KHUR` → capture
        - `PHA/KHUR` → mature
 - `TWAL` is used for "ch" sounds found in words like the following that are usually spelled as "-tual":
    - `SPEU/REU/TWAL` → spiritual
    - `AOE/SREPB/TWAL` → eventual
    - `EUPB/TE/HREBG/TWAL` → intellectual
    - `PHAOU/TWAL` → mutual
 - `TK*EU` is always used for the initial `TKEU` sound when starting a word
    - `TK*EU/REBGT` → direct
    - `TK*EU/HREU/SKWREPBT` → diligents
 - `EU` is used for long I when it is spelled with an "I" or a "Y"
    - `AR/PE/SKWREU/KWROE` → arpegg**i**o
    - `KUFRB/KWREU` → curvy
    - `KRUFT/KWREU/HREU` → crustily
    - > There are a lot of words that just *feel* wrong to use `EU` instead of `AOE` based on my experience using main.json. I haven't been able to figure out what causes this, so I've resorted to include both `EU` and `AOE` in these cases where it's ambiguous to me. However, if it's spelled with an I and has a long I sound, I can guarantee that `EU` can be used.
    - > this pattern is from main.json and its suffixes such as "-y", "-ry", "-ly", etc.
 - `-RBL` → "shl" sound
    - `TK*EU/TPE/REPB/-RBL` → differential
    - `TPAOEU/TPHAPB/-RBL` → financial

#### Breaking up multisyllable words
main.json relies a lot on dropping unstressed vowels in order to break up words. Words such as "memorize" benefit from a rule like this as the middle syllable is essentially dropped, leaving it unambiguous as to where to break it up: `PHEPL/RAOEUZ`. This dictionary prioritizes entries that do not drop unstressed vowels for writing out (though many briefer entries use this principle).

In order to split a word into multiple strokes, the following rules should be used:
 - Consonants should not be doubled across strokes
    - e.g., `PHE/PHOR/RAOEUZ` would not be correct as it doubles the R
 - Strokes after the initial one should not begin with a vowel
    - e.g., `PHEPL/OR/AOEUZ` is incorrect, the last two strokes begin with vowels
    - Apart from suffix strokes which are special
      - e.g., `AER` → "-ary"

There are, of course, exceptions to these rules which are covered later. I will refer to this style as the "normal" splitting method.

"Normal" splitting method:
 - `PHE/PHO/RAOEUZ` → memorize
 - `TPOE/TPHE/TEUBG` → phonetic
 - `PEUBG/KHUR` → picture
 - `KAL/KAOU/HRAEU/TOR` → calculator
 - `RE/KOG/TPHEUGS` → recognition
 - `ABG/TEUF` → active
 - `AD/HAOE/SEUF` → adhesive

"Normal" splitting with first stroke starting with a vowel:
 - `EUPL/POR/TAPBT` → important
 - `OE/PWAEU` → obey
 - `ABG/SES` → access

It is also important to use prefixes and suffixes whenever possible. Some words cannot be split "normally" as they can be constructed using these special strokes.

The following examples can only be written using suffix strokes:
 - `HRERPB/*ER` → learner
 - `KOP/KWREU` → copy
 - `TOG/-L` → toggle
 - `KEUT/KWREU` → kitty

However sometimes for a given word, it may not be clear that a suffix can be used. For example, the word "copy" is not related to the word "cop" in terms of its modern definitions but it is still written using the "-y" suffix.

This suffix stroke along with a few others are special in that they can be used in words where the previously written translation wasn't necessarily a word or related to the intended word.

These suffixes should be able to be used universally:
 - `KWREU` → "-y"
 - `*ER` → "-er"
 - `-L` → "-l"

The following are examples of using these suffixes in this manner:
 - `TPAOUR/KWREU` → fury
 - `PWUR/KWREU` → bury
 - `TPOEPB/KWREU` → phoney
 - `HR*ET/*ER` → leather
 - `KOR/KWREU/KWRAPBD/*ER` → coriander
 - `TPA*UT/*ER` → father
 - `EBG/SA*PL/-L` → example
 - `OBS/TABG/-L` → obstacle
 - `*UPBG/-L` → uncle

Note: this rule is only a recent addition and it doesn't apply to all words. For example, the word "demography" should be able to be written `TKE/PHOG/RAF/KWREU`, however, there are already a lot of entries for "demography". In particular, if one wishes to use the `KWREU` suffix it would make more sense to use `TKE/PHO/TKPWRAF/KWREU` as `TKE/PHO` is a prefix stroke, and `TKPWRAF` is a word by itself.

These special suffixes can be used when they make more sense than "normal" syllable splitting or using regular affix strokes, but I would not recommend relying on them completely.

Prefixes should also be used in this manner.
 - `AOE/KHRAOE/SEU/KWRAS/TEUBG` → ecclesiastic
    - Since `AOE` is the "e-" prefix, it is used instead of `AOEBG/HRAOE/...`

If there are two vowels next to each other that have to be represented in two strokes, `KWR` is used as a linker between the vowels.

`KWR` as a linker between vowels:
 - `AOEU/KWROE/HREU` → aioli
 - `PEU/KWRA/TPHOE` → piano

Depending on pronuncation, `W` can also begin a consecutive vowel stroke:
 - `AL/TRAOU/WEUS/TEUBG` → altruistic
 - `KOPB/TKAOU/WEUT` → conduit

In general, every word in the dictionary will have at least one of these ways to break up a word. Special suffixes are first preferred if they feel more natural than "normal" splitting, followed by regular suffixes on root words, and finally "normal" splitting which may involve the `KWR` linker.

Other invalid examples of splitting a word:
 - `TERPL/KWRAOEUT` (termite) ❌
   - Use normal method, `TER/PHAOEUT`
 - `EBGS/SAOED` (exceed) ❌
   - Don't double consonants, instead use `EBG/SAOED`
   - Instead use `EBG/SAOED` (see below)
 - `TPRAFRPB/AOEUZ` (franchise) ❌
   - Normal method is sufficient: `TPRAPB/KHAOEUS`
 - `PWET/KWRER` (better) ❌
   - Instead use `PWE/TER` or `PWET/*ER`
 - `TES/TER` (tester) ❌
   - Use `*ER` suffix: `TEFT/*ER`

> There may still be entries that seem to contradict the basic syllable splitting rules; I'd recommend not using these as they are only remenants of main.json style syllable splitting that I am accustomed to.

Other notes:
 - Words beginning with "ex" can be written with `EBGS` or some form of `EBG/S`
    - For a word such as exile, the X sound is made up of k and s. Doubling the S would not be permitted, so it is written as `EBG/SAOEUL` or `EBG/SAO*EUL` if it is pronounced like a Z
    - Other examples:
        - `EBG/SE/KRAEUT` → execrate
        - `EBG/SE/KAOUGS` → execution
        - `EBG/S*EU/SKWREPBS` exigence
        - `EBG/S*ULT` → exult
        - `EBGS/SES` → excess
        - `EBG/SES` → excess

#### Exceptions to syllable breaks

Sometimes a stroke should not begin with a certain chord as it is a common brief and would lead to word boundary issues. The following chords should not be used as strokes to start an outline.
 - `KO`
 - `O`
 - `E`
 - `U`
 - `EU`

Instead carry the first stroke far enough so that there is a consonant on the right hand and use other means to complete the word.
 - `KOL/KWREBGT` → collect
 - `KOR/KWREBGT` → correct
 - `EBG/KWRO/TPHO/PHEUBG` → economic

If the first stroke of an outline is a prefix, there is no need to use the `KWR` starter on the next stroke:
 - `KOE/OR/TKEU/TPHAEUT` → coordinate
 - `PRE/EPLT` → preempt
 - `TK*EU/AOE/HREBG/TREUBG` - dielectric
 - `TKEUS/AEUBL` → disable

Consonants can also be doubled if the previous stroke is a prefix and the strokes that follow form a valid word on their own:
 - `TKEUS/SOFLS` → dissolves
 - `TKEUS/SEU/PHEU/HRAR` → dissimilar

#### Prefixes and suffixes
 - Since doubling consonants isn't used, `KWREU` is default for adding "-y"
    - `KEUT/KWREU` → kitty
    - `STOR/KWREU` → story
 - `OER` is used for the "-ory" sound but not by itself
    - `SA/TEUS/TPABG/TOER` → satisfactory
    - `TPABG/TOER` → factory
 - `O*R/KWREU` can still be used for the "-ory" suffix
    - `AUTD/O*R/KWREU` → auditory
 - `KWREPB` → "-en"
    - `HRAOEUT/KWREPB` → lighten
    - `SOFT/KWREPB` → soften
 - `KWREPBT` → "-ent"
    - `A/STREUPBG/KWREPBT` → astringent
    - `STAOUD/KWREPBT` → student
    - `AOE/TPEURB/KWREPBT` → efficient
 - `-PLT` → "-ment"
 - Words ending in "-ous" and "-us" always use `KWRUS` or some variation
    - `STAOU/PEPB/TKUS` → stupendous
    - `RAOEUT/KWRUS` → righteous
    - `RAOEUT/KHUS` → righteous
 - `-LT` → "-let" suffix
    - `A/PHAOU/-LT` → amulet
    - `STAR/-LT` → starlet
 - `-L` → "-le" suffix
 - `KWREUFT` → "-ist"
 - `KWREUBG` → "-ic"
 - `ST-BG` → "-istic"
    - `A/TPHA/KROPB/ST-BG` → anachronistic
    - `KWREUS/TEUBG` and `KWREUFT/KWREUBG` will also work, but are usually not explicitly defined
 - `SH-PBS` → "-ishness" suffix
    - `TPAOL/SH-PBS` foolishness
    - `PWHRU/SH-PBS` → bluishness
 - `SH*EUP` → "-ship" suffix
    - `TPREPBD/SH*EUP` → friendship
 - `{^ally}` is `A*EL` or `A*L/KWREU` but these are not defined in the dictionary
    - Usually `HREU` can also work as these are explicitly defined in the dictionary
        - For example, `TKE/PHO/TKPWRAF/KWREUBG/HREU` → demographically (in the dictionary)
        - `TKE/PHO/TKPWRA/TPEUBG/A*EL` → demographically (not in the dictionary)
        - `TKE/PHO/TKPWRA/TPEUBG/A*L/KWREU` → demographically (not in the dictionary)
 - Words beginning with "for":
    - Use `TPAUR` by default ("for-" prefix)
        - `TPAUR/TKPWOE` → forgo
        - `TPAUR/SAEUBG` → forsake
        - `TPAUR/TAOU/WEU/TUS` → fortuitous
        - `TPAUR/PHAOU/HRAEUT` → formulate
    - If a compount word begins with "fore", use `TPOER` and asterisk the second word
        - `TPOER/H*ED` → forehead
        - `TPOER/TPHO*/HREPBLG` → foreknowledge
    - If other consonants on the right will be included in a stroke, use `TPOR`
        - `TPORPL/HRAEUT` → formulate
        - `TPORT/KWREU` → forty
 - `WAL` → "-ual" suffix
    - `PHAOUFP/WAL` → mutual
    - `SEPBS/WAL` → sensual
    - `EUPB/TE/HREBGT/WAL` → intellectual

#### Conflict resolution

If two homophones must be resolved using asterisk, there are a few aspects of each word that will decide which word gets precedence.
 - If there are repeat letters in a word, that will use asterisk
   - `#HART/PHAPB` → Hartman
   - `#HART/PHA*PB` → Hartmann
 - If two words differ in a vowel, (especially with Y or I), the asterisk will go to the word that doesn't match the vowel as spelt
   - `#HREUPB` → Lin
   - `#HR*EUPB` → Lynn
 - "kr" gets precedence over "chr" and "cr" in `KR-` as it matches the keys more
   - `#KREUS/TEU` → Kristy
   - `#KR*EUS/TEU` → Christy
 - "x" and "ks" gets precedence over "kshun" in" `-BGS`
   - `TRABGS` → tracks
   - `TRA*BGS` → traction

## raw.py
This python dictionary (requiring the [plover-python-dictionary plugin](https://github.com/benoit-pierre/plover_python_dictionary)) outputs the raw steno strokes with the help of the [plover-dict-commands plugin](https://github.com/KoiOates/plover_dict_commands). Both can be installed from the plugins manager.

After both plugins have been installed and Plover has been restarted, this dictionary should be added to the bottom of the dictionary list (lowest priority), ensuring it is **not** enabled.

Next, add the following entries to a dictionary that is higher in priority (e.g. user.json):

```
"#RA*U": "{plover:solo_dict:+Raw.py}",
"RA*U": "{plover:solo_dict:+Raw.py}{`^}",
```

Stroking `#RA*U` will output the raw steno of all the next strokes until `#RA*U` is stroked again.

If `RA*U` is stroked instead, the output will be surrounded by backticks.

Examples:
 - `RA*U/HEU/THR/HOU/RU/TKO*G/TOED/H-F/RA*U` → `` `HEU/THR/HOU/RU/TKO*G/TOED/H-F` ``
 - `#RA*U/AOEUPL/TKO*G/TPAOEUPB/THAUG/SRE/PHUFP/#RA*U` → `AOEUPL/TKO*G/TPAOEUPB/THAUG/SRE/PHUFP`

Thanks to @sammdot who made this dictionary in the first place :D.

## rh-numpad.json

> I highly recommend mapping the top `S-` key to the number key to make it easier to stroke. This also opens up the possibility for more briefs and decreases hesitation when deciding which finger to use for the number key.

With this dictionary, pressing the number key will turn `-FRPBLG` into a standard keypad with a chorded middle row. The bottom three keys are 1, 2, and 3 (from left to right) while the top three keys are 7, 8, 9 and chording two keys in a column will get 4, 5, and 6 (from left to right). If the `E` key is used in the stroke, 0 will be appended to whatever digit is being chorded. The `U` key will append a 00 on the digit, and `EU` will append a 000 on the digit.

Examples:
 - `#-G/#-R/-FR/#-R/#-PB/#-L` → 314159
 - `#EB` → 20
 - `#UPB`→ 500

## uni-number-reversals.json

This dictionary allows you to write reversals with `U` instead of `EU` which would be impossible using thumber keys on The Uni. This is a supplemental dictionary for the standard number system that comes with `main.json`; it is not compatible with [rh-numpad.json](#rh-numpadjson).

Examples:
 - `#AOU` → 05
 - `#STPU` → 321

## plover-uk.json
Soon™
