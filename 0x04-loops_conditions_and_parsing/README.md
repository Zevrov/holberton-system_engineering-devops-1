# 0x04. Loops, conditions and parsing

**What you should learn from this project**

    At the end of this project you are expected to be able to explain to anyone, without the help of Google:

* How to create SSH keys
* What is the advantage of using #!/usr/bin/env bash over #!/bin/bash
* How to use while, until and for loops
* How to use if, else, elif and case condition statements
* How to use the cut command
* What are files and other comparison operators, and how to use them

## Exercises

[0-RSA_public_key.pub](./0-RSA_public_key.pub)
```
man: ssh-keygen
You will soon have to manage your own servers hosted on remote data centers. We need to set them up with your RSA public key so that you can access them via SSH.
Create a RSA key pair.
Requirements:
```
* Share your public key in your answer file 0-RSA_public_key.pub
* Fill the SSH public key field of your intranet profile with the public key you just generated
* Keep the private key to yourself in a secure location, you will use it later to connect to your servers using SSH. Some storing ideas are Dropbox, Google Drive, password manager, USB key. Failing to do so will prevent you to access your servers, which will prevent you from doing your projects
* If you decide to add a passphrase to your key, make sure to save this passphrase in a secure location, you will not be able to use your keys without the passphrase

[1-for_holberton_school](./1-for_holberton_school)
```
Write a Bash script that displays Holberton School 10 times.
Requirement:
```
* You must use the for loop (while and until are forbidden)

[2-while_holberton_school](./2-while_holberton_school)
```
Write a Bash script that displays Holberton School 10 times.
Requirements:
```
* You must use the while loop (for and until are forbidden)

[3-until_holberton_school](./3-until_holberton_school)
```
Write a Bash script that displays Holberton School 10 times.
Requirements:
```
* You must use the until loop (for and while are forbidden)

[4-if_9_say_hi](./4-if_9_say_hi)
```
Write a Bash script that displays Holberton School 10 times, but for the 9th iteration, displays Holberton School and then Hi on a new line.
Requirements:
```
* You must use the while loop (for and until are forbidden)
* You must use the if statement

[5-4_bad_luck_8_is_your_chance](./5-4_bad_luck_8_is_your_chance)
```
Write a Bash script that loops from 1 to 10 and:
```
* displays bad luck for the 4th loop iteration
* displays good luck for the 8th loop iteration
* displays Holberton School for the other iterations
* You must use the while loop (for and until are forbidden)
* You must use the if, elif and else statements

[6-superstitious_numbers](./6-superstitious_numbers)
```
Write a Bash script that displays numbers from 1 to 20 and:
```
* displays bad luck from China for the 4th loop iteration
* displays bad luck from Japan for the 9th loop iteration
* displays bad luck from Italy for the 17th loop iteration
* You must use the while loop (for and until are forbidden)
* You must use the case statement

[7-clock](./7-clock)
```
Write a Bash script that displays the time for 12 hours and 59 minutes:
```
* display hours from 0 to 12
* display minutes from 1 to 59
* You must use the while loop (for and until are forbidden)

[8-for_ls](./8-for_ls)
```
Write a Bash script that displays:
```
* The content of the current directory
* In a list format
* Where only the part of the name after the first dash is displayed (refer to the example)
* You must use the for loop (while and until are forbidden)
* Do not display hidden files

[9-to_file_or_not_to_file](./9-to_file_or_not_to_file)
```
Write a Bash script that gives you information about the holbertonschool file.
Requirements:
```
* You must use if and, else (case is forbidden)
* Your Bash script should check if the file exists and print:
  * if the file exists: holbertonschool file exists
  * if the file does not exist: holbertonschool file does not exist
* If the file exists, print:
  * if the file is empty: holbertonschool file is empty
  * if the file is no empty: holbertonschool file is not empty
  * if the file is a regular file: holbertonschool is a regular file
  * if the file is not a regular file: (nothing)

[10-fizzbuzz](./10-fizzbuzz)
```
Write a Bash script that displays numbers from 1 to 100.
Requirements:
```
* Displays FizzBuzz when the number is a multiple of 3 and 5
* Displays Fizz when the number is multiple of 3
* Displays Buzz when the number is a multiple of 5
* Otherwise, displays the number
* In a list format

[100-read_and_cut](./100-read_and_cut)
```
help: read
Write a Bash script that displays the content of the file /etc/passwd.
Your script should only display:
```
* username
* user id
* Home directory path for the user
* You must use the while loop (for and until are forbidden)

[101-tell_the_story_of_passwd](./101-tell_the_story_of_passwd)
```
The file /etc/passwd has already been covered in a previous project and you should be familiar with it. Today we will make up a story based on it.
Write a Bash script that displays the content of the file /etc/passwd, using the while loop + IFS.
Format: The user USERNAME is part of the GROUP_ID gang, lives in HOME_DIRECTORY and rides COMMAND/SHELL. USER ID's place is protected by the passcode PASSWORD, more info about the user here: USER ID INFO
Requirements:
```
* You must use the while loop (for and until are forbidden)

[102-lets_parse_apache_logs](./102-lets_parse_apache_logs)
```
Apache is among the most popular web servers in the world, serving 50% of all active websites, no doubt that you will have to interact with it within your career.
As a Full-Stack Software Engineer, you have to master the art of parsing log files. Today we will do a simple parsing of Apache log access files.
Today the Customer Support department reported that a user reported that the site being “buggy”. Not being an accurate description, you want to have a look at the Apache logs and gather data about the traffic.
Write a Bash script that displays the visitor IP along with the HTTP status code from the Apache log file.
Requirement:
```
* Format: IP HTTP_CODE
  * in a list format
  * See example
* You must use awk
* You are not allowed to use while, for, until and cut
* Download and commit the apache-access.log file along with your answers files

[103-dig_the-data](./103-dig_the-data)
```
Now that you’ve parsed the Apache log file, let’s sort the data so you can get a better idea of what is going on.
Using what you did in the previous exercise, write a Bash script that groups visitors by IP and HTTP status code, and display this data.
Requirements:
```
* The exact format must be: 
  * OCCURENCE_NUMBER IP HTTP_CODE 
  * in a list format
* Ordered from the greatest to the lowest number of occurrence 
  * See example
* You must use awk
* You are not allowed to use while, for, until and cut

## Author
### Kevin Yook 
Email: <yook00627@gmail.com> Twitter: [@yook00627](https://twitter.com/yook00627)
