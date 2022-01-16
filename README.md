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

#### Right hand number pad
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

> Planning on using `-RBGS` for fingerspelling with hyphens (stitching) but this requires the plover-stitching plugin

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

#### Breaking up multisyllable words
main.json relies on a lot of dropping unstressed vowels in order to break up words which is also used in this dictionary. Words such as "memorize" benefit from a rule like this as the middle syllable is essentially dropped, leaving it unambiguous as to where to break it up: `PHEPL/RAOEUZ`. This dictionary also includes some entries where unstressed vowels haven't been dropped, but it is recommended to not use these as they may not be complete.

If it is still ambiguous as to where a syllable break starts, even if unstressed vowels have been dropped, then the rule is to carry each syllable as far as possible so that every stroke can start with a consonant. Consonants are also never doubled (`TKPWHROR/REU` (glory) would not be valid).

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

However, some words will not be able to be broken up like this such as words starting with vowels. These are handled exactly the same, except that it is acceptable for the first stroke to begin with a vowel.

Examples:
 - `EUPL/POR/TAPBT` → important
 - `OE/PWAEU` → obey
 - `ABG/SES` → access

If there are two vowels next to each other that have to be represented in two strokes, `KWR` is used as a linker between the vowels.

Examples:
 - `AOEU/KWROE/HREU` → aioli
 - `PAOE/KWRA/TPHOE` → piano

It is also important to use prefixes and suffixes whenever possible to break up words. Many entries containing prefixes and suffixes exist in the dictionary. However, given the nature of how Plover handles suffixes, writing words using these strokes that aren't defined in the dictionary will not show up when using the lookup tool.

Examples:
 - `HRAOBG/SKWRUP` → lookup
 - `HRERPB/*ER` → learner

Some words will also be able be stroked using suffix strokes, even if whatever was previously stroked is is not a word. This may be because some strokes would be too short and would cause word boundary issues.

Examples:
 - `UT/*ER` → utter (as opposed to `U/TER`)
 - `ED/EUGS` → edition (as opposed to `E/TKEUGS`)

If there is no other way to break up a word so that every non-prefix, non-suffix, and non-starting stroke begins with a vowel, `KWR` is used instead as a linker.

Examples:
 - `ER/KWROR` → error

In general, every word in the dictionary will have at least one of these ways to break up a word. If a unstressed vowels have been dropped and a word cannot be written using the "normal" syllable breaking method (taking each stroke as far as possible so that they begin with a consonant), then it will either be written using prefixes and suffixes, or using `KWR` as a beginning consonant.

The majority of words actually have multiple entries for splitting. You may use whichever method makes the most sense for a given word, but I would recommend preferring to drop unstressed vowels, splitting "normally", and using prefixes and suffixes whenever those fail. I would only use the `KWR` linker if the other methods seemed unnatural, or if it is impossible to use the other methods.

#### Suffixes and prefixes
There have been a lot of changes.
