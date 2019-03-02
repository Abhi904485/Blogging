
FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /Blogging
COPY requirements.txt /Blogging
WORKDIR /Blogging/
RUN pip install -r requirements.txt
COPY . /Blogging/
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]