# Smart-ID-amp-Credential-Validator
 Smart ID & Credential Validator
 Problem Overview
A university is developing a Smart Registration System to approve student accounts.
Before approval, the system must strictly validate student credentials using basic string operations and conditional logic only.
This program validates:
Student ID
Email ID
Password
Referral Code

If all inputs are valid, the system prints:
APPROVED
Otherwise, it prints:
REJECTED

Validation Rules
->Student ID Rules
Format: CSE-XXX
Must start with "CSE"
4th character must be -
Last 3 characters must be digits

-> Email ID Rules
Must contain @ and .
@ must not be the first or last character
Must end with .edu

-> Password Rules
Length must be at least 8
First character must be an uppercase letter
Must contain at least one digit

-> Referral Code Rules
Format: REF##@
Must start with "REF"
Next two characters must be digits
Last character must be @

 Test Case 1
Student ID: CSE-245
Email: student@univ.edu
Password: Aman1234
Referral Code: REF45@

Output
APPROVED

 Test Case 2
Student ID: CSE245
Email: student@univ.edu
Password: aman1234
Referral Code: REF4A@

Output
REJECTED

-> Final Output Logic
If all four inputs pass validation → APPROVED
If any one input fails → REJECTED

-> Learning Outcomes
Strong understanding of string indexing and slicing
Applying conditional logic effectively
Writing validation logic without loops or advanced tools
Building real-world input validation systems
