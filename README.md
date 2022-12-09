# selenium_demo_framework
Test cases for the nopcommerce website. 
1.login test case and home page title test case.
2. adding the customer is second testcase. 

Implemented the hybrid framework.

Followed some steps to create the framework. 

Step -1
Creating a project and installing required plugins/packages

Selenium- selenium libraries
Pytest- python with unit test framework
Pytest-html — to pytest html reports
pytest-xdist - run tests parallel

Step.2-Creating folder structure

Project Name-
Page Objects(Package)
Test cases(Package)
Utilities- (Package)
Test data (Folder)- If we have test data in excel files
Configurations(Folder)
Logs (Folder)
Screenshots (Folder)
Reports (Folder)

Step.3- Automating login test cases
Creating a login test page objects class under “page object”

Create login test under “test cases”

Create conftest.py file  under “test cases”(common things into this file). creating a fixture,which can be used in all test cases like launching browser. 

Step.4-
 Capture screenshot as failures
Updating login test with screenshot under test cases

Step.5-
Create ini file to read common values
Adding config.ini file in the configuration files
Create a “readproperties.py” utility file under utilities package to read common data. 

Step.6- 
Adding logs to test cases
Adding customlogger.py file  under utilities package
Add logs to login test case

Step.7- 
Run tests on desired browser and parallel

Step.8- 
Generate pytest HTML reports

Step.9-
Adding new test cases
email id is unique. Generate random test data. 
2 types - static and dynamic data
static - prepare before and create excel file and hardcode it. 
dynamic - generate different mailid for different customer. 

Step.10- 
Grouping tests
Adding markers to every test method
(customized markers - add in pytest.ini)
             @pytest.mark.sanity -
             @pytest.mark.regression
Adding marker entries in pytest.ini file
