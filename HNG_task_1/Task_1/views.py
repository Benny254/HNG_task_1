import requests
from django.http import JsonResponse
from django.views import View



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
        return "Could not fetch fun fact."
    return "No fact available."


class ClassifyNumberView(View):
    def get(self, request):
        """Handle GET requests to classify a number."""
        number = request.GET.get("number")

        # Validate input
        try:
            number = int(number)
        except (TypeError, ValueError):
            return JsonResponse({
                "number": "alphabet",
                "error": True
            }, status=400)

        # Determine number properties
        is_prime = number > 1 and all(number % i != 0 for i in range(2, int(number ** 0.5) + 1))
        is_perfect = number > 0 and sum(i for i in range(1, number) if number % i == 0) == number
        digit_sum = sum(int(d) for d in str(abs(number)))
        is_armstrong_number = is_armstrong(number)

        properties = []
        if is_armstrong_number:
            properties.append("armstrong")
        properties.append("even" if number % 2 == 0 else "odd")

        # Fetch fun fact
        fun_fact = get_fun_fact(number)

        # Response
        response_data = {
            "number": number,
            "is_prime": is_prime,
            "is_perfect": is_perfect,
            "properties": properties,
            "digit_sum": digit_sum,
            "fun_fact": fun_fact,
        }

        return JsonResponse(response_data, status=200)
