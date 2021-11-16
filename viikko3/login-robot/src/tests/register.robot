*** Settings ***
Resource  resource.robot


*** Test Cases ***
Register With Valid Username And Password
    Input New Command And Create User  oikea  oikea123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input New Command And Create User  oikea  oikea123
    Input New Command And Create User  oikea  oikea1234
    Output Should Contain  Username already exists

Register With Too Short Username And Valid Password
    Input New Command And Create User  o  oikea123
    Output Should Contain  Username must contain [a-z] and be atleast 3 characters long

Register With Valid Username And Too Short Password
    Input New Command And Create User  oikea  o
    Output Should Contain  Password must contain both characters and numbers and be atleast 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input New Command And Create User  oikea  salasana
    Output Should Contain  Password must contain both characters and numbers and be atleast 8 characters long


*** Keywords ***
Input New Command And Create User
    [Arguments]  ${username}  ${password}
    Input New Command
    Input Credentials  ${username}  ${password}