# Leave Management – Business Rules

## 1. Introduction

The Leave Management Module allows employees to apply for leave, track their leave balances and check application status.

Managers can review and approve or reject leave requests, while HR can manage leave policies, leave balances and employee leave records.

## 2. Leave Management Features

The system should provide the following features:

- Apply for leave.
- View leave history.
- Check available leave balance.
- Approve or reject leave requests.
- Manage different leave types.
- Track pending and approved requests.
- Maintain leave records.
- Generate leave reports.

## 3. Types of Leave

The system should support the following leave types:

| Leave Type | Description |
|---|---|
| Casual Leave (CL) | Leave for personal reasons. |
| Sick Leave (SL) | Leave due to illness or health-related reasons. |
| Earned Leave (EL) | Leave accumulated based on organizational policy. |
| Unpaid Leave (LWP) | Leave taken when paid leave balance is unavailable or not applicable. |
| Maternity Leave | Leave provided according to applicable organizational policy and law. |
| Paternity Leave | Leave provided according to organizational policy. |

**Note:** Leave types and their eligibility rules should be configurable by HR or Admin.

## 4. Leave Application Rules

- Employees can submit leave applications through the system.
- Employees must select the leave type.
- Employees must provide the start date and end date.
- Employees must enter a reason for leave.
- The system must validate the requested leave dates.
- Employees can view their submitted leave requests.
- Employees cannot apply for leave for dates that violate configured leave policies.

## 5. Leave Approval Workflow

The leave approval process follows these steps:

1. Employee submits a leave request.
2. System records the request with Pending status.
3. Assigned Manager receives the request.
4. Manager reviews the application.
5. Manager approves or rejects the request.
6. System updates the leave request status.
7. Employee receives the updated status.

If additional HR approval is required, the request should be forwarded to HR according to organizational policy.

## 6. Leave Approval and Rejection Rules

- Only authorized Managers can approve or reject requests from their assigned teams.
- HR or Admin can manage leave requests according to their permissions.
- Managers must provide a rejection reason when rejecting a request.
- Employees must be notified when a decision is made.
- Approved leave must be reflected in the employee's leave balance.
- Rejected leave must not reduce the employee's leave balance.

## 7. Leave Balance Management

- Every eligible employee should have a leave balance based on organizational policy.
- The system should maintain separate balances for different paid leave types.
- Approved paid leave should reduce the available leave balance.
- Rejected and cancelled requests should not reduce the balance.
- Leave balance updates must be recorded.
- HR can adjust leave balances with proper authorization and a recorded reason.

**Formula:**

Available Leave Balance = Total Allocated Leave − Approved Leave Taken

## 8. Leave Cancellation Rules

- Employees can request cancellation of approved leave according to organizational policy.
- Pending leave requests can be withdrawn by the employee.
- Approved leave cancellation may require Manager or HR approval.
- Cancelled approved leave should be restored to the leave balance.
- All cancellation activities must be recorded.

## 9. Leave Application Status

| Status | Description |
|---|---|
| Pending | Waiting for approval. |
| Approved | Leave request has been accepted. |
| Rejected | Leave request has been declined. |
| Cancelled | Leave request has been cancelled. |
| Withdrawn | Employee has withdrawn a pending request. |

## 10. Leave Validation Rules

- Start date cannot be after the end date.
- Leave requests must have valid dates.
- Employees cannot apply for leave beyond their permitted balance for paid leave types, unless policy allows it.
- Overlapping leave applications must be detected.
- Holidays and weekly offs should be considered when calculating leave duration according to organizational policy.
- Employees must be active to submit new leave applications.

## 11. Leave Access Permissions

| Operation | Admin | HR | Manager | Employee |
|---|---|---|---|---|
| Apply for Leave | Yes | Yes | Yes | Yes |
| View All Leave Records | Yes | Yes | No | No |
| View Team Leave Requests | Yes | Yes | Yes | No |
| View Own Leave Records | Yes | Yes | Yes | Yes |
| Approve Leave | Yes | Yes | Assigned Team | No |
| Reject Leave | Yes | Yes | Assigned Team | No |
| Manage Leave Balance | Yes | Yes | No | No |
| Configure Leave Types | Yes | Yes | No | No |
| Cancel Own Request | Yes | Yes | Yes | Yes |

## 12. Leave Reports

The system should generate leave reports containing:

- Employee ID and Name.
- Leave Type.
- Leave Start Date.
- Leave End Date.
- Total Leave Days.
- Application Date.
- Approval Status.
- Approver Details.
- Available Leave Balance.

Reports should be accessible only to authorized users.

## 13. Notifications

The system should notify users about:

- Successful leave application submission.
- Leave approval.
- Leave rejection.
- Leave cancellation.
- Pending approval requests.

## 14. Security and Audit Rules

- Employees can view only their own leave records.
- Managers can view leave requests of assigned team members.
- Only authorized users can approve or reject leave.
- Leave balance changes must be recorded.
- Every approval, rejection and cancellation must be stored in the audit history.
- Unauthorized access must be restricted.

## 15. Expected Outcome

The Leave Management Module simplifies the leave application and approval process. It maintains accurate leave balances, reduces manual work, improves transparency and provides an organized leave management process for employees, managers and HR.
