*** Settings ***
Library  SeleniumLibrary
Library  ../AppLibrary.py

*** Keywords ***
Login Should Succeed
    Main Page Should Be Open

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}
