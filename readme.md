## Simple Fast API example


A simple fast api example with a healthcheck endpoint that always return 200.



### How to run

#### Local

We recommend that you use a virtual environment.

if you dont have venv module please run

```sh
pip3 install venv
```

create the virtual environment and install dependencies

```sh
source .venv
pip3 install -r requirements.txt
```

next, run the server

```sh
uvicorn main:app --reload
```


#### Build your own docker image

If you need to build your own image, we delivery a sample Dockerfile, to build it:

```sh
docker build . -t fastapi-example
```

and run mapping the port (inside the dockerfile the server runs on port 80 )

```sh 
docker run -p 8080:80 fastapi-example
```

in your computer check the 8080 port

```sh
curl http://localhost:8080/health
```

#### Using the public docker image

This repository contains an github action to publish images in docker hub. 

To get the latest version you can simply run

```sh
docker run -p 8080:80 hebertrfreitas/fastapi-example:latest
```

