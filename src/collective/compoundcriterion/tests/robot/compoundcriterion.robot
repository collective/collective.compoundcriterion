*** Settings ***
Documentation  collective.compoundcriterion keywords, built on the ui_plone${PLONE_MAJOR}.robot keywords.
...            Robot Framework 3.0 syntax (shared with the Plone 4.3 environment).
Resource  ui_plone${PLONE_MAJOR}.robot


*** Keywords ***
Open a manager browser with a collection and documents
    Open test browser
    Enable autologin as  Manager
    Create content  type=Document  id=matching  title=Matching special_text_to_find document
    Create content  type=Document  id=other  title=Other document
    Create content  type=Collection  id=collection  title=Collection

Edit the collection query
    [Documentation]  Adds a criterion with a value to the query of the collection and saves
    [Arguments]  ${criterion}  ${value}
    Go to  ${PLONE_URL}/collection
    Open the edit form
    Add the query criterion  ${criterion}
    Select the query value  ${value}
    Save the edit form

The collection lists
    [Arguments]  ${title}
    Element should contain  css=#content-core  ${title}

The collection does not list
    [Arguments]  ${title}
    Element should not contain  css=#content-core  ${title}
