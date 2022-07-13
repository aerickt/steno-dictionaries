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
This dictionary is intended to replace Plover's `main.json` that comes by default. It has over 100,000 entries and should be sufficient for most everyday writing. It roughly follows Plover theory with a few additions and changes outlined in this page.

> I manually built this dictionary over the course of 6 months on and off. Please let me know if you spot any errors or misleading entries to correct!

I've written a little bit about my motivations for creating a new dictionary over on my [website](https://aerick.ca/steno/dictionary-building) if you'd like a summary of this project.

### Dictionary contents
 - [Who should use this dictionary?](#Who-should-use-this-dictionary?)
 - [Using this dictionary](#Using-this-dictionary)
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
 - [Beyond writing out](#Beyond-writing-out)

#### Who should use this dictionary?

I believe this dictionary will make it easier for beginners to pick up stenography due to the following reasons I outline below. However, this reference page is the only learning resource specific to this dictionary and thus learning the bulk of the theory will be reading this page or [looking up](#Using-this-dictionary) entries.

I would consider using this dictionary only if you are the type that like to figure things out by themselves as opposed to going through a step by step process that guides you along the way. Furthermore, I would definitely recommend skimming through some of the contents on this page and understanding the main differences this dictionary has with stock Plover theory.

It is also necessary to know the main missing sounds and compound clusters of Plover theory before reading this page. You can learn these from reading Art of Chording or Learn Plover!. I recommend reading the latter up to the end of lesson 3.

#### Using this dictionary

You can download this dictionary by right clicking [here](https://github.com/aerickt/steno-dictionaries/raw/main/plover-base.json) and pressing "save link". Make sure you save the file as json especially on Windows. Afterwards, add it to Plover and disable or remove `main.json`.

Since this page is the only place to learn the theory that comes with this dictionary, I recommend keeping it bookmarked and coming back regularly. If you find a quirk in the lookup tool that doesn't sit right with you, consult this page first.

If it is still unclear to you, feel free to reach out to me, either by opening a GitHub issue on this repo, or contacting me on Discord (I am aerick#3063) through the [Plover Discord Server](https://discord.gg/NAzMz7C3wq).

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

One more thing to note is that using the lookup tool you will often find words with folded suffix strokes. For example, take the word "recreating":
```
"RAOE/KRAOE/KWRAEUGT": "recreating",
"RAOE/KRAOEGT": "recreating",
"RE/KRAOE/KWRAEUGT": "recreating",
"RE/KRAOEGT": "recreating",

```

You do **not** have to fold in the G on these strokes! Even though `RAOE/KRAOE/KWRAEUT/-G` is not defined in the dictionary, it will still work. Same goes for `-S`, `-D`, and `-Z`. Folding is more of an [advance technique](#Folding-suffix-keys) that is discussed more later.

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
 - `TK*EU` is always used for the initial `TKEU` sound when starting a word. `TKEU` is reserved for the phrase "did I"
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

When it is ambiguous as to whether `W` or `KWR` is used, there should be options for both. Add alternatives to your dictionary if they make sense to you.

However, beware of attempting to rely on `KWR` solely as this is not the point of this dictionary. You will have to add many entries if you tend to rely on `KWR` excessively.

The following are words that unnecessarily use the `KWR` linker:
 - `TPRAFRPB/KWRAOEUZ` (franchise) ❌
   - `TPRAPB/KHAOEUS` ✔️
 - `EUPB/SAOUL/KWREUPB`(insulin) ❌
   - `EUPB/SAOU/HREUPB` ✔️
 - `HARPS/KWREU/KORD` (harpsichord) ❌
   - `HARP/SEU/KORD` ✔️

#### Exceptions to syllable breaks

##### Starting strokes not to be used

Sometimes a stroke should not begin with a certain chord as it is a common brief and would lead to word boundary issues. The following chords should not be used as strokes to start an outline.
 - `KO`
 - `O`
 - `E`
 - `U`
 - `EU`

Instead carry the first stroke far enough so that there is a consonant on the right hand and use other means (such as `KWR` linker or suffixes) to complete the word.
 - `KOL/KWREBGT` → collect
 - `EBG/KWRO/TPHO/PHEUBG` → economic
 - `KOT/KWROPB` → cotton

##### `KWR` linker with prefix strokes

If the first stroke of an outline is a prefix, there is no need to use the `KWR` linker on the next stroke:
 - `KOE/OR/TKEU/TPHAEUT` → coordinate
 - `PRE/EPLT` → preempt
 - `TK*EU/AOE/HREBG/TREUBG` - dielectric
 - `TKEUS/AEUBL` → disable

##### Consonant doubling with prefixes

Consonants can be doubled if the previous stroke is a prefix and the strokes that follow form a valid word on their own:
 - `TKEUS/SOFLS` → dissolves
 - `TKEUS/SEU/PHEU/HRAR` → dissimilar

##### The problem of the vowel/consonant "R"
When it comes to vowels that are combined with a final `-R`, it may be necessary to use suffix strokes and/or the `KWR` linker in order to preserve the phonetics of the vowel. For example, the word "carry" would have to be written as `KAEUR/KWREU` as the R changes the sound of the vowel and thus should be kept in the first stroke.

If the R was treated as a consonant it was instead split as "ca|rry", the outline could only be `KAEU/REU` or `KA/REU`  which are not completely accurate to the pronunciatoin. Thus, if an R changes the sound of a vowel in a word, it is recommended to keep it with the vowel to preserve its sound and instead use the `KWR` linker to complete the next stroke.

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

This method is, however, used to resolve a few conflicts; see [Conflict resolution](#Conflict-resolution).

##### Situations that benefit from dropping unstressed vowels
As previously mentioned in [phonetics](#Phonetics), `TEU` can be used to represent -ity even if not used as a suffix. This is very much a situation that is actually dropping an unstressed vowel in disguise. Consider the two outlines of writing "felicity":
 - `TPE/HREUS/TEU`
 - `TPE/HREU/SEU/TEU`

You'll notice that in the first outline, the second "i" was dropped as it is unstressed. The second outline is not recommended as it uses an extra stroke, making it slower to write.

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

On the other hand, the following are examples of when using suffixes is unnecessary:
 - `STAOUD/KWREPBT` (student) ❌
   - `STAOU/TKEPBT` ✔️
 - `WAUT/*ER` (water) ❌
   - `WAU/TER` ✔️
 - `SKOL/A*R` (scholar) ❌
   - `SKO/HRAR` ✔️

For ambiguous situations where it is not clear whether to use suffixes or split a word syllabically, both options should be available to use. And of course, don't be afraid to add your own alternatives.

#### Prefixes and suffixes
This is a list of common prefix and suffix strokes. Knowing these should be sufficient for most writing.
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
 - In addition to being suffix strokes, the following can be used to split words syllabically with the `KWR` chord representing a diphthong. Use `KWR*` if the "I" variant of the suffix is needed on a translation that isn't already in the dictionary.
   - `KWROPB` → -on
     - Syllabically as in `OPB/KWROPB` → onion
   - `KWRAPB` → -an
     - Syllabically as in `OB/SEUD/KWRAPB` → obsidian
   - `KWRAPBT` → -ant
     - Syllabically as in `SRAL/KWRAPBT` → valiant
   - `KWREPB` → -en
     - Syllabically as in `AEUL/KWREPB` → alien
   - `KWREPBT` → -ent
     - Syllabically as in `RAOE/SEUP/KWREPBT` → recipient
 - `A*R` → -ar
 - `A*L` → -al
 - `O*R` → -or
 - `*ER` → -er
 - `-PLT` → -ment
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
 - For conflicts with words ending "i" vs "y", use `EU` and `KWREU` respectively
   - `#TE/REU` → Terri
   - `#TER/KWREU` → Terry
   - `#SAPL/KWREU` → Sammy
   - `#SA/PHEU` → Sammi

#### Beyond writing out
It's no secret that writing out syllabically can be quite slow. Here are a few techniques you can find in the dictionary that will help you write a bit shorter.

##### Dropping unstressed vowels
I have kind of already illustrated this technique in [Situations that benefit from dropping unstressed vowels](#Situations-that-benefit-from-dropping unstressed-vowels). Figuring out stress can be a bit of a challenge within a word and I unfortunately do not have any tips at this moment, apart from showing a few examples.
 - `PHEPL/RAOEUZ` → memorize ("o" is dropped)
 - `TPOFRPB/TPHAT` → fortunate ("u" is dropped)
 - `KPHAPBD` → command ("o" is dropped and remaining word is fit into one stroke)
 - `KPHAOUPB/KAEUT` → communicate (both the "o" and the "i" are dropped)
 - `STKAOEUR` → desire ("e" is dropped, and `STK` serves as "ds" using an inversion)
 - `STKPAOER` → disappear ("i" and first "a" are both dropped, `STK` serving as "ds" using an inversion)
 - `RUFR` → rougher ("e" is dropped, `-FR` representing the "fer" sound)
 - `TKEUFRPBT` → different (both "e"'s are dropped, remaining consonants fit into single stroke)

##### Using shorter prefixes and suffixes
Most prefixes and suffixes are simple to determine. For example, `PHE/TKPWA` is the mega- prefix. However, you can save a stroke by using `PH*EG` instead. Use the lookup tool to find shorter prefixes if they exist

A few examples are listed below:
 - `PHEU/HREU` → milli-
   - `PH*EUL` can instead be used
 - `KEU/HROE` → kilo-
   - `K*EUL` can instead be used
 - `RE/TROE` → retro-
   - `RERT` can instead be used

Suffixes can also be shortened similarly like I have shown in [Situations that benefit from dropping unstressed vowels](#Situations-that-benefit-from-dropping unstressed-vowels).

A few other special suffixes are worth mentioning, however.

The canonical way of writing "dictionary" is `TKEUBGS/KWRAEUR/KWREU` with `KWRAEUR/KWREU` representing the -ary suffix. `KWRAER` serves as a shorter alternative as seen in the following examples:
 - `TKO/KAOU/-PLT/KWRAER` → documentary
 - `TKEUS/PEPBS/KWRAER` → dispensary
 - `SREUGS/KWRAER` → visionary

-ory can also be shortened from `O*R/KWREU` to `KWROER`:
 - `TPABGT/O*R/KWREU` → factory
   - Can instead be `TPABGT/KWROER`
 - `PRE/EPLT/O*R/KWREU` → preemptory
   - Can instead be `PRE/EPLT/KWROER`
 - `STA/KHAOUT/O*R/KWREU` → statutory
   - Can instead be `STA/KHAOUT/KWROER`

`AER` and `OER` are also special in that they are not just parts of suffixes, but can represent the sounds of  -ary and -ory when combined with other consonants.

 - `EUPB/SREPB/TOER` → inventory
 - `OB/HREU/TKPWA/TOER` → obligatory
 - `UPB/TPHE/SE/SAER` → unnecessary
 - `ES/KHAOU/WAER` → estuary

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
