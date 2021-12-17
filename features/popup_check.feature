Feature: Popup check
  Scenario: Launch website and validate popup behaviour
    Given user launches "https://www.afr.com/policy/foreign-affairs/capability-edge-and-keeping-south-china-sea-open-crucial--christopher-pyne-20180924-h15rq9"
    Then Verify that the subscription prompt poupped up
    And User scrolls downs to the end of the page
    And User waits for 10 seconds
    Then Verify that pop up disappears
