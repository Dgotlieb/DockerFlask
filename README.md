# DockerFlask
Simple Flask on Docker

### Instructions:  
#### 1. Build the image:  
```$ docker build -t myflask . ```  
#### 2. Run a container without volumes:  
```$ docker run -p 5000:5000 myflask ```  

#### 3. Run a container using volumes:  
##### Windows users only:  
```$ docker run -v %cd%/logs:/app/logs -p 5000:5000 myflask ```   
##### Mac / Linux / Powershell(Windows) users only:  
```$ docker run -v $(pwd)/logs:/app/logs -p 5000:5000 myflask ```  
  
Visit http://localhost:5000/hello/name  
  
#### Docker toolbox users will need to mount the files of the VM (deafult)
