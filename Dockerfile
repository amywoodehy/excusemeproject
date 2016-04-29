FROM tiangolo/uwsgi-nginx:latest
ADD . /excusemeproject
WORKDIR /excusemeproject
COPY nginx.conf /etc/nginx/conf.d/
RUN apt-get install libffi-dev
RUN pip install -r requirements.txt
RUN apt-get autoremove -y