FROM python:3.6

# create root directory for our project in the container

RUN mkdir /FileUpload

# Set the working directory to /FileUpload
WORKDIR /FileUpload

# Copy the current directory contents into the container at /FileUpload
ADD . /FileUpload

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT [ "python3.6", "manage.py"]

CMD [ "runserver", "0.0.0.0:8000"]



