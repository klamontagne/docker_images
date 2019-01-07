FROM python:3

RUN install -o www-data -d /var/www
USER www-data
COPY dump.py /var/www/
WORKDIR /var/www

ENV PORT=8080
EXPOSE 8080
CMD python3 /var/www/dump.py
