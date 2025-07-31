# Movie-Management-System
Movie Management System For Efficiently Managing Your Movie Database

In MySQL Workbench, they can:
  Go to: Server > Data Import
  Choose: "Import from Self-Contained File"
  Select your movielist.sql file
  Choose "New Database" or select an existing one
  Click Start Import
         OR
## 🗃️ How to Set Up the Database

1. Install MySQL
2. Create a new database called `movielist`
3. Import the SQL file:

```bash
mysql -u root -p movielist < database/movielist.sql
