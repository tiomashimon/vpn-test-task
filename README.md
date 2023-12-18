Running the Project

Follow these steps to set up and run the project on your local machine.

Prerequisites
Docker: Make sure you have Docker installed on your machine. You can download it from here.
Installation Steps

1.Clone the Repository

git clone https://github.com/tiomashimon/vpn-test-task.git

cd vpn-test-task

2.Create Environment File

Add a .env file in the project root with the following content:

SECRET_KEY=vus65*qj@s-vg$!s45z!$jl#)@mzk&gs!7m7%tv9hj=12m55gz

DB_NAME=taskdb

DB_USER=task

DB_PASSWORD=20task23

DB_HOST=db

DB_PORT=5432

POSTGRES_PASSWORD=20task23

POSTGRES_USER=task

POSTGRES_DB=taskdb

EMAIL_HOST_USER=teamchallangechat@ukr.net

EMAIL_HOST_PASSWORD=gm7B5FpsJNDzWcPb

3.Build Docker Images

docker-compose build

4. Run Docker Containers


docker-compose up

This will start the necessary containers and run the project. You can access the project at http://localhost:8000.

Additional Notes

Make sure no other services are using ports 5432 and 8000 on your machine.
You may need to use sudo or run Docker commands with administrator privileges based on your operating system.
Now, your project should be up and running locally!
