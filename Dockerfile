FROM python:3.7.4

LABEL maintenance="Rodrigo"

RUN pip install --upgrade pip

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .
WORKDIR /usr/src/app/volume_calculator

# command to run on container start
CMD ["python", "__init__.py"]
