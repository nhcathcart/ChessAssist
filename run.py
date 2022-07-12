from chessassist import create_app

# app instance
app = create_app()

#run webapp
if __name__ == '__main__':
    app.run(debug=True)