from app import create_app # Grabs the function from __init__.py that builds the app

app = create_app() # Runs the function to build the app and store it in a variable called app

if __name__ == '__main__': # Only run server if this file is executed directly
    app.run(debug=True) # Starts web server, debug=True means it will auto update when code is changed