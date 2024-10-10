from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        return f"Hello, {name}! Your email is {email}."
    
    return render_template_string('''
        <!doctype html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Flask Form Example</title>
        </head>
        <body>
            <h2>Flask Form</h2>
            <form method="POST" action="/">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required><br><br>

                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required><br><br>

                <input type="submit" value="Submit">
            </form>
        </body>
        </html>
    ''')

if __name__ == "__main__":
    app.run(debug=True)
