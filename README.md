Welcome to the Todo application! This is a simple yet powerful task management tool built using Bootstrap for styling, HTML/CSS for the frontend, and Django for the backend. The application uses SQLite as its database and provides a seamless experience for managing your tasks.

Features![Screenshot from 2025-03-23 17-03-22](https://github.com/user-attachments/assets/1fbbbf24-c3f0-494e-9277-eecf091e2a0a)

Welcome Page: A landing page with options to register, login, or directly access the task list.

Registration Page: Allows new users to create an account.![Screenshot from 2025-03-23 17-03-30](https://github.com/user-attachments/assets/714464a4-775e-4acf-9b21-5efd9987e714)


Login Page: Enables existing users to log in.![Screenshot from 2025-03-23 17-03-35](https://github.com/user-attachments/assets/660a5de4-5988-4f59-bb5a-a88de04f2df2)


Task List Page: Displays all tasks associated with the logged-in user.![Screenshot from 2025-03-23 17-04-02](https://github.com/user-attachments/assets/50be5ecf-7f6f-4506-bb17-f2c1cf27edd7)


Add Task Page: Allows users to add new tasks.![Screenshot from 2025-03-23 17-04-07](https://github.com/user-attachments/assets/0abb7e85-4ea4-49d9-8378-0bcdc20d4d5f)


Edit Task Page: Enables users to modify existing tasks.![Screenshot from 2025-03-23 17-04-14](https://github.com/user-attachments/assets/5c2c22ae-bdf2-4f31-947b-8e2fce89e247)


Delete Task Page: Provides an option to delete tasks.![Screenshot from 2025-03-23 17-04-22](https://github.com/user-attachments/assets/908ffc99-9c16-47b7-acb3-2ddc549bac8a)


Admin Panel
The admin panel can be accessed using the following credentials:

Username: Meer

Password: 797122

If you want to change the admin username or password, follow the instructions below.

Screenshots
Screenshots of all the pages are available in the GitHub repository's README file. Check them out to get a visual understanding of the application.

How to Run the Project Locally
Follow these steps to run the Todo application on your local machine:

Step 1: Clone the Repository
Clone the repository to your local machine using the following command:

bash
Copy
git clone https://github.com/your-username/Todo-App.git
Step 2: Navigate to the Project Folder
Go to the project directory:

bash
Copy
cd Todo-App
Step 3: Set Up a Virtual Environment
Create a virtual environment to isolate the project dependencies:

bash
Copy
python -m venv venv
Activate the virtual environment:

On macOS/Linux:

bash
Copy
source venv/bin/activate
On Windows:

bash
Copy
venv\Scripts\activate
Step 4: Install Dependencies
Install the required dependencies using the following command:

bash
Copy
pip install -r requirements.txt
Step 5: Run Migrations
Apply the database migrations to set up the SQLite database:

bash
Copy
python manage.py migrate
Step 6: Create a Superuser (Admin)
Create a superuser to access the Django admin panel:

bash
Copy
python manage.py createsuperuser
Follow the prompts to set a username, email, and password for the admin account.

Step 7: Run the Development Server
Start the Django development server:

bash
Copy
python manage.py runserver
Step 8: Access the Application
Open your browser and go to http://127.0.0.1:8000/ to access the application.

Changing Admin Username and Password
If you want to change the username or password of the admin account, follow these steps:

Access the Django Shell:
Run the following command to open the Django shell:

bash
Copy
python manage.py shell
Update Admin Credentials:
Use the following Python commands to change the username and password:

python
Copy
from django.contrib.auth.models import User
user = User.objects.get(username='Meer')  # Replace 'Meer' with the current username
user.username = 'new_username'  # Set a new username
user.set_password('new_password')  # Set a new password
user.save()
Exit the Shell:
Type exit() and press Enter to exit the Django shell.

