# automation

## All the scenario defination is mentioned in popup_check.feature file inside features dir.

## Programming language used: Python
## Framework used: Behave

## Development approach: POM

### Execution: feature-->Scenario-->steps

# Popup Verification Logic:
  1. Verification of value of data-testid which is "SubscriptionPrompt-true" if popup is visible and "SubscriptionPrompt-true" if popup is invisible
  2. Verification of popup comming from bottom of the page has been done by checking the css properties applied to he popup div
   i.e. position = fixed and bottom = 0px which will conforms that the element will be visible at the bottom of the page and scrolling effect doesnot applies in the div.

# Steps to run the code:
1.  I have add virtual environment(venv) in the repo(which is not a good practice)for windows machine
2. Install virtual environment if not installed
    pip install virtualenv
2. Activate virtual environment
    goto inside Script dir of venv in cmd and run activate
3. Go back to project root dir and run "behave"

# Browser used Chrome

(FYI there could be driver version issue.Check your chrome version and replece chrome driver with your match version. Chrome driver is in driver dir.)

