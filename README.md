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
 - [Phonetics](#Phonetics)
 - [Orthography](#Orthography)
 - [Syllabic splitting](#Syllabic-splitting)
 - [Exceptions to syllable breaks](#Exceptions-to-syllable-breaks)
 - [Using prefixes and suffixes](#Using-prefixes-and-suffixes)
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

#### Phonetics
The main principles of Plover theory have been left unchanged and Learn Plover! or Art of Chording are fully compatible with this dictionary (apart from word breaks as well as suffixes and prefixes). The following list includes changes I've made as well as any rules or tips not necessarily mentioned in any main learning resources for stock Plover.
 - `*PL` is used as the -mp cluster intsead of `-FRP`
 - Ending sounds that fall out of steno order can be written using right hand consonant strokes
   - `HEL/-P` → help
   - `STRAPBG/-L` → strangle
   - `HEL/-PL` → helm
   - For `-F` and `-T`, asterisk is used to prevent conflicts
     - `TKEL/*F` → delve
     - `HREUPL/*F` → lymph
     - `WURS/*T` → wurst
   - Briefer outlines using compound clusters and inversions are also available and should be preferred
 - `OR` is used for the "or" sound, never `OER`
 - `KWR` is used in certain diphthongs such as:
   - `SREUD/KWROE` → video
   - `AEUR/KWRA` → area
   - `EUPB/SOPL/TPHEU/KWRA` → insomnia
   - `RAOE/KWRAL/TEU` → reality
   - `#PHAR/KWROE` → Mario
   - `HAUP/KWRA` → haupia
     - You may find entries such as `HAU/PEU/KWRA` → haupia;
       - They may be used as fallbacks, but are not recommended as they are longer to write
   - Essentially, if the vowel can be approximated with "Y", it is used
 - `KHUR` is always used for the "chur" sound
   - `HREBG/KHUR` → lecture
   - `KAP/KHUR` → capture
   - `PHA/KHUR` → mature
 - `TWAL` is used for "chwal" sounds found in words like the following that are usually spelled as "-tual":
   - `SPEU/REU/TWAL` → spiritual
   - `AOE/SREPB/TWAL` → eventual
   - `EUPB/TE/HREBG/TWAL` → intellectual
 - Alternatively, `WAL` can be used to represent "-ual" with the T being left to the previous stroke:
   - `SPEU/REUT/WAL` → spiritual
   - `AOE/SREPBT/WAL` → eventual
   - `EUPB/TE/HREBGT/WAL` → intellectual
 - `TK*EU` is always used for the initial `TKEU` sound when starting a word. `TKEU` is reserved for the frays "did I"
   - `TK*EU/REBGT` → direct
   - `TK*EU/HREU/SKWREPBT` → diligent
 - `TP*EU` is used for sounds spelled with "ph" that are pronounced as "F"
   - `TP*EU/SEUBGS` → physics
   - `TP*EU/HRO/SO/TP*EU` → philosophy
 - `EU` is used for long I when it is spelled with an "I" or a "Y"
   - `AR/PE/SKWREU/KWROE` → arpegg**i**o
   - `KUFRB/KWREU` → curvy
   - `PEU/KWRA/TPHOE` → piano
 - `-RBL` is used for the "shl" sound
   - `TK*EU/TPE/REPB/-RBL` → differential
   - `TPAOEU/TPHAPB/-RBL` → financial
 - Non-initial "X" can be written using `-BGS` or some variation of `-BG/S`
   - `EBG/SE/KAOUGS` → execution
   - `EBG/SEU/SKWREPBS` exigence
     - Can also be written `EBG/S*EU/SKWREPBS` with `S*` representing "Z"
   - `EBG/SULT` → exult
     - Can also be written `EBG/S*ULT` with `S*` representing "Z"
   - `EBG/SES` → excess
   - `EBGS/TEPBD` → extend
 - `-PLT` is used for the "-ment" cluster in addition to be being a suffix
   - `SE/-PLT` → cement
   - `KAFP/-PLT` → catchment
   - `EBGS/PE/REUPLT` → experiment
 - `-LT` is used for the "-let" cluster in addition to being a suffix
   - `A/PHAOU/-LT` → amulet
   - `TAB/-LT` → tablet
   - `SKARLT` → scarlet
 - Although a suffix, `-BL` can also be used as a compound cluster for the "-able" or "-ible" sound
   - `KRAOU/-BL` → crucible
   - `PAEURBL` → parable
   - `A/HROUBL` → allowable

#### Orthography
Orthography has also largely been preserved with a few exceptions.
 - Much like stock Plover theory, short vowels and schwas are represented with the vowel they are spelt with despite their sound
   - `SKO/HRAR` → scholar
   - `PWE/TER` → better
   - `WORS` → worse
   - `SU/PORT` → support
   - `PHO/TPHEU/TOR` → monitor
 - Final Z sounds are represented with `-Z` if they are spelt as such or will get around a conflict
   - `SREUS/-BL` → visible
   - `PHEUS/RABL` → miserable
   - `TPHAOEZ` → knees (`TPHAOES` is niece)
   - `SAOEZ` → seize
 - Initial "ph" is represented with `TP*` to differentiate from regular "f"
   - `TPO*E/TOE` → photo
   - `TP*EU/HRO/SO/TP*ER` → philosopher
 - Words starting with "X" are always written with `KP`
   - `KPAOEU/HRO/TPO*EPB` → xylophone
   - `KPEU` → xi

#### Syllabic splitting
main.json relies a lot on dropping unstressed vowels in order to break up words. Words such as "memorize" benefit from a rule like this as the middle syllable is essentially dropped, leaving it unambiguous as to where to break it up: `PHEPL/RAOEUZ`.

For write-outs, this dictionary does not rely as heavily on dropping unstressed vowels, though, this principle is still used for briefer entries.

In order to split a word into multiple strokes syllabically, the following rules should be used:
 - Consonants should not be doubled across strokes
   - e.g., `PHE/PHOR/RAOEUZ` would not be correct as it doubles the R
 - Strokes after the initial one should not begin with a vowel
   - e.g., `PHEPL/OR/AOEUZ` is incorrect, the last two strokes begin with vowels
   - Apart from suffix strokes which are special
     - e.g., `A*R` → "-ar"

In essence, every stroke should begin with a consonant and represent a different syllable of a word. There are, of course, exceptions to these rules which are covered later.

Examples of using the syllabic splitting method:
 - `PHE/PHO/RAOEUZ` → memorize
 - `TPO*E/TPHE/TEUBG` → phonetic
 - `PEUBG/KHUR` → picture
 - `KAL/KAOU/HRAEU/TOR` → calculator
 - `RE/KOG/TPHEUGS` → recognition
 - `ABG/TEUF` → active
 - `AD/HAOE/SEUF` → adhesive
 - `EUPL/POR/TAPBT` → important
 - `OE/PWAEU` → obey
 - `ABG/SES` → access

Sometimes vowels might have to be spread across multiple strokes and it may be impossible to start a stroke with a consonant. If this is the case, use `KWR` as a linker between vowels.
 - `AOEU/KWROE/HREU` → aioli
 - `PEU/KWRA/TPHOE` → piano

Depending on pronuncation, `W` can also begin a consecutive vowel stroke:
 - `AL/TRAOU/WEUS/TEUBG` → altruistic
 - `KOPB/TKAOU/WEUT` → conduit

When it is ambiguous as to whether `W` or `KWR` is used, there should be options for both. Add alternatives to your dictionary if they make sense to you.

However, beware of attempting to rely on `KWR` solely as this is not the point of this dictionary. You will have to add many, many entries.

The following are words that unnecessarily use the `KWR` linker:
 - `TPRAFRPB/KWRAOEUZ` (franchise) ❌
   - `TPRAPB/KHAOEUS` ✔️
 - `EUPB/SAOUL/KWREUPB`(insulin) ❌
   - `EUPB/SAOU/HREUPB` ✔️
 - `HARPS/KWREU/KORD` (harpsichord) ❌
   - `HARP/SEU/KORD` ✔️

#### Exceptions to syllable breaks

Sometimes a stroke should not begin with a certain chord as it is a common brief and would lead to word boundary issues. The following chords should not be used as strokes to start an outline.
 - `KO`
 - `O`
 - `E`
 - `U`
 - `EU`

Instead carry the first stroke far enough so that there is a consonant on the right hand and use other means (such as `KWR` linker or suffixes) to complete the word.
 - `KOL/KWREBGT` → collect
 - `EBG/KWRO/TPHO/PHEUBG` → economic
 - `KOT/O*PB` → cotton

If the first stroke of an outline is a prefix, there is no need to use the `KWR` linker on the next stroke:
 - `KOE/OR/TKEU/TPHAEUT` → coordinate
 - `PRE/EPLT` → preempt
 - `TK*EU/AOE/HREBG/TREUBG` - dielectric
 - `TKEUS/AEUBL` → disable

Consonants can also be doubled if the previous stroke is a prefix and the strokes that follow form a valid word on their own:
 - `TKEUS/SOFLS` → dissolves
 - `TKEUS/SEU/PHEU/HRAR` → dissimilar

When it comes to vowels that are combined with a final `-R`, it may be necessary to use suffix strokes and/or the `KWR` linker in order to preserve the phonetics of the vowel. For example, the word "carry" would have to be written as `KAEUR/KWREU` as the R sound changes the sound of the vowel and thus should be kept in the first stroke.

If the R was treated as a consonant and the split occurred right before it, the outline would be `KAEU/REU` which does not reflect the pronunciation. Thus, if an R changes the sound of a vowel in a word, it is recommended to keep it with the vowel to preserve its sound and instead use the `KWR` linker to complete the next stroke.

The following are some other examples of words where `-R` should be kept in the initial stroke:
 - `#HRAEUR/KWREU` → Larry
 - `#TER/KWREU` → Terry
 - `TOR/KWRUS` → torus
 - `TPHROR/KWREUFT` → florist

An alternative to this would be to split the word before the "R", but treat the previous vowel as a short vowel.
For example:
 - `TPHRO/REUFT` → florist
 - `EBGS/PE/REU/-PLT` → experiment

However, this method is incomplete among entries and may lead to other conflicts and is therefore not recommended.

> For a while this was my preferred method but it proved to be flawed. However, I had already added many entries of this nature to my dictionary which is why they may turn up when using the lookup tool.

#### Using prefixes and suffixes

It is also important to use prefixes and suffixes.

A good rule of thumb to determine whether or not it is appropriate to use suffix strokes is to examine what will be written before the suffix stroke.

For example, it should be apparent that the word "tester" can be broken into the root word "test" and the suffix "-er" and thus should be written `TEFT/*ER` as opposed to `TES/TER`. On the other hand, the word "termite" should be written syllabically since it can't be broken into smaller parts: `TER/PHAOEUT`.

> NOTE: With `KWRAOEUT` being the "-ite" suffix, it is technically possible to write "termite" as `TERPL/KWRAOEUT` but that is against the principles of this dictionary. If it is desirable to you to write in this manner, then this dictionary is probably not for you.

It should be apparent that the following words should be written with suffix strokes as opposed to syllabically:
 - `HRERPB/*ER` → learner
   - `*ER` → "-er"
 - `SE/HREBGT/-BL` → selectable
   - `-BL` → "-(a|i)ble"
 - `KUT/-G` → cutting
   - `-G` → "-ing"
 - `TPHAOEUF/-S` → knives
   - `-S` → "-s"
 - `KAFP/-PLT` → catchment
   - `-PLT` → "-ment"
 - `RE/SPOPBD/KWREPBT` → respondent
   - `KWREPBT` → "-ent"
 - `TKEUBGS/KWRAEUR/KWREU` → dictionary
   - `KWRAEUR/KWREU` → "-ary"

On the other hand, the following are words which should be written syllabically:
 - `STAOUD/KWREPBT` (student) ❌
   - `STAOU/TKEPBT` ✔️
 - `WAUT/*ER` (water) ❌
   - `WAU/TER` ✔️
 - `SKOL/A*R` (scholar) ❌
   - `SKO/HRAR` ✔️

For ambiguous situations where it is not clear whether to use suffixes or split a word syllabically, both options should be available to use. And of course, don't be afraid to add your own alternatives.

#### Prefixes and suffixes
 - Since doubling consonants isn't used, `KWREU` is default for adding "-y"
   - `KEUT/KWREU` → kitty
   - `STOR/KWREU` → story
 - `OER` is used for the "-ory" sound
   - `SA/TEUS/TPABG/TOER` → satisfactory
   - `TPABG/TOER` → factory
   - `TPABGT/KWROER` → factory (using the {^ory} suffix)
 - `O*R/KWREU` can still be used for the "-ory" suffix
   - `AU/TKEU/TOR/KWREU` → auditory
   - `AU/TKEUT/O*R/KWREU` → auditory (using the {^ory} suffix)
 - `KWREPB` → "-en"
   - `HRAOEUT/KWREPB` → lighten
   - `SOFT/KWREPB` → soften
 - `KWREPBT` → "-ent"
   - `A/STREUPBG/KWREPBT` → astringent
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
     - Also can be written `#KHREUS/TEU`
 - "x" and "ks" gets precedence over "kshun" in" `-BGS`
   - `TRABGS` → tracks
   - `TRA*BGS` → traction
   - `RE/TPHREBGS` → reflex
   - `RE/TPHR*EBGS` → reflection
> The one exception to this rule is `TKEUBGS` → diction as I want to be able to write "dictionary" as `TKEUBGS/KWRAER`. Seeing "dicks" show up before writing `KWRAER` seems silly.

## raw.py
This python dictionary (requiring the [plover-python-dictionary plugin](https://github.com/benoit-pierre/plover_python_dictionary)) outputs the raw steno strokes with the help of the [plover-dict-commands plugin](https://github.com/KoiOates/plover_dict_commands). Both can be installed from the plugins manager.

After both plugins have been installed and Plover has been restarted, load the dictionary ensuring that it is **not** enabled. Next, add the following entries to a dictionary that is higher in priority (e.g. user.json):

```
"#RA*U": "{plover:solo_dict:+raw.py}",
"RA*U": "{plover:solo_dict:+raw.py}{`^}",
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

When holding down left hand `P` with this number pad, numbers will be treated like regular translations and will not glue to one another.

Examples:
 - `#-G/#-R/-FR/#-R/#-PB/#-L` → 314159
 - `#P-G/#P-R/#P-6R/#P-R/#P-7B/#P-8` → 3 1 4 1 5 9
 - `#EB` → 20
 - `#UPB`→ 500

## uni-number-reversals.json

This dictionary allows you to write reversals with `U` instead of `EU` which would be impossible using thumber keys on The Uni. This is a supplemental dictionary for the standard number system that comes with `main.json`; it is not compatible with [rh-numpad.json](#rh-numpadjson).

Examples:
 - `#AOU` → 05
 - `#STPU` → 321

## plover-uk.json
Soon™
