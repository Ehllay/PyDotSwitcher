<p align="center">
Switch your dotfiles on demand!
<br><br>
<a href="./LICENSE.md"><img src="https://img.shields.io/badge/license-MIT-cba6f7.svg"></a>
</p>
PConfSwitcher is a Python utility that allows you to easily switch between your dotfiles.

## Features


- 📋 **Declarable**: PCS will only change between dotfiles YOU declare.
- 📁 **Grouped**: Make a group to change multiple configurations at the same time. Especially useful for changing colorschemes!
- 🛟  **Safe**: PCS Backs up files before it switches them, and changes to the dotfiles are linked with your current configuration group.
- 📜 **Scriptable**: You can also embed shell scripts for doing stuff when changing themes.
## Usage
Out of the box, PCS won't do anything. That is because you have to declare what files you want. 

But first, a configuration group is needed:

```$ pcswitcher -g MyConfig # Creates the MyConfig Group if it doesn't exist```

Now, let's add a file to our new group with the -a (Append) flag. For example, let's add our GTK settings:

```$ pcswitcher -a ~/.config/gtk-3.0/settings.ini MyConfig``` 

Groups act as separate Home directories, so, running this command will create a ```./.config/gtk-3.0``` directory to store the ```settings.ini``` file inside the __MyConfig__ group (Which, by default resides in ~/.config/pcswitcher/groups/).

Now, to switch up our files, run:
```$ pcswitcher [group]```

This will apply all the configurations inside the group and will backup the existing configuration inside ```~/.cache/pcswitcher/```, however, if you want to disable this, add the ```--no-backup``` flag.

For scripting, run ```$ pcswitcher -s [group]```. This will auto generate a _.sh_ file for you to do scripting, and it will be executed when you switch up the files. If you have added a script to a group but don't want to execute it, append ```--no-script```.

## Tips & Tricks
Some applications require a restart after having an updated. To fix this, create a script in your group and add ```killall program-name && program-name &``` to your script.

