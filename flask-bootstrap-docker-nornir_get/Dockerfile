FROM python

WORKDIR /flask-docker
COPY . .
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

