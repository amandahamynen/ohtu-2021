*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  amanda
    Set Password  amanda123
    Set Password Confirmation  amanda123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  a
    Set Password  amanda123
    Set Password Confirmation  amanda123
    Submit Credentials
    Register Should Fail With Message  Username must contain [a-z] and be atleast 3 characters long

Register With Valid Username And Too Short Password
    Set Username  amanda
    Set Password  a
    Set Password Confirmation  a
    Submit Credentials
    Register Should Fail With Message  Password must contain both characters and numbers and be atleast 8 characters long

Register With Nonmatching Password And Password Confirmation
    Set Username  amanda
    Set Password  amanda123
    Set Password Confirmation  amanda321
    Submit Credentials
    Register Should Fail With Message  Passwords do not match

Login After Successful Registration
    Set Username  amanda
    Set Password  amanda123
    Set Password Confirmation  amanda123
    Submit Credentials
    Click Link  Continue to main page
    Click Button  Logout
    Set Username  amanda
    Set Password  amanda123
    Click Button  Login
    Login Should Succeed

Login After Failed Registration
    Set Username  amanda
    Set Password  a
    Set Password Confirmation  a
    Submit Credentials
    Go To Login Page
    Set Username  amanda
    Set Password  a
    Click Button  Login
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Reset And Go To Register Page
    Reset
    Go To Register Page

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}