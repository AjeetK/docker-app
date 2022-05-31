# Docker-app (DinD)

This app is a flask based app which runs in a docker container and provides a UI to run containeron on the same host. It uses docker-python SDK.
Along with the flask app, it also runs another container called DinD container and using the UI dashboard, you can run another container inside this DinD container.

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
- It runs a DinD (Docker in Docker Container).
- Provides a dashboard to run Docker container inside DinD container
- You can apply apparmor custom profile to DinD container as well as to the container spawning inside it.

### Technology used

- Python
- Flask
- Google Cloud
- Docker
- AppArmor

### Local Setup/Installation

- Setup a Ubuntu based host. (On Virtualbox, Google-Cloud, AWS or any Cloud provider of your choice)
- If you are using cloud based host, please make sure to open port 5000 to access the application or consider changing the port in the code.
- Install [docker](https://docs.docker.com/engine/install/ubuntu/) & ([docker-compose](https://docs.docker.com/compose/install/)) on the host
- Install git with the following command:
    `sudo apt install git`
- Pull this repository (To build the image or for changing the source)
- Build/Run the app by running from project root directory:
	`docker-compose up -d`
- Check running containers with following command:
	`docker-compose ps`
- To deploy the stack on swarm:
	`docker stack deploy --compose-file docker-compose.yml dinddemo`
- Check the stack services:
	`docker stack services stackdemo`
- Access the app on `IP:5000` or `localhost:5000`
- To run a container inside another container, visit the URL - `http://<IP/localhost>:5000/dind/`
- In the textbox present in front of `dind` image, run followign command to run a container
    `docker run -d -it --security-opt "apparmor=custom" -v /sys/kernel/security:/sys/kernel/security nginx`

### Assumptions
- The `docker` host/daemon, `docker-app` is connecting to, is running on the same host.
- The docker-app is deployed on `ubuntu` based host

### Future Enhancement

- Allow `docker-app` to connect to remote docker daemon/host
- Add feature for streaming of container logs
- Show status of image getting pulled
- Feature to add cutom apparmor profile from dashboard
- More features on dashboard to see logs of child container running inside parent container.

## Contributing

- TBD

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Ajeet Khan** - [Ajeet Khan](https://github.com/ajeetk)

## License

ISC
