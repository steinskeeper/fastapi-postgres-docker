# FastAPI + Postgres + Docker Compose + Heroku Deploy


### Features
1. FastAPI with Postgres setup
2. Docker container with docker-compose
3. JWT User Authentication
4. Modular Project Structure
5. Heroku Deploy with Githu Actions
6. Manage Migrations with Alembic script

# TO-DO when Running on Local Machine
1. Change `entrypoint.sh` file from
    ```
   #!/bin/bash
    alembic upgrade head
    uvicorn app.server:app --reload --host 0.0.0.0 --port $PORT
    ```
    To
    
    ```
    #!/bin/bash
    alembic upgrade head
    uvicorn app.server:app --reload --host 0.0.0.0 --port 5000
    ```

# If there is any changes to Database Schema
1. `$ sh mig.sh`
   Example 
   ```
   sh mig.sh
   Enter the Migration File name : 
   cluster groups org
   ```
   The resulting file name will be
   `21ce965c935e_cluster_groups_org.py`

2. Commit the migration files.

# When Pushing to Main
1. Change back --port 5000 to --port $PORT in `entrypoint.sh`
 

