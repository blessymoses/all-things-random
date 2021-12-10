# Docker for Python Development

## A Simple Python Flask App
Create a simple flask app to containerize it using Docker
### Install flask
```sh
$ pip3 install flask

$ pip3 freeze
click==8.0.1
Flask==2.0.1
itsdangerous==2.0.1
Jinja2==3.0.1
MarkupSafe==2.0.1
Werkzeug==2.0.1
```
Write the dependencies to a requirements file.
```sh
$ pip3 freeze > requirements.txt
```
### Create the app
`app.py` contains the application’s code, where you create the app and its views.
### Run the app locally
By default, Flask will run the application on port 5000.
```sh
$ flask run
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
To reload your application automatically whenever you make a change, pass an environment variable `FLASK_ENV=development`, to flask run:
```sh
$ FLASK_ENV=development flask run
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
```
### Verify the app
```sh
$ curl http://127.0.0.1:5000/
$ curl http://127.0.0.1:5000/box
```
## commands
- To execute docker commands, without becoming root:

```sh
sudo usermod -aG docker blessy
```
- docker version
- docker-compose version
- docker image ls
- docker container ls
- docker ps : list all running containers
- docker ps -a : list all running and stopped containers
- docker start container_id : To launch a stopped container
- docker build --no-cache -t [image-name]:latest . : build the image
- docker run -it [image-name]
- docker run -it -p 5000:8888 todo-flask

```sh
$ docker version
Client: Docker Engine - Community
 Version:           20.10.3
 API version:       1.41
 Go version:        go1.13.15
 Git commit:        48d30b5
 Built:             Fri Jan 29 14:34:33 2021
 OS/Arch:           linux/amd64
 Context:           default
 Experimental:      true

Server: Docker Engine - Community
 Engine:
  Version:          20.10.3
  API version:      1.41 (minimum version 1.12)
  Go version:       go1.13.15
  Git commit:       46229ca
  Built:            Fri Jan 29 14:32:09 2021
  OS/Arch:          linux/amd64
  Experimental:     false
 containerd:
  Version:          1.4.3
  GitCommit:        269548fa27e0089a8b8278fc4fc781d7f65a939b
 runc:
  Version:          1.0.0-rc92
  GitCommit:        ff819c7e9184c13b7c2607fe6c30ae19403a7aff
 docker-init:
  Version:          0.19.0
  GitCommit:        de40ad0
```

