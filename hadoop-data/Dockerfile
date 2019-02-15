FROM 10.0.1.7:5000/hadoop-all-master6:v6.1

RUN mkdir /home/data && \
    mkdir /home/code


COPY data/data/job.sql  /home/data
COPY data/data/movie.sql  /home/data
COPY data/code/*  /home/code

RUN chmod +x /data/data/auto-mysql.sh

RUN apt-get update --fix-missing
EXPOSE 22 3306 4200 8001 8088 19888 50070 9000 2181 4040 8080 8081 8888 60010 60030
CMD [ "bash","./start.sh"]
