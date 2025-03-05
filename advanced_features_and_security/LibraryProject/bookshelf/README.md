In this project, custom permissions are defined for the Book model, and groups are created to control user access. The following permissions are implemented:

can_view: Permission to view a book.
can_create: Permission to create a new book.
can_edit: Permission to edit a book.
can_delete: Permission to delete a book.
The groups created include:

Viewers: Can only view books.
Editors: Can create, edit, and delete books.
Admins: Full access to view, create, edit, and delete books.
Setup Instructions
Define Permissions in Models
Permissions are defined in the Book model under the Meta class. Custom permissions like can_view, can_create, can_edit, and can_delete are created.

Create Groups and Assign Permissions
Groups such as Editors, Viewers, and Admins are created, and the appropriate permissions are assigned to each group. You can do this either programmatically or using Django's admin interface.

