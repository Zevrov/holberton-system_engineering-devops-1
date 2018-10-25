# 0x0C. Web stack debugging #0

## Exercises

[0-give_me_a_page](./0-give_me_a_page)
```
In this first debugging project, you will need to get Apache to run on the container and to return a page containing Hello Holberton when querying the root of it.
Example:
```
```
root@vagrant-ubuntu-trusty-64:/home/vagrant# docker run -p 8080:80 -d -it holbertonschool/265-0
d275ce8cffc10fa1fab33f6d61d40b6530e3693c7bf097128be6d51ac63c0fda
root@vagrant-ubuntu-trusty-64:/home/vagrant# docker ps
CONTAINER ID        IMAGE                          COMMAND             CREATED             STATUS              PORTS                  NAMES
d275ce8cffc1        holbertonschool/265-0:latest   "/bin/bash"         2 seconds ago       Up 1 seconds        0.0.0.0:8080->80/tcp   high_euclid
root@vagrant-ubuntu-trusty-64:/home/vagrant# curl 0:8080
curl: (56) Recv failure: Connection reset by peer
root@vagrant-ubuntu-trusty-64:/home/vagrant
```
```
Here we can see that after starting my Docker container, I curl the port 8080 mapped to the Docker container port 80, it does not return a page but an error message. Note that you might also get the error message curl: (52) Empty reply from server.
```
```
root@vagrant-ubuntu-trusty-64:/home/vagrant# curl 0:8080
Hello Holberton
root@vagrant-ubuntu-trusty-64:/home/vagrant#
```
```
After connecting to the container and fixing whatever needed to be fixed (here is your mission), you can see that curling port 80 return a page that contains Hello Holberton. Paste the command(s) you used to fix the issue in your answer file
```
