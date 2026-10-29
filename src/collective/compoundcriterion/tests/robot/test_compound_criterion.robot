*** Settings ***
Documentation  "Compound criterion" field of the Collection query widget, with the testing-compound-adapter
...            filter of testing.zcml (title contains special_text_to_find).
...            Version-independent: Plone selectors are in ui_plone*.robot.
Resource  compoundcriterion.robot
Test Setup  Open a manager browser with a collection and documents
Test Teardown  Close all browsers


*** Test Cases ***
The collection lists only the documents of the compound criterion
    Edit the collection query  Compound criterion  testing-compound-adapter
    The status message contains  Changes saved
    The collection lists  Matching special_text_to_find document
    The collection does not list  Other document

The edit form shows the saved compound criterion
    Edit the collection query  Compound criterion  testing-compound-adapter
    Open the edit form
    The query criterion is shown  Compound criterion  testing-compound-adapter
