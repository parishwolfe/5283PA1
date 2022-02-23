# CS5283 PA1

This repository is a manual implementation of a http web server and web client using sockets

## Server

Usage:  
`python3 web_server.py 8080 ./`

## Client

Usage:  
`python3 .\web_client.py http://127.0.0.1:8080/index.html HEAD`  
`python3 .\web_client.py http://127.0.0.1:8080/index.html GET`  
`python3 .\web_client.py http://127.0.0.1:8080/largeFile.html GET`  
`python3 .\web_client.py http://127.0.0.1:8080/NonExistantFile.html GET`  

## screenshots

Client and server operation:
![ClientAndServerOperation](/img/demo.png?raw=true "Server and Client Operation")  
Large File from chrome:
![LargeFileFromChrome](/img/LargeFileFromChrome.png?raw=True "Large File from chrome")
404 from chrome:
![404](/img/404FromChrome.png?raw=True "404 from Chrome")  
