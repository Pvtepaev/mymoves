FROM ubuntu:latest
RUN apt update && apt install -y python-dev python-pip build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8000
ENTRYPOINT ['python']
CMD ['main.py']
