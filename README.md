Number Classification API

Overview

The Number Classification API provides mathematical properties of a given number, including whether it is prime, perfect, or an Armstrong number. It also fetches a fun fact about the number from an external API.

Resources

Fun fact API: Numbers API

Parity in Mathematics

Technology Stack

You can implement this API using any of the following:

C#

PHP

Python

Go

Java

JavaScript/TypeScript

Deployment Requirements

Must be deployed to a publicly accessible endpoint

CORS must be handled

JSON response format is required

Version Control

Code must be hosted on GitHub

Repository must be public

Must include this README.md

API Specification

Endpoint:

GET <your-domain.com>/api/classify-number?number=371

Response Format

Success (200 OK):

{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}

Error (400 Bad Request):

{
    "number": "alphabet",
    "error": true
}

Acceptance Criteria

Functionality

Accepts GET requests with a number parameter

Returns JSON in the specified format

Accepts only valid integers

Provides appropriate HTTP status codes

Code Quality

Well-structured code

Basic error handling and input validation

No hardcoded values

Documentation

This README must be complete and well-structured

Deployment

API must be publicly accessible and stable

Response time should be under 500ms

Submission Guidelines

Host the API on a publicly accessible platform.

Verify that all requirements and criteria are met.

Thoroughly test the API.

Submit the task via the designated submission form.

Announce your submission in the stage-one-backend channel using /task.

Deadline

📅 Submission Deadline: February 6, 2025, 11:59 PM WAT (GMT +1)

Late submissions will not be accepted.

Additional Notes

Use the math type from the Numbers API to fetch the fun fact.

Scoring: 10 marks. A passing score is required to proceed to the next stage.

Properties Field Combinations:

["armstrong", "odd"] → Armstrong number & Odd

["armstrong", "even"] → Armstrong number & Even

["odd"] → Not Armstrong, but Odd

["even"] → Not Armstrong, but Even
