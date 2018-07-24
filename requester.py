from FIOS.font import grey as _grey, end as _end, beige as _beige
from FIOS.sample import choicebox as _box
from FIOS.convert import to_interval as _to_i, to_single_list as _to_s

# TODO: simplify ; rename() ; incorrect words ; match with fm; multiple tags
help_req = {
    "GENERAL":        '',                                # ------
    "undo":           "Cancel last operation",           # X
    "exit":           "Finish program",                  # >
    "":               "Enter",                           # V
    ".TAGS..":        '',                                # ------
    "++":             "Inc",                             # >
    "--":             "Dec",                             # >
    "-r":             "Recursive",                       # V
    "-o":             "Odd",                             # >
    "exc":            "$EXCEPTION",                      # V
    "usd":            "$USED",                           # V
    "-d":             "Dir",                             # >
    "-f":             "File",                            # >
    "-t":             "Type",                            # X
    "EXPLORE":        '',                                # ------
    "mk {item}":      "Make {item} in WD",               # V
    "rn {item}":      "Rename {item}",                   # V
    "rm {item}":      "Remove {item}",                   # V
    "rm -o ":         "Delete empty items in WD",        # V
    "cp {item}":      "Copy {item} to ...",              # V
    "mv {item}":      "Move {item} to ...",              # V
    "sd":             "Single Sort WD",                  # V
    "sd -r":          "Recursive Sort WD",               # V
    "op":             "Open WD",                         # V
    "rf":             "Refresh WD content",              # V
    "tp":             "Get type for every folder",       # V
    "clr":            "Get color for every item",        # V
    "fl":             "Change fluency parameter",        # >
    "{*item} >> exc": "Index {item} into exception",     # V
    "{*item} >> usd": "Index {item} into used",          # V
    "gt -d":          "Get dirs in WD",                  # V
    "gt -f":          "Get files in WD",                 # V
    ".......":        '',                                # ------
    # "-i exception": "Set Extension Directory",
    # "-ch step": "choose step",
}

req = {
    "cmd": {
        "help": "help",
        "undo": "undo",
        "exit": "fin",
        "mk": "make",
        "rn": "rename",
        "rm": "del",
        "cp": "copy",
        "mv": "move",
        "sd": "sort",
        "op": "open",
        "rf": "ref",
        "tp": "type",
        "clr": "color",
        "ind": "ind",
        "fl": "fluency",
        "gt": "get",
    },
    "tag": {
        "++": "inc",
        "--": "dec",
        "-r": "rec",
        "-o": "odd",
        "-d": "dir",
        "-f": "file",
        "-t": "type",
    },
}


def console(ui):
    def init_input():
        fin = ui.split() + ['']*(3 - len(ui.split()))
        if fin[0].isdigit():
            return ("ent", '', int(fin[0])) if not fin[1] else ("ind", fin[-1], (fin[:-2:]))
        else:
            _cmd, _tag = req.get("cmd").get(fin[0], ''), req.get("tag").get(fin[1], '')
            _cmd = "ref" if not _cmd and ui.count(' ') == 0 and ui else _cmd
            return (_cmd, _tag, fin[1]) if not _tag else (_cmd, _tag, fin[2])

    cmd, tag, val = init_input()
    [print(k.ljust(32, ' '), v) if v else print('.' * 29 + k + '.' * 29) for k, v in help_req.items()] if ui == "help" else None
    val = val if cmd not in ["move", "copy", "del", "open", "make"] or tag else ui.split()[1::]
    val = int(val) if str(val).isdigit() else val
    if isinstance(val, list):
        for i in range(len(val)):
            val[i] = (int(val[i]) if val[i].isdigit() else val[i]) if val[i].count('-') == 0 else _to_i(val[i], int)
        val = _to_s(val)
    return cmd, tag, val


def start(*args, requester='', choicebox=True, reverse=False, color=_beige):
    val = args[1:] if len(args) > 1 else []
    if val:
         [print('-', x) for x in _to_s(val)]
    text = args[0].capitalize() if args[0].islower() else args[0]
    print(color + requester + color + text, '?', _box[0] * choicebox + _end)
    user_input = input(color + '>> ' + _end)
    true_return = ['y', "yes"] if reverse else ['', 'y', "yes"]
    if user_input in true_return:
        print(_grey + "<< yes" + _end)
        return True
    else:
        print(_grey + "<< no" + _end)
        return False


if __name__ == "__main__":
    # start("Well. Let's start")
    # start("Well. Let's start", reverse=True)
    console("help")
    print()
    for item in ['', "20", "rf", "13 >> exc", "1 2 3 >> usd", "rm 13", "rm -o", "mk folder", "mk folder_1 folder_2", "mv 1 23 5-7 16", "tp", "clr", "op 7", "rn 3", "sd", "sd -r", "fl ++", "fl --"]:
        print(str({item}).ljust(20), console(item))
    for j in range(3):
        print(console(input(">> ")))
