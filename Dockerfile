FROM python:3.11-slim

WORKDIR /app
COPY flask_example.py /app/
COPY config.json /app/
COPY requirments.txt /app/
COPY printColors.py /app/

RUN pip3 install -r requirments.txt

ENV HOST_IP=127.0.0.1

EXPOSE 5000

CMD ["python", "flask_example.py"]



