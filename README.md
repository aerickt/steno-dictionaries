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

This dictionary is for Lapwing theory, a free alternative to Plover theory and its `main.json`. For details, see the [wiki](https://github.com/aerickt/steno-dictionaries/wiki/Lapwing-Theory-Reference-Page).

## lapwing-uk-additions.json

A dictionary for UK spellings for use with Lapwing theory. See the [wiki](https://github.com/aerickt/steno-dictionaries/wiki/Lapwing-Theory-Reference-Page#uk-spellings) for details.

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

This is my second attempt at a Vietnamese theory which is an improved version of my [old one](https://github.com/aerickt/plover_viet_old) with some inspiration from [user202729's plover_vi](https://github.com/user202729/plover_vi).

This system is easier to learn than my old system due to having fewer awkward chords and using the standard English layout. This removes the need to learn a another layout, saving weeks in the learning process if you are already familiar with English steno.

Although user202729's system has a faster potential speed with 2 word phrasing (which my system lacks) I have not been able to get it working with the latest version of Plover which is why I created this system.

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
