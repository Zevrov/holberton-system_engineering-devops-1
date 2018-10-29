# 0x17. Web stack debugging #3

## Exercises

[0-strace_is_your_friend.pp](./0-strace_is_your_friend.pp)
```
Using strace, find out why Apache is returning a 500 error. Once you find the issue, fix it and then automate it using Puppet (instead of using Bash as you were previously doing).
```
* strace can attach to a current running process
* You can use tmux to run strace in one windows and curl in another one
* Your 0-strace_is_your_friend.pp file must contain Puppet code
* You can use whatever Puppet resource type you want for you fix

## Author
### Kevin Yook 
Email: <yook00627@gmail.com> Twitter: [@yook00627](https://twitter.com/yook00627)
