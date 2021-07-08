FROM python:3.9

LABEL maintenance="Rodrigo"

RUN pip install --upgrade pip

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

# command to run on container start
CMD [ "python", "volume_calculator/volume_calculator.py" ]
