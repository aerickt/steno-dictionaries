# Steno Dictionaries
My personal steno dictionaries.
 - [commands.json](#commandsjson)
 - [ip.py](#ippy)
 - [lapwing-base.json](#lapwing-basejson)
 - [lapwing-uk-additions.json](#lapwing-uk-additionsjson)
 - [movement.modal](#movementmodal)
 - [raw.py](#rawpy)
 - [rh-numpad.json](#rh-numpadjson)
 - [uni-number-reversals.json](#uni-number-reversalsjson)
 - [viet.json](#vietjson)

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

## ip.py

Write `#AOEUP` to output the local IP address of the machine Plover is running on. Useful on a headless [Stenogotchi](https://github.com/Anodynous/stenogotchi) that doesn't have a screen.

Requires [plover-python-dictionary plugin](https://github.com/benoit-pierre/plover_python_dictionary) as well as the `netiface` python package (must be installed from the command-line).

It uses `netiface` because that was the most reliable way I could get it to work.

## lapwing-base.json

This dictionary is a derivative of Plover's `main.json` that is intended to act as a replacement. It has over 111k entries and is sufficient for most everyday writing. Lapwing differs from stock Plover theory in a few ways. I have listed core principles and changes on this page.

> I manually built this dictionary over the course of 6 months on and off. Please let me know if you spot any errors or misleading entries to correct!

I've written a bit about my motivations in a quick summary of this project over on my [website](https://aerick.ca/steno/dictionary-building).

### Dictionary contents

 - [Who should use this dictionary?](#who-should-use-this-dictionary)
 - [Main changes and advantages](#main-changes-and-advantages)
 - [Using this dictionary](#using-this-dictionary)
 - [Compound words](#compound-words)
 - [Proper nouns](#proper-nouns)
 - [Movement keys, keyboard shortcuts, commands](#movement-keys-keyboard-shortcuts-commands)
 - [Punctuation](#punctuation)
 - [Right hand number pad](#right-hand-number-pad)
 - [Fingerspelling](#fingerspelling)
 - [Phonetics](#phonetics)
 - [Orthography](#orthography)
 - [Syllabic splitting](#syllabic-splitting)
 - [Exceptions to syllabic splitting](#exceptions-to-syllabic-splitting)
 - [Using prefixes and suffixes](#using-prefixes-and-suffixes)
 - [Prefixes](#prefixes)
 - [Suffixes](#suffixes)
 - [Conflict resolution](#conflict-resolution)
 - [Beyond writing out](#beyond-writing-out)

#### Who should use this dictionary?

I believe this dictionary will make it easier for beginners to pick up stenography due to the following reasons I outline [below](#Main-changes-and-advantages). However, this reference page is the only learning resource specific to this dictionary and thus learning the bulk of the theory will be done through reading this page or [looking up](#Using-this-dictionary) entries.

> I would consider using this dictionary only if you are the type that likes to figure things out by themselves. If you instead prefer learning by being guided through a step by step process, this is not the dictionary for you. Furthermore, I would definitely recommend skimming through some of the contents on this page. There are quite a few differences between this and stock Plover theory which you should take into consideration.

Before studying this page, it is necessary to know the main missing sounds and compound clusters of Plover theory. Many of the examples will not make sense without prior knowledge of the steno layout. These can be learned from reading Art of Chording or Learn Plover!. I recommend reading the latter as that is what I am familiar with. It is only necessary to read up to the end of lesson 3 in order to proceed with this dictionary.

#### Main changes and advantages

##### Consistent syllabic write-outs

When it comes to writing out, main.json sometimes prefers using prefixes and suffixes, sometimes splits with syllables, and is also sometimes right hand greedy. Furthermore, most write-out entries drop unstressed vowels.

Lapwing eliminates the ambiguity by having a consistent and predictable method of writing out syllabically (with some exceptions) without having to determine stress within a word.

##### Free of misstrokes

The default Plover dictionary came from Mirabai Knight's own personal dictionary several years ago. As such, main.json is full of misstroke entries. When writing at speed, a stenographer may accidentally miss a key, or press a wrong key in a specific outline regularly. To help combat this, they may add these wrong outlines to their dictionary to ensure the intended translation is outputted. These are known as "misstroke entries" or just "misstrokes" and work as a kind of passive autocorrection.

Although helpful to those already comfortable with theory, they are detrimental to beginners who may have trouble determining which outlines are correct. Many learn by simply looking up outlines in the dictionary, especially hobbyist stenographers. Having a dictionary where all the entries are correct is extremely important.

##### Fewer inconsistencies

In addition to being full of misstrokes, main.json also has many inconsistent rules that work for some words, but not for others. Especially when it comes to breaking up a word into multiple strokes, main.json just doesn't have a consistent method. Looking up a word will result in a multitude of ways to write a word. Leaving it up to the user to decide how to break up a word would be fine on its own if the dictionary contained every single method. However, that is just not the case with many of these alternative word breaks missing.

In this dictionary, write-outs adhere to splitting rules a lot more closely. Write-outs for one word will resemble write-outs for other similar words and there are often no more than a few entries for writing out.

##### More consistent prefixes and suffixes

Prefixes in Lapwing will generally be working in the background, so to speak. They are not entries one will have to memorize, but rather come as a result of the syllabic splitting method. For example, "conserve" would be written out as `KOPB/SEFRB` but it is not necessary to know that `KOPB` is the "con-" prefix.

Suffixes, however, do need to be slightly more unique as they have to be differentiated from normal words. Most common suffixes, however, are fairly regular and form "families" of outlines that are similar to one another. See [suffixes](#suffixes) for examples.

#### Using this dictionary

Download this dictionary by right clicking [here](https://github.com/aerickt/steno-dictionaries/raw/main/lapwing-base.json) and pressing "save link". Ensure that the file is saved as json and not just a text file. Afterwards, it can be added to Plover's dictionary stack and `main.json` can be removed or disabled.

You will also want to install the plover-stitching plugin (see [fingerspelling](#fingerspelling)) and the plover-last-translation plugin. The latter of which allows you to repeat the last translation (multistroke outlines included) just by pressing the number key.

> Since this page is the only place to learn the theory that comes with this dictionary, I recommend keeping it bookmarked and coming back regularly. If you find a quirk in the lookup tool that doesn't sit right with you, consult this page first. If an entry still seems to be wrong, feel free to either comment on the (Lapwing Suggestions)[https://github.com/aerickt/steno-dictionaries/issues/1] thread or contact me on Discord (aerick#3063) through the [Plover Discord Server](https://discord.gg/NAzMz7C3wq). New vocab additions are also welcome.

When it comes to looking up entries, the best strategy would be to look at the longest definition as this corresponds to the fully written-out outline.

For example, looking up the word "personality" will result in the following:

```
PER/SO*PB/A*L/TEU
PER/SO*PB/A*LT
PER/SOPB/A*L/TEU
PER/SOPB/A*LT
PERPB/A*LT
PERPBLT
PERS/TPHAL/TEU
PERS/TPHALT
```

The two outlines you should consider as fully written-out would be `PER/SO*PB/A*L/TEU` and `PER/SOPB/A*L/TEU`. The other outlines are briefer or use other techniques that are not utilized when it comes to writing out words.

One more thing about this dictionary is that words are often defined with folded suffix keys. For example, take the word "recreating":

```
"RAOE/KRAOE/KWRAEUGT": "recreating",
"RAOE/KRAOEGT": "recreating",
"RE/KRAOE/KWRAEUGT": "recreating",
"RE/KRAOEGT": "recreating",

```

Although these all include folded suffix keys, it is **not** necessary to keep `-G` from being its own stroke! Even though `RAOE/KRAOE/KWRAEUT/-G` is not defined in the dictionary, it will still work. Same goes for `-S`, `-D`, and `-Z`. Folding is more of an [advance technique](#Folding-suffix-keys) that is discussed more later. Folding can potentially lead to conflicts and so it is not something that is recommended to do as a beginner.

#### Compound words

Compound words are always written with the asterisk on the first stroke of the second word.
 - `KAOE/PWAO*RD` → keyboard
 - `TEGT/PWAO*BG` → textbook
 - `PHOUS/PA*D` → mousepad
 - `STOR/KWREU/PWAO*BG/-S` → storybooks

#### Proper nouns

Proper nouns are always written with the number key on the first stroke. Everything else is written with the same rules.
 - `#A/HREU/SA` → Alyssa
 - `#PWOB` → Bob
 - `#PAOE/TER` → Peter
 - `#AP/-L` → Apple
 - `#AUS/TRAEUL/KWRA` → Australia
 - `#HART/PHAPB` → Hartman

> I highly recommend mapping the top `S-` key to the number key to make it easier to stroke. This also opens up the possibility for more briefs and decreases hesitation when deciding which finger to use for the number key.

Unfortunately, due to how Plover handles the number key entries using the number key will not be displayed as shown above. When using the number key, the top row of keys plus `A` and `O` are converted to numbers and are stored as such in the dictionary. Looking up "Bob" in the dictionary will result in `3W0B` instead of `#PWOB`

#### Movement keys, keyboard shortcuts, commands

See [commands.json](#commandsjson). Lapwing contains everything from this dictionary by default.

#### Punctuation

The following is a list of commonly used punctuation marks characters.
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

> The conventional number system does not work in lapwing-base.json. You will have to delete all entries containing the glue operator and a number (e.g. `{&8}`) if you want to use the conventional number system.

lapwing-base.json has this system by default. See [rh-numpad.json](#rh-numpadjson).

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

The main principles of Plover theory have been left unchanged and Learn Plover! or Art of Chording are fully compatible with this dictionary (apart from word breaks as well as suffixes and prefixes). Although this list is quite long, a lot of these principles are actually part of stock Plover theory which I thought were worth mentioning.
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
     - Entries such as `HAU/PEU/KWRA` (haupia) can be found in the dictionary as fallbacks but are not recommended due to being longer to write.
   - Essentially, `KWR` is used if the vowel can be approximated with "Y"
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
 - `TK*EU` is always used for the initial `TKEU` sound when starting a word. `TKEU` is reserved for the phrase "did I"
   - `TK*EU/REBGT` → direct
   - `TK*EU/HREU/SKWREPBT` → diligent
 - `TP*EU` is used for sounds spelled with "ph" that are pronounced as "F"
   - `TP*EU/SEUBGS` → physics
   - `TP*EU/HRO/SO/TP*EU` → philosophy
 - `EU` is used for long E when it is spelled with an "I" or a "Y"
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
   - `EBGS` cannot be used universally due to syllabic splitting constraints (see [Syllabic splitting](#Syllabic-splitting))
 - `-PLT` is used for the "-ment" cluster in addition to be being a suffix
   - `SE/-PLT` → cement
   - `KAFP/-PLT` → catchment
   - `EBGS/PE/REUPLT` → experiment
 - `-LT` is used for the "-let" cluster in addition to being a suffix
   - `A/PHAOULT` → amulet
   - `KHEUBG/-LT` → chiclet
   - `SKARLT` → scarlet
 - `-BL` can be used for the "-able" or "-ible" cluster in addition to being a suffix
   - `KRAOUS/-BL` → crucible
   - `PAEURBL` → parable
   - `A/HROUBL` → allowable
 - `TEU` can be used for the "-ity" cluster in addition to being a suffix
   - `SKAEURS/TEU` → scarcity
   - `STEU` → city
   - `EUPB/SAPB/TEU` → insanity
 - Some variation of `US` is used for the "us" sound whether it is spelled "ous" or "us"
   - `PHO/TPHO/TO/TPHUS` → monotonous
   - `STAOU/PEPB/TKUS` → stupendous
   - `TOR/KWRUS` → torus
   - `RAOEUT/KHUS` → righteous
 - `AU` is used for the "aw" vowel when not spelled with "O"
   - `PWAUT` → bought
   - `PWRAUD` → broad
   - `PAUPL` → palm

#### Orthography

Orthography has also largely been preserved with a few exceptions.
 - Much like stock Plover theory, short vowels and schwas are represented with the vowel they are spelt with despite their sound
   - `SKO/HRAR` → scholar
   - `PWE/TER` → better
   - `WORS` → worse
   - `SU/PORT` → support
   - `PHO/TPHEU/TOR` → monitor
 - Final Z sounds are represented with `-Z` if they are spelt as such or help to get around a conflict
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
 - Words beginning with "Y" use `KWR`
   - `KWREP` → yep
   - `KWRERPB` → yearn
   - Other words drop `KWR`
     - `AOU/TPO*R/KWRA` → euphoria
     - `AOUS` → use
     - `UR/KWREUPB` → urine
 - Words beginning with capital "J" can use `#STKPW` as an alternative to `#SKWR`
   - `#STKPW/TPHEUS` → Janice
   - `#STKPW/PHAEU/KA` → Jamaica
 - Common contractions use asterisk when there's a conflict
   - `WAOER` → weir
   - `WAO*ER` → we're
   - `HAOEL` → heel
   - `HAO*EL` → he'll
   - For the most part, contractions are just written phonetically, but asterisked variants do exists for all of them as well
     - For example, `AOEUL` works for "I'll" `AO*EUL` does as well

#### Syllabic splitting

main.json relies a lot on dropping unstressed vowels in order to break up words which is a bit of a challenge to learn especially for non-native speakers.

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

When it is ambiguous as to whether to use `W` or `KWR`, outlines containing both should be available.

> Add alternatives to your dictionary if none of the available are intuitive to you.

However, beware of attempting to rely too heavily on linker chords as this dictionary does not use them universally. Attempting to use them excessively will result in thousands of entries needing to be added.

The following are words that unnecessarily use the `KWR` linker:
 - `TPRAFRPB/KWRAOEUZ` (franchise) ❌
   - `TPRAPB/KHAOEUS` ✔️
 - `EUPB/SAOUL/KWREUPB`(insulin) ❌
   - `EUPB/SAOU/HREUPB` ✔️
 - `HARPS/KWREU/KORD` (harpsichord) ❌
   - `HARP/SEU/KORD` ✔️
 - `TKPWAL/KWROPB` (gallon) ❌
   - `TKPWA/HROPB` ✔️

#### Exceptions to syllabic splitting

##### Strokes not to be used when starting outlines

Sometimes it is undesirable for the beginning of an outline to use a stroke due to conflicts. For example, `KO/HREBGT` conflicts with the word "collect" and the phrase "could elect". The following chords should not be used as strokes to start an outline.
 - `KO`
 - `O`
 - `E`
 - `U`
 - `EU`

Instead carry the first stroke far enough so that there is a consonant on the right hand and use other means (such as `KWR` linker or suffixes) to complete the word.
 - `KOL/KWREBGT` → collect
 - `EBG/KWRO/TPHO/PHEUBG` → economic
 - `EUL/KWRAOUGS` → illusion
 - `KOT/KWROPB` → cotton

##### `KWR` linker with prefix strokes

If the first stroke of an outline is a prefix, there is no need to use a linker chord such as `KWR` on the next stroke:
 - `KOE/OR/TKEU/TPHAEUT` → coordinate
 - `PRE/EPLT` → preempt
 - `TK*EU/AOE/HREBG/TREUBG` - dielectric
 - `TKEUS/AEUBL` → disable

##### Consonant doubling with prefixes

Consonants can be doubled if the previous stroke is a prefix and the strokes that follow form a valid word on their own:
 - `TKEUS/SOFLS` → dissolves
 - `TKEUS/SEU/PHEU/HRAR` → dissimilar

> Of course, if it makes sense to you to disregard this exception then feel free to add entries such as `TK*EU/SEU/PHEU/HRAR` → dissimilar to your dictionary.

##### Consonant doubling with "ng"

Words with "ng" such as "mango" would not be able to be defined accurately if consonants could not be doubled across strokes. Thus it is acceptable for these words to double the "G" across strokes:
 - `PHAPBG/TKPWOE` → mango
 - `TPEUPBG/TKPWER` → finger
 - `SEUPBG/TKPWAOU/HRAR` → singular

##### The problem of the vowel/consonant "R"

When it comes to vowels that are combined with a final `-R`, it may be necessary to use suffix strokes and/or the `KWR` linker in order to preserve the phonetics of the vowel. For example, the word "carry" would have to be written as `KAEUR/KWREU` as the R changes the sound of the vowel and thus should be kept in the first stroke.

If the R was treated as a consonant it was instead split as "ca|rry", the outline could only be `KAEU/REU` or `KA/REU`  which are not completely accurate to the pronunciation. Thus, if an R changes the sound of a vowel in a word, it is recommended to keep it with the vowel to preserve its sound and instead use the `KWR` linker to complete the next stroke.

The following are some other examples of words where `-R` should be kept in the initial stroke:
 - `#HRAEUR/KWREU` → Larry
 - `#TER/KWREU` → Terry
 - `TOR/KWRUS` → torus
 - `TPHROR/KWREUFT` → florist

> NOTE: keeping the `-R` in the stroke with the vowel only applies to words where the "R" actually changes the pronunciation of the vowel. For example, the second "R" in "periphera" doesn't change the vowel significantly so it is acceptable to split it as `PE/REU/TP*E/RA`. That said, `PE/REU/TP*ER/KWRA` is also defined as it is somewhat ambiguous.

##### Situations that benefit from dropping unstressed vowels

As previously mentioned in [phonetics](#Phonetics), `TEU` can be used to represent -ity even if not used as a suffix. This is very much a situation that is actually dropping an unstressed vowel in disguise. Consider the two outlines of writing "felicity":
 - `TPE/HREUS/TEU`
 - `TPE/HREU/SEU/TEU`

Notice that in the first outline, the second "i" was dropped as it is unstressed. The second outline is not recommended as it uses an extra stroke, making it slower to write.

Furthermore, entries with strokes that take the shape of `EU/TEU` are not necessarily complete as I may have been too tired or lazy when trying to add these in. Thus, try to not use an extra stroke when it comes to `TEU`.

Other examples of when to drop an "i" in such a manner:
 - `EBGS/TRE/PHEU/TEU` → extremity
   - Can instead be `EBGS/TREPL/TEU`
 - `EUPB/TPEU/TPHEU/TEU` → infinity
   - Can instead be `EUPB/TPEUPB/TEU`
 - `SEPB/SEU/TEUF` → sensitive
   - Can instead be `SEPBS/TEUF`

Another situation where you should really drop a vowel is where you'll see a word end with -ly.
 - `HAUT/KWREU/HREU` → haughtily
   - Can instead be `HAUT/HREU` ("i" is dropped)
 - `TRAO*UT/-FL/KWREU` → truthfully
   - Can instead be `TRAO*UT/TPHREU` (second "u" is dropped)
 - `PER/SO*PB/A*L/KWREU` → personally
   - Can instead be `PER/SO*PB/HREU` ("a" is dropped)

#### Using prefixes and suffixes

It is also important to use prefixes and suffixes.

A good rule of thumb to determine whether or not it is appropriate to use suffix strokes is to examine what will be written before the suffix stroke.

For example, it should be apparent that the word "tester" can be broken into the root word "test" and the suffix "-er" and thus should be written `TEFT/*ER` as opposed to `TES/TER`. On the other hand, the word "termite" should be written syllabically since it can't be broken into smaller parts: `TER/PHAOEUT`.

> NOTE: With `KWRAOEUT` being the "-ite" suffix, it is technically possible to write "termite" as `TERPL/KWRAOEUT` but that is against the principles of this dictionary. If it is desirable to you to write in this manner, then this dictionary is probably not for you.

The following list of words are other examples where suffixes should be used instead of syllabic splitting:
 - `HRERPB/*ER` → learner
   - `*ER` → "-er"
 - `SE/HREBGT/-BL` → selectable
   - `-BL` → "-able"
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

On the other hand, the following are examples of incorrect suffix usage:
 - `STAOUD/KWREPBT` (student) ❌
   - `STAOU/TKEPBT` ✔️
 - `WAUT/*ER` (water) ❌
   - `WAU/TER` ✔️
 - `SKOL/A*R` (scholar) ❌
   - `SKO/HRAR` ✔️

For ambiguous situations where it is not clear whether to use suffixes or split a word syllabically, both options should be available to use. And of course, don't be afraid to add your own alternatives.

#### Prefixes

As previously mentioned, prefix strokes are not outlines that usually have to be memorized. Most common prefix strokes come about when splitting words syllabically and don't need much thought. For example, "ex-", "super-", and "hetero-" are written as `EBGS`, `SAOU/PER`, and `HE/TER/KWROE`, respectively, as if they were just regular words. With a basic grasp of syllabic splitting, most prefixes should be fairly straightforward.

There are, of course, a few prefixes that are not able to be defined normally due to conflicts such as the ones listed below:
 - `TK*EU` → di-
 - `PW*EU` → bi-
 - `TR*EU` → tri-
 - `AUPB` → on-
 - `AUF` → off-

> NOTE: Words such as "offhand" and "online" can also be written as regular compound words: `OF/HA*PBD`, `OPB/HRAO*EUPB`.

There can also sometimes be multiple entries for the same prefix such as `PRE` and `PRAOE` for "pre-" or `UL/TRA` and `ULT/RA` for "ultra-". Whichever works best for a given situation should be used and multiple options are available if there is ambiguity.

##### Prefixes by themselves

Sometimes it is needed to write a prefix outline as a regular word. Take, for example, "super". This can be a prefix as in "supernatural" or a regular word as in "super awesome". Since syllabic splitting will go to the prefix form, asterisk is used on the last stroke to obtain the word form.

Thus, `SAOU/PER/AU/SOPL` would output "superawesome" while `SAOU/P*ER/AU/SOPL` would output "super awesome".

> As you write more and more using this dictionary, you will encounter many situations where you intended a word instead of a prefix stroke to be written. When this happens, take note of the prefix and remember the usage of asterisk to prevent this in future.

If the prefix form of an outline is accidentally written when the word form was intended, [asterisk can be toggled retroactively](https://github.com/openstenoproject/plover/wiki/Dictionary-Format#toggle-asterisk) using `#*` instead of deleting the whole word and starting over.

For example, consider the attempt to write "super awesome":

`SAOU/PER/AU/SOPL`

Instead of pressing the asterisk 4 times and rewriting the entire word, an alternative would be to backspace the last two strokes, toggle asterisk with `#*` to get the word form, and continue with "awesome":

`SAOU/PER/AU/SOPL/*/*/#*/AU/SOPL` (9 strokes)

`SAOU/PER/AU/SOPL/*/*/*/*/SAOU/P*ER/AU/SOPL` (12 strokes)

#### Suffixes

Unlike prefixes, most suffixes do have to be memorized but are quite predictable with many following patterns.

The following inexhaustive list contains common suffix strokes that should be sufficient for most everyday writing:
 - `KWREU` → -y
   - `KRAEUZ/KWREU` → crazy
 - `KWREUF` → -ive
   - `KRAOE/KWRAEUT/KWREUF` → creative
 - `KWREUFPL` → -ism
   - `PHAG/TPHET/KWREUFPL` → magnetism
 - `KWREUPB` → -in
   - `PHRUG/KWREUPB` → plugin
 - `KWREUBG` → -ic
   - `AOEU/KWROPB/KWREUBG` → ionic
 - `KWREUFT` → -ist
   - `ART/KWREUFT` → artist
 - The following outlines are primarily used in syllabic splitting with `KWR` representing a diphthong like in words such as "obsidian" (`OB/SEUD/KWRAPB`). However, by themselves, these outlines are defined without an initial "I" as shown below:
   - `KWROPB` → -on
   - `KWRAPB` → -an
   - `KWRAPBT` → -ant
   - `KWREPB` → -en
   - `KWREPBT` → -ent

> If you come across a word that needs to be defined using one of the above suffixes, use them as is regardless of if a diphthong is present in its pronunciation. For example, "harden" and "alien" would be defined as `HARD/KWREPB` and `AEUL/KWREPB`, respectively. The suffix is still the same regardless of if an "I" is present in their spelling. However, if you need to end an arbitrary word with one of the above suffixes with a leading "I", use an asterisk on the suffix stroke. For example, "hardan" would be written as `HARD/KWRAPB` while "hardian" would be written as `HARD/KWRA*PB`.

 - `A*R` → -ar
 - `A*L` → -al
 - `AEUGS` → -ation
 - `O*R` → -or
 - `*ER` → -er
 - `-PLT` → -ment
 - `-PBS` → -ness
 - `-BL` → -able
 - `-BLT` → -ability
 - `-L` → -le
 - `-LT` → -let
 - `-G` → -ing
 - `-S` → -s
 - `-Z` → -s
 - `ST-BG` → -istic
 - `SH-PBS` → -ishness
 - `SH*EUP` → -ship

#### Conflict resolution

If two homophones must be resolved using asterisk, there are a few aspects of each word that will decide which word gets precedence.

If there are repeat letters in a word, that will use asterisk
 - `#HART/PHAPB` → Hartman
 - `#HART/PHA*PB` → Hartmann

If two words differ in a vowel, (especially with Y or I), the asterisk will go to the word that doesn't match the vowel as spelt
 - `#HREUPB` → Lin
 - `#HR*EUPB` → Lynn

 "kr" gets precedence over "chr" and "cr" in `KR-` as it matches the keys more
 - `#KREUS/TEU` → Kristy
 - `#KR*EUS/TEU` → Christy
   - Also can be written `#KHREUS/TEU`

"x" and "ks" gets precedence over "kshun" in" `-BGS`
 - `TRABGS` → tracks
 - `TRA*BGS` → traction
 - `RE/TPHREBGS` → reflex
 - `RE/TPHR*EBGS` → reflection
 - > The one exception to this rule is `TKEUBGS` → diction; I like being able to write "dictionary" as `TKEUBGS/KWRAER`. Seeing "dicks" show up before writing `KWRAER` seems silly.

For conflicts with words ending "i" vs "y", use `EU` and `KWREU` respectively
 - `#TE/REU` → Terri
 - `#TER/KWREU` → Terry
 - `#SAPL/KWREU` → Sammy
 - `#SA/PHEU` → Sammi

#### Beyond writing out

It's no secret that writing out syllabically can be quite slow. This dictionary does have some techniques for writing significantly shorter.

##### Dropping unstressed vowels

This technique has already been somewhat illustrated in [Situations that benefit from dropping unstressed vowels](#situations-that-benefit-from-dropping-unstressed-vowels). Figuring out stress can be a bit of a challenge within a word and I unfortunately do not have any tips at this moment, apart from showing a few examples:
 - `PHEPL/RAOEUZ` → memorize ("o" is dropped)
 - `T*EPL/RAEUR/KWREU` → temporary ("o" is dropped)
 - `TPOFRPB/TPHAT` → fortunate ("u" is dropped)
 - `KPHAPBD` → command ("o" is dropped and remaining word is fit into one stroke)
 - `KPHAOUPB/KAEUT` → communicate (both the "o" and the "i" are dropped)
 - `STKAOEUR` → desire ("e" is dropped, and `STK` serves as "ds" using an inversion)
 - `STKPAOER` → disappear ("i" and first "a" are both dropped, `STK` serving as "ds" using an inversion)
 - `RUFR` → rougher ("e" is dropped, `-FR` representing the "fer" sound)
 - `TKEUFRPBT` → different (both "e"'s are dropped, remaining consonants fit into single stroke)
 - `EBGS/PERPLT` → experiment ("i" is dropped)

##### Using shorter prefixes and suffixes

Most prefixes are simple to determine but may take multiple strokes. For example, `PHE/TKPWA` is the mega- prefix which is logical and predictable. However, a stroke can be saved by using `PH*EG` instead.

A few examples are listed below:
 - `PHEU/HREU` → milli-
   - `PH*EUL` can instead be used
 - `KEU/HROE` → kilo-
   - `K*EUL` can instead be used
 - `RE/TROE` → retro-
   - `RERT` can instead be used

Suffixes can be shortened in much the same way.

For example, the canonical way of writing "dictionary" is `TKEUBGS/KWRAEUR/KWREU` with `KWRAEUR/KWREU` representing the -ary suffix. `KWRAER` serves as a shorter alternative as seen in the following examples:
 - `TKO/KAOU/-PLT/KWRAER` → documentary
 - `TKEUS/PEPBS/KWRAER` → dispensary
 - `SREUGS/KWRAER` → visionary

-ory can also be shortened to `KWROER`:
 - `TPABGT/KWROER` → factory
 - `PRE/EPLT/KWROER` → preemptory
 - `STA/KHAOUT/KWROER` → statutory

`AER` and `OER` are also special in that they are not just parts of suffixes, but can represent the sounds of  -ary and -ory when combined with other consonants.

 - `EUPB/SREPB/TOER` → inventory
 - `OB/HREU/TKPWA/TOER` → obligatory
 - `UPB/TPHE/SE/SAER` → unnecessary
 - `ES/KHAOU/WAER` → estuary

> Using `AER` and `OER` are great ways to shorten your writing! Whenever you write `____AEUR` or `____OR` followed by `KWREU`, remember that these can all be compressed into one stroke!

##### Folding and stacking sounds on ending strokes

Ending consonants on the right hand can be combined with ending strokes to fit more sounds into one stroke. For example, `-T` can be used to represent -ity conjunction with other chords:
 - `PRAOEU/KWRORT` → priority
 - `SAOEPB/KWRORT` → seniority
 - `EUPB/SAPBT` → insanity
 - `PHOE/HRAERT` → molarity

`-L` can be used in a similar manner to represent -al or -ly:
 - `EBGS/TERPBL` → external
 - `EUPL/PHORL` → immoral
 - `EUPL/PEURBL` → impishly
 - `RAOE/SPEBG/TEUFL` → respectively

`-R` can be used to represent an ending R sound:
 - `SOFT/KWRERPB` → softener
 - `OERPB` → owner
 - `KHRAOERPB` → cleaner
 - `TKAOEURPB` → diner

##### Folding suffix keys

Folding suffix keys can come with unintended conflicts (for example, `SPEUGT` for "spitting" vs "spigot") but it is an easy way to reduce how many strokes you use. That said, hitting `-G`, `-S`, `-D`, or `-Z` separately is already quite fast. Folding these keys often requires more finger contortions. Do not feel obliged to fold suffix keys, despite the dictionary containing these entries.

##### Examples of short entries that I might use

The following words are a few examples of some of using two or more techniques above to form short entries. They should demonstrate how you can write shorter without having to memorize a bunch of briefs or suffix strokes.
 - `T*EPL/RAERL` → temporarily
   - Dropping the unstressed "o", using the "AER" compound cluster, and folding a `-L` to represent "-ly"
   - Written-out form: `TEPL/POR/KWRAEUR/KWREU/HREU`
 - `KA*LG/HRAEUGT` → calculating
   - Dropping the unstressed "u" and folding the `-G` suffix key
   - Written-out form: `KAL/KAOU/HRAEUT/-G`
 - `TAEURLG` → tailoring
   - Dropping the unstressed "o" and folding the `-G` suffix key
   - Written-out form: `TAEU/HROR/-G` or `TAEUL/O*R/-G`
 - `KOR/KWRARPBD` → coriander
   - Using `KWR` to represent the "i" and folding in `-R` to represent the "er"
   - Written-out form: `KOR/KWREU/KWRAPB/TKER`
 - `AL/TERPB/TEUFL` → alternatively
   - Dropping the unstressed second "a" and folding a `-L` to represent "-ly"
   - Written-out form: `AL/TER/TPHA/TEUF/HREU`
 - `ERTD` → editor
  - Dropping the unstressed "i" and folding in `-R` to represent the "or"
  - Written-out form: `ED/KWREUT/O*R`

## lapwing-uk-additions.json

By default `lapwing-base.json` mainly only contains American spellings of words. This dictionary allows for both American and British spellings without having to switch dictionaries.

> I have made this dictionary mainly with Canadians and Australians in mind. If you primarily write British spellings, then this dictionary might not be ideal foryou.

### Dictionary contents

 - [Switching with `#TPH`](switching-with-tph)
 - [ae spellings](#ae-spellings)
 - [ise spellings](#ise-spellings)
 - [ll spellings](#ll-spellings)
 - [oe spellings](#oe-spellings)
 - [ou spellings](#ou-spellings)
 - [re spellings](#re-spellings)
 - [Miscellaneous briefs](#miscellaneous-briefs)

### Switching with `#TPH`

Writing `#TPH` after any translation will switch the previous word into its British variant (if it exists in the dictionary).

Unfortunately, there is currently a limitation that requires all suffix keys (`-G`, `-S`,`-D` and `-Z`) to either be folded into the last stroke or written after the `#TPH` chord.

For example, the following attempt to write "accessorising" will not work:
 - `ABG/SE/SOR/KWRAOEUZ/-G/#TPH`

Instead write it as either of the following:
 - `ABG/SE/SOR/KWRAOEUZ/#TPH/-G`
 - `ABG/SES/KWROR/KWRAOEUGZ/#TPH`

Using `#TPH` is the recommended method that will always work when switching to British spellings. There are a few shorter models listed below, but they are not guaranteed to always work.

### ae spellings

Regardless of pronunciation, words that are spelled with "ae" can be written with `AE`

Examples:
 - `EPB/SAOEU/KHROE/PAE/TKEU/KWRA` → encyclopaedia
 - `AET/KWROLG` → aetiology

### ise spellings

Words spelled with "ise" use `AOEUS` and `AOEUF` when folding in ending sounds.

Examples:
 - `PHAG/PHE/TAOEUS` → magnetise
 - `STAEUBL/KWRAOEUFR` → stabiliser
 - `AOUT/HRAOEUFG` → utilising

### ll spellings

The rule discussed in [conflict resolution](#conflict-resolution) is utilized where asterisk is used on the stroke with the double "L".

Examples:
 - `RAOE/TPAO*ULG` → refuelling
 - `RE/SR*EL/*ER` → reveller

> NOTE: because of this rule, single l spellings such as "instal" or "fulfil" are not possible using any method other than `#TPH`

### oe spellings

Words spelled with "oe" are written with `OE`

Examples:
 - `OES/TROE/SKWREPB` → oestrogen
 - `HOEPL/KWROE/PA*T` → homoeopath
 - `AOE/TKOE/PHA` → edoema

### ou spellings

Any spellings with "ou" instead of "o" can be written using `OU`.

Examples:
 - `TPHAEU/PWOUR` → neighbour
 - `KAPB/TKOUR` → candour
 - `KOL/O*UR` → colour

### re spellings

The stroke with `ER` is asterisked. There is no "-re" suffix currently and so any outlines normally written with `*ER` does not fall under this method.

Examples:
 - `KA/HREU/PW*ER` → calibre
 - `PHAOEU/T*ER` → mitre
 - `HREU/T*ER` → litre

### Miscellaneous briefs

~~Asterisk extravaganza!~~

Just asterisk whenever possible.

Examples:
 - `PHAO*ERT` → metre
 - `*ORG` → organise
 - `HRA*EUBLG` → labelling
 - `TPHA*EURB` → neighbour

## movement.modal
This is a modal dictionary that is an extension to the [movement keys in my commands.json dictionary](#Movement-keys).

After the [modal dictionary plugin](https://github.com/Kaoffie/plover_modal_dictionary) has been installed from the plugins manager, ensure Plover has been restarted and the plugin is enabled (configure → plugins). Next add the dictionary above whichever dictionary contains the default movement strokes.

Using this dictionary for movement keys is exactly the same as those in [commands.json](#Movement-keys), however every successive movement stroke after the first does not need to contain the `STPH` cluster.

Examples:
 - `STPH-G/-G/-G/-G` → arrow key to the right 4 times
 - `STPH*R/*R/*R` → select 3 characters to the left
 - `STPH-BG/-BG/-BG` → move to the right by 3 words

## raw.py
This python dictionary (requiring the [plover-python-dictionary plugin](https://github.com/benoit-pierre/plover_python_dictionary)) outputs the raw steno strokes joined by slashes (`/`) with the [plover-stitching plugin](https://github.com/morinted/plover_stitching). You will also need the [plover-dict-commands plugin](https://github.com/KoiOates/plover_dict_commands) for enabling this dictionary with steno strokes. All plugins can be installed from the plugins manager.

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

This dictionary defines number reversals with `U` instead of `EU` which would be impossible using thumber keys on The Uni. This is a supplemental dictionary for the standard number system that comes with `main.json`; it is not compatible with [rh-numpad.json](#rh-numpadjson).

Examples:
 - `#AOU` → 05
 - `#STPU` → 321

## viet.json

My Vietnamese steno theory utilizing the English layout.

![80 WPM Vietnamese steno test](https://cdn.discordapp.com/attachments/1010616084988178502/1011698964338311198/MonkeyType_Viet.gif)

### Basics

It is an orthographic system with chords for the different letter combinations and tones.

In addition to the table below listing all of the chords, there is also a [Quizlet folder](https://quizlet.com/aerickt/folders/vietnamese-steno-theory/sets) for flash card sets containing these chords. I recommend using the "write" option (under "learn") and answering the definition. Disabling your dictionaries can allow you to input the steno chord for each term.

I am unsure of the the usability of this system, however 150 WPM is theoretically possible with a stroke speed of 3 strokes per second. I am currently at one and a half strokes per second after a little under 2 weeks of learning this system (70 WPM or so).

<table>
<tr><td valign="top" align="center">

| Beginning Consonant | Steno Chord |
| - | - |
| b | PW |
| c | K |
| d | TKP |
| đ | TK |
| g | TKPW |
| h | H |
| k | K |
| l | HR |
| m | PH |
| n | TPH |
| p | P |
| q | KW |
| r | R |
| s | S |
| t | T |
| v | SR |
| x | KP |
| ch | KHR |
| đr | TKR |
| gh | TKPWH |
| gi | STKPW |
| kh | KH |
| nh | TPHR |
| ng | STPH |
| ngh | STPHR |
| ph | TP |
| th | TH |
| tr | TR |
| qu | KWR |

| Vowel | Steno Chord |
| - | - |
| a | A |
| o | O |
| u | U |
| ô | OE |
| i | -F |

</td><td valign="top" align="center">

| Vowel | Steno Chord |
| - | - |
| ă | AFR |
| e | E |
| â | EFR |
| ơ | OU |
| ê | AE |
| iê | AEF |
| ư | UR |
| ươ | OUR |
| oa | AOU |
| ai | AF |
| ao | AO |
| uô | OEU |
| eo | EF |
| ây | ER |
| ôi | OEF |
| oi | OF |
| ay | AR |
| âu | EUFR |
| ui | UF |
| ưa | AUR |
| ơi | OUF |
| iêu | EU |
| au | AU |
| ua | OR |
| iu | -FR |
| oe | O*E |
| ia | AUF |
| uy | UFR |
| êu | AEU |
| uyê | EUR |
| oă | AOFR |
| oai | AOF |
| uâ | OEUFR |
| ươi | OUFR |
| uôi | OEUF |

</td><td valign="top" align="center">

| Vowel (Cont.) | Steno Chord |
| - | - |
| uê | AEFR |
| y | -R |
| ưu | AOE |
| yê | AER |
| oo | AOEU |
| oay | AOR |
| ươu | OFR |
| uơ | O*UR |
| uây | *EUFR |
| ưi | EUF |
| oeo | OER |
| yêu | AEUR |
| uyu | AOEUFR |
| uya | AOEUR |
| ya | A*R |
| uă | AUFR |

| Ending Consonant | Steno Chord |
| - | - |
| c | -BG |
| n | -L |
| m | -PL |
| p | -P |
| t | -G |
| h | -B |
| ch | -PBLG |
| nh | -PB |
| mh | -PLG |
| ng | -LG |

| Tone | Steno Chord |
| - | - |
| ngang | |
| huyền | -S |
| hỏi | -D |
| sắc | -T |
| ngã | -TS |
| nặng | -Z |

</td></tr> </table>

### Fingerspelling

When doing typing tests, you may often come across chords that you are unfamiliar with. If this is the case, it's best to fingerspell and watch the suggestions window for what you had missed.

Fingerspelling itself is done by writing a chord with the asterisk. `-P` can be used to capitalize.
