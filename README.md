## Easyxmotion
A Easy motion style window switcher.

### How it works
To focus any visible window just launch easyxmotion (preferably from a key binding) then it displays letters on each window, type that letter to jump to the window. 

Should work with any window manager that supports [EWMH](http://en.wikipedia.org/wiki/Extended_Window_Manager_Hints). It probably only makes sense with tiling window managers. This fork is focused on compatibility with QTile.

inspired by the [easymotion vim plugin](https://github.com/Lokaltog/vim-easymotion).

## Dependencies

### Arch
```sudo pacman -S libwnck3 xosd python-gobject python-xlib xorg-xlsfonts```

The `xorg-xlsfonts` package isn't required, but comes in handy when configuring the desired font.

## Installing
Install with the `pipx` (recommended) or `pip` commands:
```sh
pipx install "https://github.com/stiftcast/easyxmotion/releases/download/v1.0/easyxmotion-1.0-py3-none-any.whl"
```
or
```sh
pip3 install --user "https://github.com/stiftcast/easyxmotion/releases/download/v1.0/easyxmotion-1.0-py3-none-any.whl"
```

Alternatively, you can download the wheel [here](https://github.com/stiftcast/easyxmotion/releases/latest) and install it locally:
```
cd ~/Downloads  # Or wherever you saved it
pip3 install --user easyxmotion-1.0-py3-none-any.whl
```
Afterwards, you can use the program by issuing the command `easyxmotion`.


## Example
The best way to use this program is by wrapping it in a shell script, and calling it using a keybinding in your window manager.

In addition, using the `xte` (provided by the `xautomation` package) command to trigger a keyup action on the keys that correspond to the keybinding used to launch the script can help prevent the program from prematurely exiting, in case you don't take your hand off the keys right away.
```sh
xte "keyup Super_L"
xte "keyup w"
easyxmotion  # Append your options here, if desired.
```
Note that the above will likely be need to be called using sudo. This is due to easyxmotion needing access to the `/run` directory.
