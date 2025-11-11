from django.shortcuts import render
from .models import Calculation
from datetime import datetime
from functools import reduce
import operator

def calculate_arbitrage(request):
    result = None
    message = None
    style = None
    is_arbitrage = False
    num_coeffs = 2
    x_values = []

    if request.method == "POST":
        try:
            # Number of coefficients
            num_coeffs = int(request.POST.get("num_coeffs", 2))

            # Get coefficients
            for i in range(1, num_coeffs + 1):
                val = request.POST.get(f"x{i}")
                if val:
                    val_float = float(val)
                    if val_float < 1.01:
                        message = f"⚠️ Coefficient {i} must be at least 1.01!"
                        style = "warning"
                        result = None
                        x_values = []
                        break
                    x_values.append(val_float)

            # Perform calculation if at least 2 coefficients
            if len(x_values) >= 2 and not message:

                n = len(x_values)

                # Dynamic formula
                if n == 2:
                    x, y = x_values
                    res = (1 - (x*y)/(x+y)) * 100
                elif n == 3:
                    x, y, z = x_values
                    res = (1 - (x*y*z)/(x*z + x*y + y*z)) * 100
                elif n == 4:
                    a, b, c, d = x_values
                    res = (1 - (a*b*c*d)/(a*b*c + a*b*d + a*c*d + b*c*d)) * 100
                else:
                    # General formula for 5-8 coefficients
                    numerator = reduce(operator.mul, x_values)
                    denominator = sum(
                        reduce(operator.mul, [x_values[j] for j in range(n) if j != i])
                        for i in range(n)
                    )
                    res = (1 - numerator / denominator) * 100

                result = round(res, 2)

                # Determine message and style
                if res < 0:
                    message = f"🔥 Arbitrage Found: {result}%"
                    style = "danger"
                    is_arbitrage = True
                elif res == 0:
                    message = f"Zero Arbitrage: {result}%"
                    style = "secondary"
                else:
                    message = f"✅ No Arbitrage: {result}%"
                    style = "success"

                # Save to database
                Calculation.objects.create(
                    x_value=", ".join(map(str, x_values)),
                    result=result,
                    is_arbitrage=is_arbitrage,
                    created_at=datetime.now()
                )

            elif len(x_values) < 2 and not message:
                message = "⚠️ Please enter at least 2 coefficients!"
                style = "warning"

        except (TypeError, ValueError):
            message = "⚠️ Please enter valid numbers!"
            style = "warning"

    # Last 10 calculations
    history = Calculation.objects.all().order_by("-created_at")[:10]

    context = {
        "result": result,
        "message": message,
        "style": style,
        "x_values": x_values,
        "history": history,
        "num_coeffs": num_coeffs,
    }

    return render(request, "calculator/index.html", context)