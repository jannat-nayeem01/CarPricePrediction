FROM python:3.9-bookworm

RUN pip3 install numpy
RUN pip3 install seaborn
RUN pip3 install matplotlib
RUN pip3 install jupyterlab

RUN pip3 install ipykernel
RUN pip3 install dash
RUN pip3 install pandas
RUN pip3 install dash-bootstrap-components
RUN pip3 install scikit-learn
RUN pip3 install ppscore
RUN pip3 install plotly
RUN pip3 install xgboost


CMD tail -f /dev/null