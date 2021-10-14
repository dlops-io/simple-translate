# Simple Translate App


## Installing App using Containers

### Prerequisites for Development using Containers
* Have Docker installed
* Cloned this repository to your local machine with a terminal up and running
* Check that your Docker is running with the following command

`docker run hello-world`

### Install Docker 
Install `Docker Desktop`

### Ensure Docker Memory
- To make sure we can run multiple container go to Docker>Preferences>Resources and in "Memory" make sure you have selected > 4GB

### Install VSCode  
Follow the [instructions](https://code.visualstudio.com/download) for your operating system.  
If you already have a preferred text editor, skip this step.  

## Make sure we do not have any running containers and clear up an unused images
* Run `docker container ls`
* Stop any container that is running
* Run `docker system prune`
* Run `docker image ls`

### Clone the github repository
- Clone or download from [here](https://github.com/dlops-io/simple-translate)

### Building Docker Image
Go into the app folder by running
* `cd simple-translate`
Build the docker container by running
* `docker build -t simple-translate -f Dockerfile .`

### Running Docker Container
Run the container using:
* `docker run --rm -ti simple-translate`
Running the translate code
* `python cli.py -t "Good morning" -s "en" -d "es"`
To exit from container
* Type `exit` from the Docker shell

### Pushing Docker Image to Docker Hub
* Sign up in Docker Hub and create an [Access Token](https://hub.docker.com/settings/security)
* Login to the Hub: `docker login -u <USER NAME> -p <ACCESS TOKEN>`
* Tag the Docker Image: `docker tag simple-translate <USER NAME>/simple-translate`
* Push to Docker Hub: `docker push <USER NAME>/simple-translate`
### Installing App on VM using Docker
* Create a VM Instance from [GCP](https://console.cloud.google.com/compute/instances)
* SSH into your newly created instance
* 



