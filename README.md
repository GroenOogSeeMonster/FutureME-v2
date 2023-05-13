# FutureMe Application

## Overview

The FutureMe application is a self-improvement and habit-building web app that provides users with a set of assessments to complete in a specific order. These assessments involve user text input, some with time limits. After completing all tasks, users can set up a daily routine to follow, which will be emailed to them in an attachment form.

The application is built with Flask for the backend, a MySQL database, and Celery for scheduling tasks (like sending emails). It's designed to be run in a Docker environment for easy setup and deployment.

## File Structure

```plaintext
/futureme
  /app
    /main
      __init__.py
      errors.py
      forms.py
      views.py
    /static
      /css
        styles.css
    /templates
      base.html
      home.html
      login.html
      register.html
      ...
    __init__.py
    models.py
  /migrations
  .env
  config.py
  docker-compose.yml
  Dockerfile-app
  Dockerfile-celery-beat
  Dockerfile-celery-worker
  requirements.txt
  run.py
```
## Running the Application
### Prerequisites  
You need Docker and Docker Compose installed on your machine to run this application.
  
### Clone the repository  
`git clone https://github.com/yourusername/futureme.git  `

### Navigate to the project directory
`cd futureme   `

### Build the Docker images
`docker-compose build   `

### Start the services
`docker-compose up -d   `

### Initialize the database
`docker-compose run --rm app flask db upgrade   `

Your application should now be running at localhost:5000.