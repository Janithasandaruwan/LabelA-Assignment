FROM python:3.9
LABEL author='Label A'

WORKDIR /app

# Environment
RUN apt-get update
RUN apt-get install -y bash vim nano postgresql-client
RUN pip install --upgrade pip

ENV DJANGO_SETTINGS_MODULE=autocompany.settings

# Major pinned python dependencies
RUN pip install --no-cache-dir flake8==3.8.4 uWSGI

# Regular Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy our codebase into the container
COPY . .

RUN chmod u+x ./manage.py
RUN chmod u+x ./entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]