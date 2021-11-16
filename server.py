from flask import Flask  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

# 1 localhost:5000/ - have it say "Hello World!"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

# 2 localhost:5000/dojo - have it say "Dojo!"
@app.route('/dojo')
def dojo():
    return 'Dojo!'


# 3 localhost:5000/say/flask - have it say "Hi Flask!"
#   localhost:5000/say/michael - have it say "Hi Michael!"
#   localhost:5000/say/john - have it say "Hi John!"
@app.route('/say/<string:word>')
def say(word):
    return f"Hi {word}!"


# 4 localhost:5000/repeat/35/hello - have it say "hello" 35 times
#   localhost:5000/repeat/80/bye - have it say "bye" 80 times
#   localhost:5000/repeat/99/dogs - have it say "dogs" 99 times
@app.route('/repeat/<int:num>/<string:word>')
def repeat(num, word):
    return word * num

# Return "Sorry! No response. Try again." if user types any route other than the ones specified
@app.errorhandler(404)
def page_not_found(error):
    return 'Sorry! No response. Try again.'


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

