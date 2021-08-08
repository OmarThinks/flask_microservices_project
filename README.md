# Flask Microservices Project:
Building a Microserviecs using Flask

# A) Credits:

- Udacity Course: 
	- https://www.udacity.com/course/scalable-microservices-with-kubernetes--ud615
	- (This is a free course)

# B) Technologies Used:
1. Python
2. Flask
3. Docker



# C) Services:

This consists of 2 sevices:

1. **hello_world_service**
2. **ping_service**



## C-1) Hello World Service:

### Port: 
3000  

### Endpoints:

### 1) (GET) /
Returns: Hello, World!  
**http://127.0.0.1:3000/**


### How to run:

<b>

```shell
python services/hello_world_service/app.py
```

</b>



## 2) Ping Service:

### Port: 
3001  

### Endpoints:

### 1) (GET) /ping
Returns: Pong  

**http://127.0.0.1:3001/ping**



### How to run:

<b>

```shell
python services/ping_service/app.py
```

</b>










# D) Using Docker

There is a special folder called **Docker**.  
This folder contains all the docker files.  
To run this folder, CD to this folder, and run this command:


<b>

```bash
docker-compose up --force-recreate --build -d
```

</b>
