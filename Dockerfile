# tells Docker which image to base our container on

FROM python:3.12.3-slim


# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE=1


# Set the working directory inside container
WORKDIR /Tweet-App/SocialMediaApp

# Copy requirements.txt to the working directory
COPY requirements.txt /Tweet-App/

#installing python dependencies
RUN pip install --upgrade pip && pip install -r /Tweet-App/requirements.txt

# Copy the entire project into the container
COPY . /Tweet-App/

EXPOSE 8000

# Set the default command to run Django’s development server
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
