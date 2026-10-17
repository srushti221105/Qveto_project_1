# Qveto Project 1 — Database Design

## 1. Project Objective
Design a database for a Smart HR and Employee Management System that manages employee information, attendance, leave requests, payroll, user roles, and permissions.

## 2. User Roles
- Admin: Manage users, roles, departments, and system settings.
- HR: Manage employee records, attendance corrections, leave requests, and payroll.
- Manager: View assigned team records and approve or reject team leave requests.
- Employee: View their own profile, mark attendance, apply for leave, and view their own payroll details.

## 3. Proposed Database Tables

### 3.1 Users
Stores authentication account information.
- id — Primary key
- username
- email
- password_hash
- is_active
- date_joined

Use Django's authentication system rather than storing passwords directly.

### 3.2 Roles
Defines application roles and their permissions.
- id — Primary key
- name — Admin, HR, Manager, Employee
- description

Coordinate with the backend team to determine whether Django Groups will provide the role implementation.

### 3.3 Departments
Stores company department information.
- id — Primary key
- name
- description
- is_active

### 3.4 Employees
Stores employee profile information.
- id — Primary key
- user_id — Foreign key to the authentication user
- employee_code — Unique
- first_name
- last_name
- phone
- department_id — Foreign key to Departments
- manager_id — Foreign key to Employees, nullable
- date_of_joining
- employment_status

### 3.5 Attendance
Stores daily employee attendance.
- id — Primary key
- employee_id — Foreign key to Employees
- attendance_date
- check_in
- check_out
- status
- corrected_by — Foreign key to Users, nullable
- correction_reason
- created_at
- updated_at

Prevent duplicate attendance records for the same employee and date unless the requirements allow multiple shifts.

### 3.6 Leave Types
Defines available leave categories.
- id — Primary key
- name
- description
- annual_limit

### 3.7 Leave Requests
Stores employee leave applications and decisions.
- id — Primary key
- employee_id — Foreign key to Employees
- leave_type_id — Foreign key to Leave Types
- start_date
- end_date
- reason
- status
- reviewed_by — Foreign key to Users, nullable
- reviewed_at
- created_at

### 3.8 Payroll Records
Stores employee payroll information.
- id — Primary key
- employee_id — Foreign key to Employees
- pay_period_start
- pay_period_end
- basic_salary
- allowances
- deductions
- net_salary
- payment_status
- processed_by — Foreign key to Users
- created_at

Restrict payroll creation and modification to authorized backend roles. Protect salary information from unauthorized access.

### 3.9 Audit Logs
Records important security-sensitive actions.
- id — Primary key
- actor_user_id — Foreign key to Users, nullable
- action
- resource_type
- resource_id
- timestamp
- outcome

Record appropriate actions involving sensitive records, permission failures, attendance corrections, and payroll changes. Avoid logging passwords, tokens, or unnecessary sensitive data.

### 3.10 System Settings
Stores configurable application settings.
- id — Primary key
- setting_key — Unique
- setting_value
- updated_by — Foreign key to Users, nullable
- updated_at

## 4. Main Relationships
- One department can have many employees.
- One manager can supervise multiple employees.
- One employee can have multiple attendance records.
- One employee can submit multiple leave requests.
- One leave type can be associated with multiple leave requests.
- One employee can have multiple payroll records.
- One user can perform multiple audited actions.

## 5. Security Requirements
1. Authentication is required for protected APIs.
2. Employees can access only their own personal, attendance, leave, and payroll records.
3. Managers can access only records belonging to their assigned teams.
4. Only authorized roles can create or modify payroll.
5. Backend APIs must enforce permissions for every protected operation.
6. Sensitive record access and modifications must be audited where required.

## 6. Implementation Status
- [ ] Confirm schema with the backend team
- [ ] Confirm authentication and role implementation
- [ ] Finalize table columns and constraints
- [ ] Create the ER diagram
- [ ] Implement Django models
- [ ] Create and test database migrations
- [ ] Test access restrictions and data integrity
