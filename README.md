# Just ordinary Redis Docker Tutorial
> Just Quick Tutorial how to use docker container, redis and Python
> I will try my best to explain as simple as popssible

## Requirements
- Docker
- Python3.7


## Setting up the environment
> Follow command line to get redis docker container

```
$docker run -d -p 6379:6379 --name redis-dev redis
```

> Follow command line to install python redis package/library

```
$pip install rq
```