from flask import Flask
import random

app = Flask(__name__)


@app.route('/')
def check_leap_year():
    year = random.randint(1, 2021)
    is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    if is_leap:
        leap_status = f"{year} is a leap year."
    else:
        leap_status = f"{year} is not a leap year."

    return f'''
        <h1>Random Year: {year}</h1>
        <p>{leap_status}</p>
    '''


if __name__ == '__main__':
    app.run(debug=True)
