 # Steno Dictionaries

[![paypal](https://img.shields.io/badge/-Buy%20me%20a%20coffee%20%3AD-informational?logo=paypal)](https://www.paypal.com/donate/?hosted_button_id=VNMUULBPTQGMC)

My personal steno dictionaries.
 - [ip.py](#ippy)
 - [lapwing-base.json](#lapwing-basejson)
 - [lapwing-commands.json](#lapwing-commandsjson)
 - [lapwing-movement.modal](#lapwing-movementmodal)
 - [lapwing-numbers.json](#lapwing-numbersjson)
 - [lapwing-uk-additions.json](#lapwing-uk-additionsjson)
 - [LaTeX.json](#LaTeXjson)
 - [raw.py](#rawpy)
 - [semi-modal-movement.json](#semi-modal-movementjson)
 - [uni-number-reversals.json](#uni-number-reversalsjson)
 - [viet.json](#vietjson)

## ip.py

Write `#AOEUP` to output the local IP address of the machine Plover is running on. Useful on a headless [Stenogotchi](https://github.com/Anodynous/stenogotchi) that doesn't have a screen.

Requires [plover-python-dictionary plugin](https://github.com/benoit-pierre/plover_python_dictionary) as well as the `netiface` python package (must be installed from the command-line).

It uses `netiface` because that was the most reliable way I could get it to work.

## lapwing-base.json

This dictionary is for Lapwing theory, a free alternative to Plover theory and its `main.json`.

Looking to learn Lapwing theory? Check out the [Lapwing for Beginners Wiki](https://lapwing.aerick.ca).

## lapwing-commands.json
This dictionary contains all main movement, keyboard shortcuts, and Plover commands that I use.

### Dictionary contents

 - [Movement keys](#Movement-keys)
 - [Commands and keyboard shortcuts](#Commands-and-keyboard-shortcuts)

#### Movement keys

By pressing down `STPH` on the left hand, the `-RPBG` cluster becomes arrow keys. `-FR` chorded together would be home, and `-LG` would be end. Pageup and pagedown resemble arrows pointing up and down respectively `-RPG` and `-FBL`.

By pressing `STPH*` instead, the shift modifier is used together with the movement keys in order to select text.

To move word by word (equivalent to pressing `Ctrl+Shift` and left/right), `-RB` and `-BG` are used. On macOS, `Alt+Shift` is used instead so that will have to be changed.

For more details see [Lapwing for Beginners](https://lapwing.aerick.ca/Chapter-26.html).

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
 - `#TA*B` → `Shift+Tab`

For more details, see [Lapwing for Beginners](https://lapwing.aerick.ca/Chapter-20.html#commands).

For writing every single keyboard shortcut possible, I recommend [Emily's modifiers dictionary](https://github.com/EPLHREU/emily-modifiers).

## lapwing-movement.modal

See also: [semi-modal-movement.json](#semi-modal-movementjson)

This is a modal dictionary that is an extension to the [movement keys in my commands.json dictionary](#Movement-keys).

After the [modal dictionary plugin](https://github.com/Kaoffie/plover_modal_dictionary) has been installed from the plugins manager, ensure Plover has been restarted and the plugin is enabled (configure → plugins). Next add the dictionary above whichever dictionary contains the default movement strokes.

Using this dictionary for movement keys is exactly the same as those in [commands.json](#Movement-keys), however every successive movement stroke after the first does not need to contain the `STPH` cluster.

Examples:
 - `STPH-G/-G/-G/-G` → arrow key to the right 4 times
 - `STPH*R/*R/*R` → select 3 characters to the left
 - `STPH-BG/-BG/-BG` → move to the right by 3 words

## lapwing-numbers.json

A right hand numberpad system. Lapwing not required; can be used with other theories.

See the [Lapwing for Beginners Wiki](https://github.com/aerickt/lapwing-for-beginners/wiki/Chapter-17:-Fingerspelling-and-Numbers#numbers) for more details.

## lapwing-uk-additions.json

A dictionary for UK spellings for use with Lapwing theory. See [Lapwing for Beginners](https://lapwing.aerick.ca/Chapter-20.html) for details.

## LaTeX.json

My dictionary I use for writing LaTeX with steno. See the [wiki](https://github.com/aerickt/steno-dictionaries/wiki/LaTeX) for details

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

## semi-modal-movement.json

See also: [movement.modal](#movementmodal)

This dictionary contains movement strokes without the starting chord. The idea is to keep this dictionary at the top of your stack, but only enable it when you need to move the text cursor. You can use a dictionary entry like the following to achieve this:

```
"STPH": "{plover:toggle_dict:!semi-modal-movement.json}"
```

Make sure you have the [plover-dict-commands plugin](https://github.com/KoiOates/plover_dict_commands) installed. You can do this by going to the plugins manager, installing it, and restarting Plover.

## uni-number-reversals.json

This dictionary defines number reversals with `U` instead of `EU` which would be impossible using thumber keys on The Uni. This is a supplemental dictionary for the standard number system that comes with `main.json`; it is not compatible with [rh-numpad.json](#rh-numpadjson).

Examples:
 - `#AOU` → 05
 - `#STPU` → 321

## viet.json

My Vietnamese steno theory utilizing the English layout.

![80 WPM Vietnamese steno test](https://cdn.discordapp.com/attachments/1010616084988178502/1011698964338311198/MonkeyType_Viet.gif)

This is my second attempt at a Vietnamese theory which is an improved version of my [old one](https://github.com/aerickt/plover_viet_old) with some inspiration from [user202729's plover_vi](https://github.com/user202729/plover_vi).

This system is easier to learn than my old system due to having fewer awkward chords and using the standard English layout. This removes the need to learn a another layout, saving weeks in the learning process if you are already familiar with English steno.

Although user202729's system has a faster potential speed with 2 word phrasing (which my system lacks) I have not been able to get it working with the latest version of Plover which is why I created this system.

For details see the [wiki](https://github.com/aerickt/steno-dictionaries/wiki/Vietnamese-Steno).

More recent demo on YouTube:

[![Watch the video](https://img.youtube.com/vi/5LLYKb2uwuo/maxresdefault.jpg)](https://youtu.be/5LLYKb2uwuo)
