# Example of a service with docker compose

## How to use

Go at the root of the directory and run : 

```
docker-compose build
docker-compose up
```


## Docker compose structure

3 services must work together : 2 are python processes and a redis server.
A quick justification of the `Dockerfile` structure is done on the following paragraphs

#### Python processes

Work with a basic environement. A simple requirement.txt must be installed.
The python files are organised into a package that can be installed locally, it allows to reuse some code between the processes.
Thus we need both 
```
pip install -r requirements.txt # package dependency
pip install -e . # Local package
```

## Testing the service

Example : 

Once the docker compose up command has started, you can reach an URL like 

[http://localhost:5000/something](http://localhost:5000/something)

It will return 

`something_transformed`

The behaviour of the worker is to add a string to the query string in the request.
Please note that the returned string could the new url of the processed video.

You can also try something like : 

[http://localhost:5000/toto](http://localhost:5000/toto)
