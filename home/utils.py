"""
Module with DockerApp class having method to perform following actions:
- get image list
- get details of particular image
- get container list
- get details of particular container
- get logs of particular container
- run container with command provided and ports to expose
- stop a running container
- add an image
"""

import docker, json, threading

class DockerApp(object):
    """DockerApp class containers methods for container management operations"""

    def __init__(self, DOCKER_HOST="localhost", DOCKER_TLS_VERIFY=None, DOCKER_CERT_PATH=None):
        super(DockerApp, self).__init__()
        self.client = docker.from_env(timeout=180)

    def get_images(self):
        """ Returns list(dict) of images 
              Example -
                [
                    {
                        "id": "89sddsls",
                        "tags": "busybox:latest",
                        "Author": "ajeetkhan"
                    }
                ]
            Params:
                id(string): id of the image
            }
        """
        data = [] # list of images to be returned
        try:
            for image in self.client.images.list():
                image_list = dict(id=image.short_id, tags=image.tags, author=image.attrs["Author"])
                data.append(image_list)
            return data
        except Exception as e:
            data = {'exception': "Looks like docker daemon is not running on the server!"}
            return data

    def get_image(self, id):
        """
        Accepts image-id as an argument
        Returns a dictionary having image information
        """
        try:
            image = self.client.images.get(id)
            data = image.attrs
            return data
        except Exception as e:
            data = {'exception': "Either docker daemon is not running or Image no more exist on the server"}
            return data

    def get_containers(self):
        """Returns list of containers"""
        data = []
        # available - id, name, status, labels, image and more
        try:
            for container in self.client.containers.list(all):
                container_list = dict(id=container.short_id, name=container.name, 
                            status=container.status, createdAt=container.attrs["Created"])
                data.append(container_list)
            return data
        except Exception as e:
            data = {'exception': "Looks like docker daemon is not running on the server!"}
            return data

    def get_container(self, container_id):
        """
        Accepts container-id as an argument
        Returns a dictionary having information for container-id provided

        """
        try:
            result = self.client.containers.get(container_id)
            container_data = dict(name=result.name, image=result.attrs["Config"]["Image"],
                                  volumes=result.attrs["Config"]["Volumes"], command=result.attrs["Config"]["Cmd"][0],
                                  entrypoint=result.attrs["Config"]["Entrypoint"], created=result.attrs["Created"],
                                  status=result.status, ports=result.attrs["NetworkSettings"]["Ports"], id=result.short_id,
                                  restart_count=result.attrs["RestartCount"])
            return container_data

        except Exception as e:
            container_data = {'exception': "Container Not Found!"}
            return container_data


    def run_container(self, container_id, command, port):
        """
        Accepts container-id, command to run and port to be exposed
        Returns information corresponding to contianer-id
        """
        port_dict = {}
        if port:
            port_list = port.split(',')
            for i in port_list:
                temp = i.split(":")
                key = temp[0] + "/tcp"
                port_dict[key] = temp[1]
        try:
            result = self.client.containers.run(image = container_id,volumes={'/var/run/docker.sock':{'bind': '/var/run/docker.sock', 'mode': 'rw'}}, command = command, detach=True, ports=port_dict)
            container_data = dict(name=result.name, image=result.attrs["Config"]["Image"],
                                  volumes=result.attrs["Config"]["Volumes"], command=result.attrs["Config"]["Cmd"][0],
                                  entrypoint=result.attrs["Config"]["Entrypoint"], created=result.attrs["Created"],
                                  status=result.status, ports=result.attrs["NetworkSettings"]["Ports"], id=result.short_id,
                                  restart_count=result.attrs["RestartCount"])
            return container_data
        except Exception as e:
            data = {'exception': "Either docker daemon is not running or Image no more exist on the server"}
            return data

    def show_dind(self):
        """Returns list of containers"""
        data = []
        # available - id, name, status, labels, image and more
        try:
            for container in self.client.containers.list(all):
                container_list = dict(id=container.short_id, name=container.name, 
                            status=container.status, createdAt=container.attrs["Created"])
                data.append(container_list)
            return data
        except Exception as e:
            data = {'exception': "Looks like docker daemon is not running on the server!"}
            return data

    def run_dind(self, container_id, command):
        """
        Accepts image-id, command to run and port to be exposed
        Returns information corresponding to image
        """
        # port_dict = {}
        # if port:
        #     port_list = port.split(',')
        #     for i in port_list:
        #         temp = i.split(":")
        #         key = temp[0] + "/tcp"
        #         port_dict[key] = temp[1]
        try:
            container = self.client.containers.get(container_id)
            result = container.exec_run(cmd=command)
            data = tuple(result)
            return data
        except Exception as e:
            print(e)
            data = {'exception': "Either docker daemon is not running or Image no more exist on the server"}
            return data

    def show_all_dind_container(self):
        try:
            for container in self.client.containers.list(all):
                container_list = dict(id=container.short_id, name=container.name, 
                            status=container.status, createdAt=container.attrs["Created"])
                if "dind" in container_list["name"]:
                    dind_container_id = container_list["id"]
                    dind_container = self.client.containers.get(dind_container_id)
                    data = dind_container.exec_run(cmd="docker ps -a")
            return data
        except Exception as e:
            data = {'exception': "Looks like docker daemon is not running on the server!"}
            return data


    def get_container_logs(self, id):
        """
        Accepts container-id as an argument
        Returns dictionary with 'logs' as key and the actual log content in value
        """
        try:
            container = self.client.containers.get(id)
            data = dict(logs=container.logs())
            return data
        except Exception as e:
            container_data = {'exception': "Container Not Found!"}
            return container_data

    def stop_container(self, container_id):
        try:
            container = self.client.containers.get(container_id)
            container.stop(timeout=0)
            container_data = dict(name=container.name, image=container.attrs["Config"]["Image"],
                                  volumes=container.attrs["Config"]["Volumes"], command=container.attrs["Config"]["Cmd"][0],
                                  entrypoint=container.attrs["Config"]["Entrypoint"], created=container.attrs["Created"],
                                  status=container.status, ports=container.attrs["NetworkSettings"]["Ports"], id=container.short_id,
                                  restart_count=container.attrs["RestartCount"])
            return container_data
        except Exception as e:
            data = {'exception': "Either container do not exist, or its already stopped"}
            return data

    def pull_image(self, imagename):
        """Accepts imagename as an argument and pull the image from docker hub"""
        self.client.images.pull(imagename)

    def add_image(self, imagename):
        """
        Accepts image-name as an argument and spawn a thread to pull image in background
        """
        thread = threading.Thread(target=self.pull_image, args=(imagename,))
        thread.daemon = True
        thread.start()


if __name__ == '__main__':
    pass
