import mysql.connector

# making Connection
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="employeemanagement"
)

def create_table(cursor):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Employees(
        EmpId INT AUTO_INCREMENT PRIMARY KEY,
        Name VARCHAR(255),
        Role VARCHAR(255),
        Salary DECIMAL(10,2)
    )
    """
    cursor.execute(create_table_query)

def table_exists(cursor, table_name):
    cursor.execute(f"SHOW TABLES LIKE '{table_name}'")
    return cursor.fetchone() is not None

cursor = con.cursor()
table_name = "Employees"

if not table_exists(cursor, table_name):
    create_table(cursor)

# Function to Add Employee
def Add_Employee():
    empId = input("Enter Employee EmpId: ")

    # Checking if Employee with given EmpId Already Exists or Not
    if check_employee(empId):
        print("*" * 40)
        print("Employee already exists\nTry Again\n")
        menu()
    else:
        print("-" * 40)
        name = input("Enter Employee Name: ")
        role = input("Enter Employee Role: ")
        salary = input("Enter Employee Salary: ")
        print("-" * 40)
        data = (name, role, salary)

        # Inserting Employee details into the Employee Table
        sql = "INSERT INTO Employees (Name, Role, Salary) VALUES (%s, %s, %s)"
        cursor.execute(sql, data)

        # commit() method to make changes in the table
        con.commit()
        print("*" * 40)
        print("Employee Added Successfully")
        menu()

# Function to Remove Employee with given EmpId
def Remove_Employee():
    empId = input("Enter Employee EmpId: ")

    # Checking if Employee with given EmpId Exists or Not
    if not check_employee(empId):
        print("*" * 40)
        print("Employee does not exist\nTry Again\n")
        menu()
    else:
        # Query to Delete Employee from Table
        sql = "DELETE FROM Employees WHERE EmpId = %s"
        cursor.execute(sql, (empId,))

        # commit() method to make changes in the table
        con.commit()
        print("*" * 40)
        print("Employee Removed")
        menu()

def check_employee(employee_id):
    # Use parameterized query to prevent SQL injection
    sql = "SELECT * FROM Employees WHERE EmpId = %s"

    # Making cursor buffered to make rowcount method work properly
    with con.cursor(buffered=True) as cursor:
        data = (employee_id,)

        # Use the context manager for the cursor
        cursor.execute(sql, data)

        # Use rowcount method to find the number of rows with given values
        row_count = cursor.rowcount

    return row_count == 1



def Promote_Employee():
    empId = int(input("Enter Employee's EmpId: "))

    # Checking if Employee with given EmpId Exists or Not
    if not check_employee(empId):
        print("*" * 40)
        print("Employee does not exist\nTry Again\n")
        menu()
    else:
        role = input("Enter the new role: ")
        amount = int(input("Enter increase in Salary:"))

        # Query to Fetch Salary of Employee with given EmpId
        sql_select = f"SELECT salary FROM Employees WHERE EmpId = {empId}"
        data_select = (empId,)
        c = con.cursor()

        # Executing the SQL Query
        c.execute(sql_select, data_select)

        # Fetching Salary of Employee with given EmpId
        r = c.fetchone()
        current_salary = r[0]
        new_salary = current_salary + amount

        # Query to Update Salary of Employee with given EmpId
        sql_update = f"UPDATE Employees SET salary = {new_salary}, Role = '{role}' WHERE EmpId = {empId}"
        data_update = (new_salary, role, empId)

        # Executing the SQL Query
        c.execute(sql_update, data_update)

        # commit() method to make changes in the table
        con.commit()
        print("*" * 40)
        print("Employee Promoted")
        menu()

# Function to Display All Employees from Employee Table
def Display_Employees():
    # query to select all rows from Employee Table
    sql = 'select * from Employees'
    c = con.cursor()

    # Executing the SQL Query
    c.execute(sql)

    # Fetching all details of all the Employees
    r = c.fetchall()
    print("*" * 40)
    print("Employee details")
    print("*" * 40)

    if(len(r) > 0):
        for i in r:
            print("Employee EmpId : ", i[0])
            print("Employee Name : ", i[1])
            print("Employee Role : ", i[2])
            print("Employee Salary : ", i[3])
            print("-" * 40)
    if(len(r) == 0):
        print("NO EMPLOYEE TO FETCH/DISPLAY")  
    menu()


# menu function to display menu
def menu():
    print("*" * 40)
    print("Welcome to Employee Management Record")
    print("*" * 40)
    print("Pick your choice (1 to 5): ")
    print("1 => Add Employee")
    print("2 => Remove Employee")
    print("3 => Promote Employee")
    print("4 => Display Employees")
    print("5 => Exit")

    choice = int(input("Enter your Choice: "))
    if choice == 1:
        Add_Employee()
    elif choice == 2:
        Remove_Employee()
    elif choice == 3:
        Promote_Employee()
    elif choice == 4:
        Display_Employees()
    elif choice == 5:
        exit(0)
    else:
        print("Invalid Choice")
        menu()

# Calling menu function
menu()

con.commit()
con.close()
