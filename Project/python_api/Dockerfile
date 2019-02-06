FROM python:3.7-stretch
WORKDIR /python_api/
ADD . /python_api/
RUN pip install -r requirements.txt
EXPOSE 80
CMD ["python", "./app.py"]