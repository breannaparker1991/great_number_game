from flask import Flask, render_template, session, redirect, request
from env import KEY
import random

app = Flask (__name__)
app.secret_key = KEY

@app.route('/')
def main():
  if "number" not in session:
    session['number'] = random.randint(1,100)
  if 'guess' not in session:
    session['guess'] = 0
  return render_template("index.html")

@app.route('/guess', methods=["POST"])
def guess():
  session['guess'] = int(request.form['guess'])
  return redirect('/')

@app.route('/reset')
def reset():
  session.clear()
  return redirect('/')

if __name__ == "__main__":
  app.run(debug=True)