## 0x05. Processes and signals

**What you should learn from this project**

       At the end of this project you are expected to be able to explain,
       without the help of Google:

* What is a PID
* What is a process
* How to find a process PID
* How to kill a process
* What is a signal
* What are the 2 signals that cannot be ignored

## Exercises

[0-what-is-my-pid](./0-what-is-my-pid)
```
Write a Bash script that displays its PID.
```

[1-list_your_processes](./1-list_your_processes)
```
Write a Bash script that displays a list of currently running processes.
Requirements:
```
* Must show all processes, for all users, including those which might not have a TTY
* Display a user-oriented format
* Show process hierarchy

[2-show_your_bash_pid](./2-show_your_bash_pid)
```
Using your previous exercise command, write a Bash script that displays line containing the bash word, this allowing you to easily get the PID of your Bash process
Requirements:
```
* You cannot use pgrep
* The third line of your script must be # shellcheck disable=SC2009 (for more info about ignoring shellcheck error here)

[3-show_your_bash_pid_made_easy](./3-show_your_bash_pid_made_easy)
```
Write a Bash script that displays the PID, along with the process name, of processes which name contains the word bash.
Requirements:
```
* You cannot use ps
* For the first iteration: bash PID is 4404 and that the 3-show_your_bash_pid_made_easy script PID is 4555
* For the second iteration: bash PID is 4404 and that the 3-show_your_bash_pid_made_easy script PID is 4557

[4-to_infinity_and_beyond](./4-to_infinity_and_beyond)
```
Write a Bash script that displays To infinity and beyond indefinitely. 
Requirements:
```
* In between each iteration of the loop, add a sleep 2

[5-kill_me_now](./5-kill_me_now)
```
We killed our 4-to_infinity_and_beyond process using ctrl+c in the previous task, there is actually another way to do this.
Write a Bash script that kills 4-to_infinity_and_beyond process.
Requirements:
```
* You must use kill

[6-kill_me_now_made_easy](./6-kill_me_now_made_easy)
```
Write a Bash script that kills 4-to_infinity_and_beyond process.
Requirements:
```
* You cannot use kill or killall

[7-highlander](./7-highlander)
```
Write a Bash script that displays: 
```
* To infinity and beyond indefinitely
* With a sleep 2 in between each iteration
* I am invincible!!! when receiving a SIGTERM signal

[8-beheaded_process](./8-beheaded_process)
```
Write a Bash script that kills the process 7-highlander.
```

[100-process_and_pid_file](./100-process_and_pid_file)
```
Write a Bash script that: 
```
* Creates the file /var/run/holbertonscript.pid containing its PID
* Displays To infinity and beyond indefinitely
* Displays I hate the kill command when receiving a SIGTERM signal
* Displays Y U no love me?! when receiving a SIGINT signal
* Deletes the file /var/run/holbertonscript.pid and terminate itself when receiving a SIGQUIT or SIGTERM signal

[101-manage_my_process](./101-manage_my_process)
```
man: sudo
Programs that are detached from the terminal and running in the background are called daemons or processes, need to be managed. The general minimum set of instructions is: start, restart and stop. The most popular way of doing so on Unix system is to use the init scripts.
Write a manage_my_process Bash script that: 
Write Bash (init) script 101-manage_my_process that manages manage_my_process. (both files need to be pushed to git)
Requirements:
```
* Indefinitely writes I am alive! to the file /tmp/my_process
* In between every I am alive! message, the program should pause for 2 seconds
* When passing the argument start: 
  * Starts manage_my_process
  * Creates a file containing its PID in /var/run/my_process.pid
  * Displays manage_my_process started
* When passing the argument stop: 
  * Stops manage_my_process
  * Deletes the file /var/run/my_process.pid
  * Displays manage_my_process stopped
* When passing the argument restart 
  * Stops manage_my_process
  * Deletes the file /var/run/my_process.pid
  * Starts manage_my_process
  * Creates a file containing its PID in /var/run/my_process.pid
  * Displays manage_my_process restarted
* Displays Usage: manage_my_process {start|stop|restart} if any other argument or no argument is passed

[102-zombie.c](./102-zombie.c)
```
Read what a zombie process is.
Write a C program that creates 5 zombie processes.
Requirements:
```
* For every zombie process created, it displays Zombie process created, PID: ZOMBIE_PID
* Your code should use the Betty style. It will be checked using betty-style.pl and betty-doc.pl
* When you code is done creating the parent process and the zombies, use the function bellow

## Author
### Kevin Yook 
Email: <yook00627@gmail.com> Twitter: [@yook00627](https://twitter.com/yook00627)
