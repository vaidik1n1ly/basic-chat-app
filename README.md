# basic-chat-app
> Requires `redis` to run on host pc or docker container.

### Steps to Setup Django

1. Clone the repository:

   ```bash
   git clone https://github.com/vaidik1n1ly/basic-chat-app.git
   
2. Create a virtual environment inside project directory (recommended):

   ```bash
   cd basic-chat-app
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   
3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt

4. Run migrations to set up the database:

   ```bash
   python manage.py migrate

5. Run the development server:

   ```bash
   python manage.py runserver

6. Visit the site in your browser at http://127.0.0.1:8000.

---
### Steps to setup `redis`

1. Install `docker desktop`
   ```
   https://docs.docker.com/desktop/setup/install/windows-install/

3. Create `docker-compose.yml` file on app root directory with following content:
   ```yml
   services:
       redis:
           image: redis:latest
           container_name: redis
           ports:
               - "6379:6379"

4. build and run docker container
   ```cmd
   docker-compose build
   docker-compose up
   docker-compose up -d
