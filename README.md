## Easyxmotion
A Easy motion style window switcher.

### How it works
To focus any visible window just launch easyxmotion (preferably from a key binding) then it displays letters on each window, type that letter to jump to the window. 

Should work with any window manager that supports [EWMH](http://en.wikipedia.org/wiki/Extended_Window_Manager_Hints). It probably only makes sense with tiling window managers. This fork is focused on compatibility with QTile.

inspired by the [easymotion vim plugin](https://github.com/Lokaltog/vim-easymotion).

This is the first open source project by [Gravity Four](http://www.gravityfour.com).

## Dependencies

### Arch
```sudo pacman -S libwnck3 xosd python-gobject python-xlib xorg-xlsfonts```

The `xorg-xlsfonts` package isn't required, but comes in handy when configuring the desired font.

## Installing
just put it somewhere in your path.

