from website import create_app

app = create_app()

if __name__ == '__main__':
    # run the flask application
    app.run(debug=True)