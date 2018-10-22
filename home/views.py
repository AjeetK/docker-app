from flask import Blueprint,render_template, request, redirect, url_for
import docker, json
from utils import DockerApp

home_view = Blueprint('home_view', __name__)

@home_view.route('/')  # Route for the page
def display_home_page():
    return render_template('home.html')

@home_view.route('/images/') # Route to list docker images
def display_images():
    cl = DockerApp()
    data = cl.get_images()
    if 'exception' not in data:
        message = request.args.get("message", "")
        return render_template('images.html', data=data, message=message)
    else:
        return render_template('exception.html', data=data)

@home_view.route('/image/<string:id>', methods=['GET'])  # Route for single image page
def display_image(id):
    client = DockerApp()
    data = client.get_image(id)
    if 'exception' not in data:
        return render_template('image.html', data=data)
    else:
        return render_template('exception.html', data=data)

@home_view.route('/containers')  # Route for list of containers page
def display_containers():
    client = DockerApp()
    data = client.get_containers()
    if 'exception' not in data:
        return render_template('containers.html', data=data)
    else:
        return render_template('exception.html', data=data)

@home_view.route('/container/<string:id>')  # Route for single container page
def display_container(id):
    client = DockerApp()
    data = client.get_container(id)
    if 'exception' not in data:
        return render_template('container.html', data=data)
    else:
        return render_template('exception.html', data=data)

@home_view.route('/runcontainer/<string:container_id>', methods=['POST'])  # Route for run-container page
def exec_container(container_id):
    client = DockerApp()
    if request.method == "POST":
        command = request.form['command']
        port = request.form['port']
        data = client.run_container(container_id,command, port)
        if 'exception' not in data:
            redirect_url = "/container/" + data["id"]
            return redirect(redirect_url)
        else:
            return render_template('exception.html', data=data)
    else:
        return render_template('exception.html', data=data)


@home_view.route('/stopcontainer/<string:container_id>')  # Route for stop-container
def stop_container(container_id):
    client = DockerApp()
    data = client.stop_container(container_id)
    if 'exception' not in data:
        redirect_url = "/container/" + data["id"]
        return redirect(redirect_url)
    else:
        return render_template('exception.html', data=data)

@home_view.route('/addimage', methods=['POST'])
def add_image():
    client = DockerApp()
    if request.method == "POST" and request.form['imagename']:
        imagename = request.form['imagename']
        data = client.add_image(imagename)
        info = imagename + " will be added if it exists on docker hub"
    else:
        info = "Please provide image name"
    return redirect(url_for('.display_images', message=info))

@home_view.route('/containerlogs/<string:id>')
def display_logs(id):
    client = DockerApp()
    data = client.get_container_logs(id)
    if 'exception' not in data:
        return render_template('containerlogs.html', data=data)
    else:
        return render_template('exception.html', data=data)
