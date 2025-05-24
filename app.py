from flask import Flask, request, render_template_string

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def bmi_calculator():
    bmi = None
    message = ''

    if request.method == 'POST':
        try:
            weight = float(request.form['weight'])
            height = float(request.form['height']) / 100  # Convert cm to meters
            bmi = round(weight / (height ** 2), 2)

            # Determine BMI category
            if bmi < 18.5:
                message = "Underweight"
            elif 18.5 <= bmi < 24.9:
                message = "Normal weight"
            elif 25 <= bmi < 29.9:
                message = "Overweight"
            else:
                message = "Obese"

        except (ValueError, ZeroDivisionError):
            message = "Please enter valid numbers."

    return render_template_string('''
        <h2>BMI Calculator</h2>
        <form method="post">
            Weight (kg): <input type="text" name="weight"><br><br>
            Height (cm): <input type="text" name="height"><br><br>
            <input type="submit" value="Calculate BMI">
        </form>

        {% if bmi %}
            <h3>Your BMI is: {{ bmi }}</h3>
            <p>Category: {{ message }}</p>
        {% elif message %}
            <p>{{ message }}</p>
        {% endif %}
    ''', bmi=bmi, message=message)


if __name__ == '__main__':
    app.run(debug=True)
