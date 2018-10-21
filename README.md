# Docker-app

docker-app is a web-app built in flask to list containers/images and allow operations like add-image, run-container, stop-container.

### Features:

- List all containers
- List all available images
- Information page for each container
- Information page for each image
- Stop a running container
- Delete an existing image
- Add a new image
- start a new container [It asks for the command to run and ports to expose]
- To look at logs of a running container

### Technology used

- Python
- Flask
- AWS Cloud
- Terraform
- Docker

### Local Setup/Installation

- Terraform installed on your workstation with proper aws IAM credentials/access
- To run the app on workstation
	- Install docker on your workstation
	- Run after building the docker image manually:
		- Pull this repository (To build the image or for changing the source)
		- Build the docker image by running from project root directory:
			`docker build -t ajeetkhan/docker-app:latest .`
		- Run the image:
			`docker run -d -p 5000:5000 -v /var/run/docker.sock:/var/run/docker.sock  ajeetkhan/docker-app:latest`
	- Run directly by pulling it from docker hub:
		- Pull the image:
			`docker pull ajeetkhan/docker-app:latest`
		- Run the image:
			`docker run -d -p 5000:5000 -v /var/run/docker.sock:/var/run/docker.sock  ajeetkhan/docker-app:latest`
	- Access the app on `localhost:5000`

### Deploy On AWS EC2 Instance

- Make sure you have terraform installed on your workstation
- Pull terraform script from [here](https://github.com/AjeetK/docker-app-terraform)
- Change VPC CIDR, REGION and other variables in `variables.tf` file
- Run `terraform plan` to check what all resources will be created
- Run `terraform apply` to actually create the resources
- On successfull creation of EC2 instance, hit public IP of the instance in browser to access the app
- If app isn't running on the public IP, check the logs of `userdata` in instance at `/var/log/userdata.log`
- Add a DNS entry of your domain poiniting to the public IP of instance

### Assumptions
- The `docker` host/daemon, `docker-app` is connecting to, is running on the same host.

### Future Enhancement

- Allow `docker-app` to connect to remote docker daemon/host
- Add feature for streaming of container logs
- Show status of image getting pulled

## Contributing

- TBD

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Ajeet Khan** - [Ajeet Khan](https://github.com/ajeetk)

## License

ISC
