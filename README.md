 # Steno Dictionaries

[![paypal](https://img.shields.io/badge/-Buy%20me%20a%20coffee%20%3AD-informational?logo=paypal)](https://www.paypal.com/donate/?hosted_button_id=VNMUULBPTQGMC)

My personal steno dictionaries.
 - [ip.py](#ippy)
 - [LaTeX.json](#LaTeXjson)
 - [raw.py](#rawpy)
 - [semi-modal-movement.json](#semi-modal-movementjson)
 - [uni-number-reversals.json](#uni-number-reversalsjson)
 - [viet.json](#vietjson)

**Lapwing dictionaries have been moved permanently to the [plover-lapwing-aio reposetory](https://github.com/aerickt/plover-lapwing-aio/tree/main/plover_lapwing/dictionaries).**

## ip.py

Write `#AOEUP` to output the local IP address of the machine Plover is running on. Useful on a headless [Stenogotchi](https://github.com/Anodynous/stenogotchi) that doesn't have a screen.

Requires [plover-python-dictionary plugin](https://github.com/benoit-pierre/plover_python_dictionary) as well as the `netiface` python package (must be installed from the command-line).

It uses `netiface` because that was the most reliable way I could get it to work.

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
