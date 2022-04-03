from flask import Flask, render_template, session
from env import KEY

app = Flask (__name__)
app.secret_key = KEY


if __name__ == "__main__":
  app.run(debug=True)