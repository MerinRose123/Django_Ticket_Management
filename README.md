# Django_Ticket_Management
Project to manage tickets which includes user login and registration.
Migrate _initial migration first.Then create a new migration using command in terminal
python manage.py --empty user_management --settings=TicketProject.settings.local.
Copy the migration which is to create group to the newly created migration and migrate all migrations.
This process is to create groups.
call register url first to register a user as super_admin.Then go to default page with root url.
Now login using the currently registered user.
