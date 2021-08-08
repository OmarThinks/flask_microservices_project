# flask_microservices_project
Building a Microserviecs using Flask

# References:

1. Github Repo: 
	- https://github.com/udacity/ud615  
2. Udacity Course: 
	- https://www.udacity.com/course/scalable-microservices-with-kubernetes--ud615
	- (This is a free course)

# Services

This consists of 2 sevices:

1. **hello_world_service**
2. **ping_service**



# 1) Hello World Service:

## Port: 
3000  

## Endpoints:

### 1) (GET) /
Returns: Hello, World!  
**http://127.0.0.1:3000/**




## How to run:

<b>

```shell
python services/hello_world_service/app.py
```

</b>







# 2) Ping Service:

## Port: 
3001  

## Endpoints:

### 1) (GET) /ping
Returns: Pong  

**http://127.0.0.1:3001/ping**



## How to run:

<b>

```shell
python services/ping_service/app.py
```

</b>














