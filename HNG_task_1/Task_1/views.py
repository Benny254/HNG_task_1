import sys
import os
import requests
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt

# Ensure the module path is correctly set
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import the task_1 module safely
try:
    from HNG_task_1 import task_1
except ModuleNotFoundError:
    task_1 = None  # Handle the missing module scenario

@csrf_exempt
def is_armstrong(number):
    digits = [int(d) for d in str(abs(number))]
    power = len(digits)
    return sum(d ** power for d in digits) == number

def get_fun_fact(number):
    url = f"http://numbersapi.com/{number}/math?json"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return response.json().get("text", "No fact available.")
    except requests.RequestException:
        return "Could not fetch fun fact."
    return "No fact available."

def get_data_type(value):
    if isinstance(value, int):
        return "integer"
    elif isinstance(value, float):
        return "float"
    elif isinstance(value, str):
        return "char"
    elif isinstance(value, bool):
        return "boolean"
    else:
        return "unknown"

class ClassifyNumberView(View):
    def get(self, request):
        number = request.GET.get("number")
        
        # Validate input
        try:
            number = int(number)
        except (TypeError, ValueError):
            return JsonResponse({"number": number, "error": True}, status=400)
        
        # Number properties
        is_prime = number > 1 and all(number % i != 0 for i in range(2, int(number ** 0.5) + 1))
        is_perfect = number > 0 and sum(i for i in range(1, number) if number % i == 0) == number
        digit_sum = sum(int(d) for d in str(abs(number)))
        is_armstrong_number = is_armstrong(number)
        properties = ["armstrong"] if is_armstrong_number else []
        properties.append("even" if number % 2 == 0 else "odd")
        
        # Fetch fun fact
        fun_fact = get_fun_fact(number)
        
        # Handle display condition for number
        display_number = number
        
        # Determine data type
        data_type = get_data_type(number)
        
        # Response
        response_data = {
            "number": display_number,
            "type": data_type,
            "is_prime": is_prime,
            "is_perfect": is_perfect,
            "properties": properties,
            "digit_sum": digit_sum,
            "fun_fact": fun_fact,
        }
        
        return JsonResponse(response_data, status=200)
