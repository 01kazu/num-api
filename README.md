# NUMBER CLASSIFICATION API

## Overview
The Number Classification API provides functionality to classify a given number, determining various properties such as whether it is prime, perfect, even or odd, and more. This API is useful for applications that require mathematical insights or trivia about numbers.

## Base URL
https://num-api.vercel.app/api/classify-number

## HTTP Method
GET

## Endpoint
/api/classify-number

## Request Parameters
The API accepts the following query parameter:
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
|number     | number | Yes    |The number to classify. Must be a valid integer.|


## Response Format
The response will be in JSON format with the following structure:
```
{
    "number": <number>,
    "is_prime": <boolean>,
    "is_perfect": <boolean>,
    "properties": [<string>],
    "digit_sum": <integer>,
    "fun_fact": <string>
}
```

## Response Fields
| Field | Type | Description |
|-------|------|-------------|
| number | integer | The original number that was classified.|
|is_prime |	boolean | Indicates whether the number is a prime number.|
|is_perfect | boolean |	Indicates whether the number is a perfect number.|
|properties | array | An array of strings indicating the properties of the number (e.g.,"armstrong", "even", "odd").|
|digit_sum | integer | The sum of the digits of the number.|
|fun_fact |	string | A fun fact about the number.|


## Example Request
GET https://num-api.vercel.app/api/classify-number?number=38

## Example Response
For a request to classify the number 38, the API will respond with data of this format:
```
{
    "number": 38,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["even"],
    "digit_sum": 11,
    "fun_fact": "38 is the sum of the squares of the first three primes."
}
```

## Error Handling
If the number contains non digit characters, the API will return a 400 error response. The error response will typically include the message below.

```
{"number": "alphabet", 
"error": true}

```
Common Error Codes
- 400 Bad Request: The supplied number is invalid or not in the expected format.
- 404 Not Found: The requested resource could not be found.
- 500 Internal Server Error: An unexpected error occurred on the server.




