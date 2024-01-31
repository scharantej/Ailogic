
# Import necessary modules
from flask import Flask, render_template, request, redirect, url_for

# Create a Flask application instance
app = Flask(__name__)

# Define the route for the root URL ('/')
@app.route('/', methods=['GET', 'POST'])
def index():
    # Handle GET requests (displaying the form)
    if request.method == 'GET':
        return render_template('index.html')

    # Handle POST requests (processing the form data)
    elif request.method == 'POST':
        # Extract the user's name from the form data
        name = request.form.get('name')

        # Generate a personalized greeting message
        greeting = f"Hello, {name}! Welcome to the Flask application."

        # Redirect to the '/greeting' route with the greeting message
        return redirect(url_for('greeting', greeting=greeting))


# Define the route for the '/greeting' URL
@app.route('/greeting')
def greeting():
    # Extract the greeting message from the URL arguments
    greeting = request.args.get('greeting')

    # Render the 'greeting.html' template with the greeting message
    return render_template('greeting.html', greeting=greeting)


# Run the application
if __name__ == '__main__':
    app.run(debug=True)


### Explanation:

- The `index.html` and `greeting.html` are assumed to be already created and located in the appropriate templates directory within your Flask project structure.

- The code starts by importing the necessary modules, including `Flask` for creating the Flask application, `render_template` for rendering HTML templates, `request` for accessing request data, `redirect` and `url_for` for handling URL routing.

- The `app = Flask(__name__)` line creates the Flask application instance.

- The `@app.route('/')` decorator defines the route for the root URL (`/`). It handles both GET and POST requests.

- In the GET method, it simply renders the `index.html` template, which should contain the form for collecting the user's name.

- In the POST method, it extracts the user's name from the submitted form data, generates a personalized greeting message, and redirects to the `/greeting` route with the greeting message as an argument.

- The `@app.route('/greeting')` decorator defines the route for the `/greeting` URL. It handles GET requests and renders the `greeting.html` template, passing the greeting message retrieved from the URL arguments.

- The `if __name__ == '__main__': app.run(debug=True)` statement is used to run the Flask application in debug mode.

- Remember to adjust the template file paths and ensure that your HTML files (`index.html` and `greeting.html`) are properly structured and placed in the templates directory.