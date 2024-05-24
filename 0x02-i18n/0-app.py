#!/usr/bin/env python3
"""A basic app"""


from flask import Flask, render_template

app = Flask(__name__)
app.url_map.stric_slashes = False

@app.route('/')
def index():
  """The home/index page"""
  return render_template("0-index.html",)

if __name__ == "__main__":
    app.run(hdebug=True)
