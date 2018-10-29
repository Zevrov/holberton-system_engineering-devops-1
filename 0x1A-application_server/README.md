# 0x1A. Application server


<img alt="DevOps" src=https://github.com/yook00627/holberton-system_engineering-devops/blob/master/0x1A-application_server/c7d1ed0a2e10d1b4e9b3.jpg>

## Exercises

[0-welcome_gunicorn-upstart_config](./0-welcome_gunicorn-upstart_config)
[0-welcome_gunicorn-nginx_config](./0-welcome_gunicorn-nginx_config)
```
Let’s serve what you built for AirBnB clone v2 - Web framework on web01.
Requirements:
```
* Git clone your AirBnB_clone_v2
* Install Gunicorn and other libraries required by your application
* Create an Upstart script that starts a Gunicorn instance to serve web_flask/0-hello_route.py from your AirBnB_clone_v2
* Setup Nginx so that the route /airbnb-onepage/ points to your Gunicorn instance
* Nginx must serve this page both locally and on its public IP on port 80
* Upload your Upstart config file as 0-welcome_gunicorn-upstart_config
* Upload your Nginx config file as 0-welcome_gunicorn-nginx_config

[1-pass_parameter-upstart_config](./1-pass_parameter-upstart_config)
[1-pass_parameter-nginx_config](./1-pass_parameter-nginx_config)
```
Let’s serve what you built for AirBnB clone v2 - Web framework on web01.
Requirements:
```
* Create an Upstart script that starts a Gunicorn instance to serve web_flask/6-number_odd_or_even.py from your AirBnB_clone_v2
* Setup Nginx so that the route/airbnb-dynamic/ points to your Gunicorn instance
* Nginx must serve this page both locally and on its public IP on port 80
* Upload your Upstart config file as 1-pass_parameter-upstart_config
* Upload your Nginx config file as 1-pass_parameter-nginx_config

[2-api-upstart_config](./2-api-upstart_config)
[2-api-nginx_config](./2-api-nginx_config)
```
Let’s serve what you built for AirBnB clone v3 - RESTful API on web01.
Requirements:
```
* Git clone your AirBnB_clone_v3
* data dump
* Create an Upstart script that starts a Gunicorn instance to serve api/v1/app.py from your AirBnB_clone_v3
* Make sure to use the necessary environment variables for your AirBnB_clone_v3 app
* Setup Nginx so that the route /api/ points to your Gunicorn instance
* Nginx must serve this page both locally and on its public IP on port 80
* Upload your Upstart config as 2-api-upstart_config
* Upload your Nginx config as 2-api-nginx_config

[3-complete_webapp-upstart_config](./3-complete_webapp-upstart_config)
[3-complete_webapp-nginx_config](./3-complete_webapp-nginx_config)
```
Let’s serve what you built for AirBnB clone - Web dynamic on web01.
Requirements:
```
* Git clone your AirBnB_clone_v4
* Create an Upstart script that starts a Gunicorn instance to serve web_dynamic/2-hbnb.py from your AirBnB_clone_v4
* Setup Nginx so that the route / points to your Gunicorn instance
* Setup Nginx so that it properly serves the static assets found in web_dynamic/static/
* For your website to be fully functional, you will need to reconfigure web_dynamic/static/scripts/2-hbnb.js to the correct IP and port
* Nginx must serve this page both locally and on its public IP on port 80
* Make sure to pull up your Developer Tools on your favorite browser to verify that you have no errors
* Upload your Upstart config as 3-complete_webapp-upstart_config
* Upload your Nginx config as 3-complete_webapp-nginx_config

[4-print_most_numbers.c](./4-print_most_numbers.c)
```
I believe in numbers and signs
Write a function that prints the numbers, from 0 to 9, followed by a new line.
```
* Prototype: void print_most_numbers(void);
* Do not print 2 and 4
* You can only use _putchar twice in your code

[5-more_numbers.c](./5-more_numbers.c)
```
Numbers constitute the only universal language
Write a function that prints 10 times the numbers, from 0 to 14,
followed by a new line.
```
*  Prototype: void more_numbers(void);
* You can only use _putchar three times in your code

## Author
### Kevin Yook 
Email: <yook00627@gmail.com> Twitter: [@yook00627](https://twitter.com/yook00627)
