# 0x01. Shell, permissions

**What you should learn from this project**

    At the end of this project you are expected to be able to explain to anyone, without the help of Google:

* What do the commands chmod, sudo, su, chown, chgrp do
* Linux file permissions
* How to represent each of the three sets of permissions (owner, group, and other) as a single digit
* How to change permissions, owner and group of a file
* Why can’t a normal user chown a file
* How to run a command with root privileges
* How to change user ID or become superuser
* How to create a user
* How to create a group
* How to print real and effective user and group IDs
* How to print the groups a user is in
* How to print the effective userid

## Exercises

[0-select_states.py](./0-iam_betty)
```
Create a script that changes your user ID to betty.
```
* You should use exactly 8 characters for your command (+1 character for the new line)
* You can assume that the user betty will exist when we will run your script

[1-who_am_i](./1-who_am_i)
```
Write a script that prints the effective userid of the current user.
```

[2-groups](./2-groups)
```
Write a script that prints all the groups the current user is part of.
```

[3-new_owner ](./3-new_owner )
```
Write a script that changes the owner of the file hello to the user betty.
```

[4-empty](./4-empty)
```
Write a script that creates an empty file called hello.
```

[5-execute](./5-execute)
```
Write a script that adds execute permission to the owner of the file hello.
```
* The file hello will be in the working directory

[6-multiple_permissions](./6-multiple_permissions)
```
Write a script that adds execute permission to the owner and the group owner, and read permission to other users, to the file hello.
```
* The file hello will be in the working directory

[7-everybody](./7-everybody)
```
Write a script that adds execution permission to the owner, the group owner and the other users, to the file hello
```
* The file hello will be in the working directory
* You are not allowed to use commas for this script

[8-James_Bond](./8-James_Bond)
```
Write a script that sets the permission to the file hello as follows:
The file hello will be in the working directory You are not allowed to use commas for this script
```
* Owner: no permission at all
* Group: no permission at all
* Other users: all the permissions

[9-John_Doe](./9-John_Doe)
```
Write a script that sets the mode of the file hello to this:
```
* The file hello will be in the working directory
* You are not allowed to use commas for this script

[10-mirror_permissions](./10-mirror_permissions)
```
Write a script that sets the mode of the file hello the same as olleh’s mode.
```
* The file hello will be in the working directory
* The file olleh will be in the working directory

[11-directories_permissions](./11-directories_permissions)
```
Create a script that adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users. Regular files should not be changed.
```

[12-directory_permissions](./12-directory_permissions)
```
Create a script that creates a directory called dir_holberton with permissions 751 in the working directory.
```

[13-change_group](./13-change_group)
```
Write a script that changes the group owner to holberton for the file hello
```
* The file hello will be in the working directory

[14-change_owner_and_group](./14-change_owner_and_group)
```
Write a script that changes the owner to betty and the group owner to holberton for all the files and directories in the working directory.
```

[15-symbolic_link_permissions](./15-symbolic_link_permissions)
```
Write a script that changes the owner and the group owner of the file _hello to betty and holberton respectively.
```
* The file _hello is in the working directory
* The file _hello is a symbolic link

[16-if_only ](./16-if_only )
```
Write a script that changes the owner of the file hello to betty only if it is owned by the user guillaume.
```
* Write a script that changes the owner of the file hello to betty only if it is owned by the user guillaume.

[100-Star_Wars](./100-Star_Wars)
```
Write a script that will play the StarWars IV episode in the terminal.
```

[101-man_holberton](./101-man_holberton)
```
Create a man that looks exactly like this one and passes all checks.
```

## Author
### Kevin Yook 
Email: <yook00627@gmail.com> Twitter: [@yook00627](https://twitter.com/yook00627)
