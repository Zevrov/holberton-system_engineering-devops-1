# 0x08. Networking basics #1

**What you should learn from this project**

    At the end of this project you are expected to be able to explain to anyone, without the help of Google:

* What is localhost/127.0.0.1
* What is 0.0.0.0
* What is /etc/hosts
* How to display your machine’s active network interfaces

## Exercises

[0-localhost](./0-localhost)
```
What is localhost?
```
1. A hostname that means this IP
2. A hostname that means this computer
3. An IP attached to a computer

[1-wildcard](./1-wildcard)
```
What is 0.0.0.0?
```
1. All IPv4 addresses on the local machine
2. All the IPs
3. It means null in networking

[2-change_your_home_IP](./2-change_your_home_IP)
```
Write a Bash script that configures an Ubuntu server with the below requirements.
Requirements:
```
* localhost resolves to 127.0.0.2
* facebook.com resolves to 8.8.8.8.
* The checker is running on Docker, so make sure to read this
```
In this example we can see that:
```
* before running the script, localhost resolves to 127.0.0.1 and facebook.com resolves to 157.240.11.35
* after running the script, localhost resolves to 127.0.0.2 and facebook.com resolves to 8.8.8.8

[3-show_attached_IPs](./3-show_attached_IPs)
```
Write a Bash script that displays all active IPv4 IPs on the machine it’s executed on.
Example:
Obviously, the IPs displayed may be different depending on which machine you are running the script on.
Note that we can see our localhost IP :)
```
* Prototype: void print_numbers(void);
* You can only use _putchar twice in your code

[4-port_listening_on_localhost](./4-port_listening_on_localhost)
```
Write a Bash script that listens on port 98 on localhost.
```

## Author
### Kevin Yook 
Email: <yook00627@gmail.com> Twitter: [@yook00627](https://twitter.com/yook00627)
