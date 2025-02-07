from flask import Flask, jsonify, request, abort, render_template, make_response
from flask_cors import CORS
import requests
from math import sqrt

app = Flask(__name__)
CORS(app)
app.json.sort_keys = False

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
    for i in range(2, int(sqrt(number)) + 1 ):
        if number % i == 0:
            return False
    return True

def is_perfect(number: int) -> bool:
    '''
    A number is perfect if the sum of all its divisors is equal to the number.
    e.g. the divisors of 6 are (1, 2, 3). Summing the divisors gives 6 which makes
    6 a perfect number
    '''
    if number <= 1:
        return False
    divisors = list(filter(lambda x: number % x == 0, range(1, number)))
    return sum(divisors) == number

def armstrong(number: int) -> bool:
    if number < 0:
        return False
    num_digit = len(str(number))
    total = 0
    temp = number
    while temp > 0:
        temp, digit = divmod(temp, 10) 
        total += digit ** num_digit
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
    number = abs(number)
    total = 0
    temp = number
    while temp > 0:
        temp, digit = divmod(temp, 10) 
        total += digit
    return total

def fun_fact(number: int) -> str:
    # number = str(number
    response = requests.get(f"http://numbersapi.com/{number}/math")
    return response.text

def result(number:str):
    number = int(number)
    result =  {
            "number": number,
            "is_prime": is_prime(number),
            "is_perfect": is_perfect(number),
            "properties": properties(number),
            "digit_sum": digit_sum(number),
            "fun_fact": fun_fact(number)
            }
    return jsonify(result)


@app.get("/api/classify-number")
def main_api():
    number = request.args.get('number')
    if number:
        # if number is positive number
        if number[0] != "-" and number.isdigit():
            return result(number)
        # number[1:] = number without the minus "-" sign
        if number[0] == "-" and number[1:].isdigit(): 
            return result(number)
        response = {'number': 'alphabet', 
              'error': True}
        return make_response(jsonify(response), 400)
    response = {'number': 'number is to be provided', 
              'error': True}
    return make_response(jsonify(response), 400)


@app.route("/")
def home():
    return render_template('home.html')


if __name__ == "__main__":
    main_api()
