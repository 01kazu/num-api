from flask import Flask, request, abort, render_template
from flask_cors import CORS
import json
import requests
from math import sqrt

app = Flask(__name__)
CORS(app)

'''
functions to create
1. is_prime(number) - returns true or false
2. is_perfect(number) - returns true or false
3. properties(number) - returns a list of the following existing properties: ['armstrong', 'odd',
                                                                             even']
4. digit_sum(number) - sum of each digit.
5. fun_fact(number) - use http://numbersapi.com

6. main_api() - if alphacharacters are in the characters, return a 400 Bad Request
'''

def is_prime(number: int) -> bool:
    '''
    Checks if then number is a prime number
    '''
    if number <= 1:
        return False
    for i in range(2, int(sqrt(number))):
        if number % i == 0:
            return False
    return True

def is_perfect(number: int) -> bool:
    '''
    A number is perfect if the sum of all its divisors is equal to the number.
    e.g. the divisors of 6 are (1, 2, 3). Summing the divisors gives 6 which makes
    6 a perfect number
    '''
    divisors = list(filter(lambda x: number % x == 0, range(1, number)))
    return sum(divisors) == number

def armstrong(number: int) -> bool:
    total = 0
    temp = number
    while temp > 0:
        temp, digit = divmod(temp, 10) 
        total += digit ** 3
    return number == total

def even(number: int) -> bool:
    if number % 2 == 0:
        return True

def odd(number: int) -> bool:
    if number % 2 == 1:
        return True

def properties(number: int) -> list:
    p = []
    if armstrong(number):
        p.append("armstrong")
    if even(number):
        p.append("even")
    if odd(number):
        p.append("odd")
    return p

def digit_sum(number: int) -> int:
    total = 0
    temp = number
    while temp > 0:
        temp, digit = divmod(temp, 10) 
        total += digit
    return total

def fun_fact(number: int) -> str:
    # number = str(number
    response = requests.get(f"http://numbersapi.com/{number}")
    return response.text

@app.errorhandler(400)
def not_found_error(error):
    error = {
        "number": "alphabet",
        "error": True
    }
    return  json.dumps(error), 400

@app.get("/api/classify-number")
def main_api():
    number = request.args.get('number')
    if number.isdigit():
        number = int(number)
        result =  {
            "number": number,
            "is_prime": is_prime(number),
            "is_perfect": is_perfect(number),
            "properties": properties(number),
            "digit_sum": digit_sum(number),
            "fun_fact": fun_fact(number)
            }
        return json.dumps(result, sort_keys=False)
    return abort(400)

@app.route("/")
def home():
    return render_template('home.html')


if __name__ == "__main__":
    main_api()
