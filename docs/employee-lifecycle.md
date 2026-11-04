# Employee Lifecycle – HR Management System

## 1. Introduction

Employee Lifecycle Management refers to managing all stages of an employee's journey within an organization, from initial registration and onboarding to resignation or termination.

The HR Management System provides a centralized platform to manage employee information and track their employment status throughout this lifecycle.

## 2. Stages of Employee Lifecycle

The employee lifecycle consists of the following stages:

1. Employee Registration
2. Employee Onboarding
3. Active Employment
4. Employee Profile Management
5. Department and Role Assignment
6. Resignation or Termination
7. Employee Exit Process

## 3. Employee Registration

When a new employee joins the organization, HR or Admin creates their employee record.

Required information includes:
- Employee ID
- Full Name
- Email Address
- Contact Number
- Date of Birth
- Gender (optional)
- Address
- Department
- Designation
- Date of Joining
- Employment Type
- Reporting Manager
- Employment Status

**Business Rules:**
- Every employee must have a unique Employee ID.
- Email addresses must be unique.
- Mandatory fields must be validated before saving.
- Only authorized HR or Admin users can register employees.

## 4. Employee Onboarding

Onboarding is the process of completing the formal joining activities of a new employee.

Activities include:
- Creating employee login credentials.
- Assigning a department and designation.
- Assigning a reporting manager.
- Collecting required documents.
- Providing access to the HR Management System.
- Setting the initial employment status to Active once joining is confirmed.

**Business Rules:**
- Only authorized users can complete onboarding.
- Employee records must be created before system access is provided.
- Employee information must be stored securely.

## 5. Active Employment

After onboarding, the employee becomes an active member of the organization.

During this stage, the system manages:
- Daily attendance.
- Check-in and check-out records.
- Leave applications and approvals.
- Employee information updates.
- Salary and payroll records.
- Department and designation details.

**Business Rules:**
- Only active employees can mark attendance.
- Employees can apply for leave according to organizational leave policies.
- Employees can access only their own restricted information.
- Managers can view information about their assigned team members.

## 6. Employee Profile Management

The system allows authorized users to maintain employee information.

Features include:
- View employee details.
- Update contact information.
- Update address and personal details.
- Update department and designation.
- Maintain employment history.

**Business Rules:**
- Employees can update only permitted personal information.
- HR and Admin can update employment-related information.
- Important changes must be recorded in the audit history.

## 7. Department and Role Assignment

Every employee must be associated with an appropriate department and designation.

Activities include:
- Assigning employees to departments.
- Assigning reporting managers.
- Updating designations.
- Changing department assignments.
- Updating system access roles.

**Business Rules:**
- Every employee must have a valid department assignment where applicable.
- Only authorized HR or Admin users can modify employment assignments.
- Only Admin can assign or change system-level user roles.
- Department changes must be recorded.

## 8. Resignation and Termination

This stage handles employees who decide to leave the organization or whose employment is terminated.

Activities include:
- Recording resignation requests.
- Recording resignation or termination dates.
- Updating employment status.
- Managing notice periods.
- Recording exit reasons.

**Business Rules:**
- Only authorized HR or Admin users can update employment status.
- Resignation and termination details must be maintained.
- Employee records must not be permanently deleted when employment ends.
- Final working dates must be recorded.

## 9. Employee Exit Process

The exit process ensures that all formalities are completed when an employee leaves the organization.

Activities include:
- Completing exit formalities.
- Updating final employment status.
- Revoking system access.
- Maintaining previous attendance and leave records.
- Maintaining payroll and employment history.

**Business Rules:**
- Former employees must not access active system features.
- Historical employee records must remain available to authorized HR and Admin users.
- Payroll and attendance history must be preserved.
- Exit details must be recorded in the audit history.

## 10. Employee Status

The system should support the following employment statuses:

| Status | Description |
|---|---|
| Pending | Employee registration or onboarding is incomplete. |
| Active | Employee is currently working. |
| On Leave | Employee is on approved leave. |
| Resigned | Employee has resigned. |
| Terminated | Employment has been terminated. |
| Inactive | Employee is no longer active in the system. |

**Note:** On Leave is a temporary employment state and does not mean the employee has left the organization.

## 11. Expected Outcome

The Employee Lifecycle Management module provides a structured way to manage employee records from joining to exit. It reduces manual HR work, maintains accurate employee information, ensures proper access control and preserves employment history.
