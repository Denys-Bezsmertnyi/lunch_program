FROM python:3.12

# Set the working directory in the container
WORKDIR /code

# Copy the requirements file into the container
COPY pyproject.toml poetry.lock /code/

# Install Poetry
RUN pip install poetry

# Install dependencies
RUN poetry config virtualenvs.create false && poetry install

# Copy the rest of the application code into the container
COPY . /code/

# Run the command to start the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
