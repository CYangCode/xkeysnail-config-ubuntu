from xkeysnail.transform import *

define_timeout(1)

define_modmap({
    Key.LEFT_ALT: Key.LEFT_CTRL,
    Key.LEFT_CTRL: Key.RIGHT_CTRL
})

# Carabiner and caps2esc for ideas and concept.
define_multipurpose_modmap({
    Key.CAPSLOCK: [Key.CAPSLOCK, Key.RIGHT_CTRL],
    Key.LEFT_META: [Key.LEFT_META, Key.LEFT_ALT]
})

define_keymap(None, {
    # Cursor
    K("RC-h"): with_mark(K("left")),    
    K("RC-l"): with_mark(K("right")),
    K("RC-k"): with_mark(K("up")),
    K("RC-j"): with_mark(K("down")),
    # Beginning/End of line
    K("RC-a"): with_mark(K("home")),
    K("RC-e"): with_mark(K("end")),
    # Exit
    K("LC-q"): with_mark(K('LAlt-f4')),
    # Switch
    K('LC-TAB'): with_mark(K('LAlt-TAB')),
    K('LWin-TAB'): with_mark(K('LC-TAB')),
    K('LAlt-d'): with_mark(K('LWin-d')),
    K('LC-GRAVE'): with_mark(K('LWin-GRAVE')),
    # Backspace
    K('LAlt-BACKSPACE'): with_mark(K('LC-BACKSPACE')),
    K('LC-BACKSPACE'): [K('Shift-home'), K('Shift-home'), K('BACKSPACE'), set_mark(False)],
    K('LC-RC-t'): K('LC-LAlt-t'),
    # windows
    K('LC-RC-f'): K('LC-LAlt-f'),
})