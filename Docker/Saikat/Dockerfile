FROM ubuntu:20.04
LABEL "test"="first test case"
#RUN echo "deb https://nginx.org/packages/ubuntu/ focal nginx" >> /etc/apt/sources.list
#RUN echo "deb-src https://nginx.org/packages/ubuntu/ focal nginx" >> /etc/apt/sources.list
RUN apt update && apt upgrade -y && apt install nginx -y
RUN service nginx restart
EXPOSE 80
WORKDIR /var/www/html
VOLUME /var/log/nginx
ADD html.kitchen.tar.gz /var/www/html
CMD ["nginx","-g","daemon off;"]
