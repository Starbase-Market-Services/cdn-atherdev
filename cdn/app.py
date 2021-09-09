from flask import Flask, render_template, redirect, request, send_file, abort
import os

app =  Flask(__name__)
folder = f"{os.getcwd()}\\cdn\\content\\"

@app.route("/cdn")
def cdn():
    arg = request.args.get('content')
    try: return send_file((folder+arg))
    except: abort(404)

app.run(port=21010)