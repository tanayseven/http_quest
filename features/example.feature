Feature: Show off behave

  Scenario: Run a simple test
    Given we have behave installed
      When we implement 5 tests
      When we start selenium webbrowser
      Then behave will test them for us!
