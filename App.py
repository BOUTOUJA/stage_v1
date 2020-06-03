from flask import Flask


from Blueprint import Blueprint


app=Flask(__name__)
app.register_blueprint(Blueprint)


if __name__ == '__main__':
    app.run(debug=True)

