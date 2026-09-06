# Student Management System - QA Testing

## 1. Introduction

This document records the Quality Assurance (QA) testing performed for the Student Management System.

The purpose of testing is to verify that the implemented modules work correctly and that the integrated system performs as expected.

The following modules were tested:

* Login Module
* Dashboard Module
* Reports Module

---

## 2. Testing Objectives

The objectives of QA testing are:

1. To verify that the Login module accepts valid login credentials.
2. To verify that invalid login credentials are handled correctly.
3. To verify that the Dashboard module loads and displays the required information.
4. To verify that the Reports module displays student information correctly.
5. To verify that the different modules work correctly after integration.
6. To document the testing process and results.

---

## 3. Test Environment

**Project:** Student Management System

**Repository:** Student_Managmnt_Systm

**Version Control:** Git and GitHub

**Testing Type:** Functional Testing and Integration Testing

**Tester:** QA Team Member

---

## 4. Login Module Testing

| Test ID  | Test Case                         | Expected Result                            | Actual Result                 | Status |
| -------- | --------------------------------- | ------------------------------------------ | ----------------------------- | ------ |
| LOGIN-01 | Enter valid username and password | User should be logged in successfully      | User logged in successfully   | PASS   |
| LOGIN-02 | Enter invalid username            | Login should be rejected                   | Login rejected                | PASS   |
| LOGIN-03 | Enter invalid password            | Login should be rejected                   | Login rejected                | PASS   |
| LOGIN-04 | Submit empty login fields         | System should handle empty input correctly | Empty input handled correctly | PASS   |

### Login Testing Result

The Login module was tested using valid and invalid input combinations. The module performed as expected for all tested cases.

---

## 5. Dashboard Module Testing

| Test ID | Test Case                          | Expected Result                         | Actual Result                 | Status |
| ------- | ---------------------------------- | --------------------------------------- | ----------------------------- | ------ |
| DASH-01 | Open Dashboard                     | Dashboard should load successfully      | Dashboard loaded successfully | PASS   |
| DASH-02 | View student information           | Student information should be displayed | Student information displayed | PASS   |
| DASH-03 | Navigate through Dashboard options | Available options should work correctly | Options worked correctly      | PASS   |

### Dashboard Testing Result

The Dashboard module was tested for loading, displaying student information, and navigating through its available options. All tested functions worked as expected.

---

## 6. Reports Module Testing

| Test ID   | Test Case                        | Expected Result                                | Actual Result                      | Status |
| --------- | -------------------------------- | ---------------------------------------------- | ---------------------------------- | ------ |
| REPORT-01 | Open Reports module              | Reports module should open successfully        | Reports module opened successfully | PASS   |
| REPORT-02 | Display student report           | Student report should be displayed             | Student report displayed           | PASS   |
| REPORT-03 | Display multiple student records | Multiple records should be displayed correctly | Records displayed correctly        | PASS   |

### Reports Testing Result

The Reports module was tested for opening the module and displaying student records. The tested functionality performed as expected.

---

## 7. Integration Testing

Integration testing was performed after the individual modules were developed.

| Test ID | Integration Test          | Expected Result                                                    | Actual Result                           | Status |
| ------- | ------------------------- | ------------------------------------------------------------------ | --------------------------------------- | ------ |
| INT-01  | Login → Dashboard         | Successful login should allow access to Dashboard                  | Dashboard accessed successfully         | PASS   |
| INT-02  | Dashboard → Reports       | Reports option should open the Reports module                      | Reports module opened successfully      | PASS   |
| INT-03  | Complete application flow | Application should operate correctly through the available modules | Application flow completed successfully | PASS   |

---

## 8. Git and QA Workflow

The QA work was maintained separately using a dedicated branch.

```bash
git checkout main
git pull origin main
git checkout -b qa/testing
```

After completing the QA documentation:

```bash
git add QA/TESTING.md QA/test_results.txt
git commit -m "Add QA testing documentation and results"
git push -u origin qa/testing
```

The QA branch can then be reviewed and merged into the main branch by the team lead.

---

## 9. Overall Testing Result

All planned functional and integration test cases were completed successfully.

The Login, Dashboard, and Reports modules were verified, and the integrated Student Management System performed as expected during testing.

**Overall Status: PASS**

---

## 10. Conclusion

QA testing verified the functionality of the Student Management System modules and their integration. The testing results were documented and committed using Git as part of the team's collaborative version-control workflow.
