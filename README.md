# poeladderapp

## introduction
Hobby project web app to show filtered ladder info from path of exile for me and my friends.

## repository
- /app directory contains the application code and docker file
- /deploy directory contains the kubernetes yaml files
- /doc contains overview documentation of the technical architecture

## useful commands
A list of commands that I found useful while working on this project and that I don't want to forget about.
- `docker buildx build -t jasper9119/nginx-poe-arm64 --platform linux/arm64 .` to build nginx app
- `docker buildx build -t jasper9119/poedata-arm64 --platform linux/arm64 .` to build poedata app
- `docker run -d -p 80:8080 jasper9119/nginx-poe-arm64:latest` to run nginx app
- `docker run -d -p 5000:5000 jasper9119/poedata-arm64:latest` to run poedata app locally
- `kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.10.1/deploy/static/provider/cloud/deploy.yaml` to install the ingress controller
- `kubectl apply -f myfile` to apply any file to kubernetes
- `workon myvirtualenvname` to activate a python virtual environment of virtualenvwrapper


