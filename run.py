from app import create_app

app = create_app()

if __name__ == '__main__':  # only run server if this file is executed directly
    app.run(debug=True)
