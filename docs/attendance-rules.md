# Attendance Management – Business Rules

## 1. Introduction

The Attendance Management Module is responsible for recording, monitoring and managing employee attendance.

It allows employees to mark their daily check-in and check-out times while HR and Managers can monitor attendance records and working hours.

## 2. Attendance Features

The system should provide the following features:

- Daily employee check-in.
- Daily employee check-out.
- Automatic recording of attendance date and time.
- Calculation of total working hours.
- Attendance history.
- Late arrival tracking.
- Early departure tracking.
- Attendance reports.
- HR attendance management.

## 3. Check-In Rules

- Employees can mark their check-in when they start working.
- The system must automatically record the check-in date and time.
- An employee can have only one valid check-in for a working day.
- Employees must be authenticated before marking attendance.
- Duplicate check-in attempts must be prevented.

## 4. Check-Out Rules

- Employees can mark their check-out when they finish working.
- The system must automatically record the check-out date and time.
- Check-out is allowed only after a valid check-in.
- An employee cannot check out more than once for the same attendance session.
- The system calculates working hours using check-in and check-out timestamps.

## 5. Working Hours Calculation

The system calculates total working hours based on check-in and check-out times.

**Formula:**

Total Working Hours = Check-out Time − Check-in Time − Break Duration

Example:

- Check-in: 9:30 AM
- Check-out: 6:30 PM
- Break Duration: 1 Hour
- Total Working Hours: 8 Hours

The system should store the calculated working hours for attendance reporting.

## 6. Late Arrival Rules

- The organization should define standard working hours.
- Employees checking in after the permitted start time may be marked late.
- The system should record late arrival details.
- HR can view late arrival reports.
- Managers can monitor late arrivals within their assigned teams.

**Note:** The grace period and official working hours must be configurable by HR or Admin.

## 7. Early Departure Rules

- Employees leaving before the scheduled working time may be marked as early departure.
- The system should record the actual check-out time.
- HR and Managers can monitor early departures.
- Approved early departures should be distinguishable from unapproved departures.

## 8. Attendance Status

The system should support the following attendance statuses:

| Status | Description |
|---|---|
| Present | Employee has completed the required attendance process. |
| Absent | Employee has not attended work and has no approved leave. |
| Half Day | Employee has completed only part of the required working hours. |
| Late | Employee has checked in after the permitted start time. |
| On Leave | Employee has approved leave. |
| Holiday | Organization has declared a holiday. |
| Weekly Off | Scheduled non-working day. |
| Work From Home | Employee is working remotely with approval. |

**Note:** Late can be maintained as an attendance flag alongside Present instead of a separate mutually exclusive status.

## 9. Attendance Modification Rules

- Employees cannot directly modify submitted attendance records.
- HR or authorized Admin users can correct attendance records.
- Attendance corrections must include a reason.
- All modifications must be recorded in the audit history.
- Managers may request corrections but cannot modify records unless authorized.

## 10. Attendance Access Permissions

| Operation | Admin | HR | Manager | Employee |
|---|---|---|---|---|
| Mark Check-In | Yes | Yes | Yes | Yes |
| Mark Check-Out | Yes | Yes | Yes | Yes |
| View All Attendance | Yes | Yes | No | No |
| View Team Attendance | Yes | Yes | Yes | No |
| View Own Attendance | Yes | Yes | Yes | Yes |
| Modify Attendance | Yes | Yes | No | No |
| Generate Reports | Yes | Yes | Team Only | No |

## 11. Attendance Reports

The system should generate attendance reports containing:

- Employee ID and Name.
- Attendance Date.
- Check-In Time.
- Check-Out Time.
- Total Working Hours.
- Attendance Status.
- Late Arrival Details.
- Early Departure Details.

Reports should be accessible according to user roles.

## 12. Validation and Security Rules

- Employees must be authenticated before accessing attendance features.
- Duplicate attendance entries must be prevented.
- Check-out time cannot be earlier than check-in time.
- Attendance records must be associated with the correct employee.
- Employees must not access other employees' attendance records.
- All timestamps should be stored consistently, preferably in UTC, and displayed in the organization's configured timezone.
- Attendance modifications must be logged.

## 13. Expected Outcome

The Attendance Management Module provides an accurate and transparent way to track employee working hours, attendance status, late arrivals and early departures. It reduces manual attendance management and helps HR and Managers monitor employee attendance efficiently.
