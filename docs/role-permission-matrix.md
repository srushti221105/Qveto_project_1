# Role-Permission Matrix – HR Management System

## 1. Introduction

The Role-Permission Matrix defines the access rights and responsibilities of different users in the HR Management System.

The system follows **Role-Based Access Control (RBAC)**, where permissions are assigned according to the user's role. This ensures that users can access only the information and features required for their responsibilities.

## 2. User Roles

The system consists of four primary roles:

### 2.1 Admin
The Admin has complete control over the HR Management System.

Responsibilities:
- Manage user accounts and assign roles.
- Create, update and deactivate employee accounts.
- Manage departments and organizational settings.
- Access all employee records.
- Monitor attendance and leave records.
- Access and manage payroll information.
- View system activity and audit logs.

### 2.2 HR
The HR department manages employee-related activities and administrative operations.

Responsibilities:
- Register and update employee information.
- Manage employee onboarding and exit processes.
- View and manage attendance records.
- Review and manage leave records.
- Generate and manage payroll.
- Manage employee departments and designations.
- Maintain employee documentation.

### 2.3 Manager
Managers supervise employees within their assigned departments or teams.

Responsibilities:
- View assigned team members.
- Monitor team attendance.
- Review leave applications.
- Approve or reject leave requests.
- View team-related employee information.
- Monitor team performance and activities.

### 2.4 Employee
Employees have access to their own personal and employment information.

Responsibilities:
- View and update permitted personal details.
- Mark daily attendance.
- View attendance history.
- Apply for leave.
- Track leave application status.
- View available leave balance.
- View their own salary details and payslips.

## 3. Role-Permission Matrix

| Features / Permissions | Admin | HR | Manager | Employee |
|---|---|---|---|---|
| Manage User Accounts | Yes | Limited | No | No |
| Assign User Roles | Yes | No | No | No |
| Add Employees | Yes | Yes | No | No |
| Update Employee Records | Yes | Yes | Limited | Own Details |
| Delete/Deactivate Employees | Yes | Yes | No | No |
| Manage Departments | Yes | Yes | No | No |
| View Employee Records | All | All | Assigned Team | Own |
| Mark Attendance | Yes | Yes | Yes | Yes |
| View Attendance | All | All | Assigned Team | Own |
| Modify Attendance Records | Yes | Yes | Limited | No |
| Apply for Leave | Yes | Yes | Yes | Yes |
| Approve/Reject Leave | Yes | Yes | Assigned Team | No |
| View Leave Records | All | All | Assigned Team | Own |
| Manage Leave Balance | Yes | Yes | No | No |
| Manage Payroll | Yes | Yes | No | No |
| View Salary Details | All | Authorized | No | Own |
| Generate Payslips | Yes | Yes | No | No |
| View Audit Logs | Yes | Authorized | No | No |

**Note:** Limited access means access is restricted to specifically authorized actions. Managers can access only employees assigned to their teams. Employees can access only their own records.

## 4. Access Control Rules

1. Every user must log in using valid credentials.
2. Each user must be assigned a role.
3. Permissions must be checked on the backend before performing any restricted operation.
4. Employees must not access another employee's personal, attendance, leave or salary information.
5. Managers can access only employees assigned to their teams.
6. HR can manage employee and payroll operations but cannot assign administrative roles.
7. Only Admin can assign or change user roles.
8. Payroll information must be accessible only to authorized users.
9. Unauthorized access attempts must be rejected.
10. Important operations must be recorded in the audit history.

## 5. Authentication and Authorization

### Authentication
Authentication verifies the identity of a user.

- Users must log in with valid credentials.
- Passwords must be stored securely using hashing.
- The system should maintain authenticated user sessions or secure tokens.
- Users must log out when their session is complete.

### Authorization
Authorization determines what an authenticated user can access.

- The system checks the user's assigned role.
- The system verifies the requested action against permissions.
- Access is granted or denied according to the role.
- Unauthorized requests return an appropriate HTTP 403 Forbidden response.

## 6. Role Management Rules

- Every user must have one active primary role.
- Only Admin can assign or modify roles.
- A user cannot grant permissions to themselves.
- Inactive users cannot access the system.
- Role changes must be recorded in the audit log.
- Permissions must be enforced at both API and application levels.

## 7. Security Requirements

- Implement Role-Based Access Control (RBAC).
- Protect sensitive employee and payroll information.
- Use secure password hashing.
- Validate user permissions for every restricted API endpoint.
- Prevent unauthorized access to employee records through URL or API manipulation.
- Maintain audit logs for important administrative activities.

## 8. Expected Outcome

The Role-Permission Matrix ensures secure and organized access to the HR Management System. It clearly separates the responsibilities of Admin, HR, Manager and Employee, prevents unauthorized access and maintains the confidentiality of employee and payroll information.
