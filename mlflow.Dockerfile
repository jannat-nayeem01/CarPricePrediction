
FROM akraradets/ait-ml-base:2023
RUN pip3 install mlflow

WORKDIR /mlflow
CMD mlflow server -h 0.0.0.0 -w 2


#FROM akraradets/ait-ml-base:2023

#RUN apt update && apt upgrade -y

#RUN pip3 install --upgrade pip
#RUN apt-get clean && rm -rf /var/lib/apt/lists/*

#WORKDIR /mlflow
#CMD mlflow server -h 0.0.0.0 -w 2Merge remote-tracking branch 'origin/main' into main


