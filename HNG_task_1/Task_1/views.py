import requests
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
import logging

# Setup logging
logger = logging.getLogger(__name__)

# Try importing task_1 module safely
try:
    from HNG_task_1 import task_1
except ModuleNotFoundError:
    logger.warning("Module 'task_1' not found. Ensure it is installed and in the correct directory.")
    task_1 = None  # Handle the missing module scenario


def is_armstrong(number):
    """Check if a number is an Armstrong number."""
    digits = [int(d) for d in str(abs(number))]
    power = len(digits)
    return sum(d ** power for d in digits) == number


def get_fun_fact(number):
    """Fetch a fun fact about a number from NumbersAPI."""
    url = f"http://numbersapi.com/{number}/math?json"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return response.json().get("text", "No fact available.")
    except requests.RequestException:
        logger.error("Error fetching fun fact from NumbersAPI.")
        return "Could not fetch fun fact."
    return "No fact available."


def get_data_type(value):
    """Determine the data type of the number."""
    if isinstance(value, int):
        return "integer"
    elif isinstance(value, float):
        return "float"
    elif isinstance(value, str):
        return "char"
    elif isinstance(value, bool):
        return "boolean"
    return "unknown"


@csrf_exempt
class ClassifyNumberView(View):
    def get(self, request):
        """Handle GET requests to classify a number."""
        number = request.GET.get("number")

        # Validate input
        try:
            number = int(number)
        except (TypeError, ValueError):
            return JsonResponse({"error": "Invalid number provided."}, status=400)

        # Determine number properties
        is_prime = number > 1 and all(number % i != 0 for i in range(2, int(number ** 0.5) + 1))
        is_perfect = number > 0 and sum(i for i in range(1, number) if number % i == 0) == number
        digit_sum = sum(int(d) for d in str(abs(number)))
        is_armstrong_number = is_armstrong(number)

        properties = ["armstrong"] if is_armstrong_number else []
        properties.append("even" if number % 2 == 0 else "odd")

        # Fetch fun fact
        fun_fact = get_fun_fact(number)

        # Response
        response_data = {
            "number": number,
            "type": get_data_type(number),
            "is_prime": is_prime,
            "is_perfect": is_perfect,
            "properties": properties,
            "digit_sum": digit_sum,
            "fun_fact": fun_fact,
        }

        return JsonResponse(response_data, status=200)
