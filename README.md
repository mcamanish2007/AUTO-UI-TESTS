# Project Name

SELENIUM UI AUTOMATION

## Overview

This project automates UI testing of the Twitch website using **Selenium WebDriver** and **Pytest**. The test simulates a user searching for a stream (e.g., "StarCraft II"), verifies the video player, and captures a screenshot for validation.

## Test Case

| **Test Case ID** | **Test Description**        | **Steps Performed**                                                                                | **Expected Result**                                     | **Status** |
| ---------------- | --------------------------- | -------------------------------------------------------------------------------------------------- | ------------------------------------------------------- | ---------- |
| TC-UI-001        | Verify Twitch search player | Navigate to Twitch → Click Browse → Search "StarCraft II" → Scroll → Click video → Wait for player | Twitch player should be visible and screenshot captured | Passed     |

## How to Run Tests

1. Install dependencies: `pip install -r requirements.txt`
2. Run the tests: `pytest -s tests/`
