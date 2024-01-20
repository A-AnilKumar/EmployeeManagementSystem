# Employee Management System

This is a basic Employee Management System implemented in Python with MySQL as the database.

## Features

- Add new employees
- View employee details
- Update employee information
- Remove employees
- Promote Employee

## Prerequisites

- Python 3.x
- MySQL

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/EmployeeManagementSystem.git
    cd EmployeeManagementSystem
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Configure MySQL:

    - Create a MySQL database named `employeemanagement`.
    
4. Run the application:

    ```bash
    python main.py
    ```

## Database Schema

The system uses a simple MySQL database with the following schema:

```sql
CREATE TABLE employees (
    EmpId INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Role VARCHAR(255),
    Salary INT,
    ....... // as per requirements
);
