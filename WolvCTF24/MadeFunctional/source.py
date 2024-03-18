
import os
from pathlib import Path
import re
import subprocess
import tempfile

from flask import Flask, request, send_file

app = Flask(__name__)
flag = open('flag.txt').read()


def write_flag(path):
    with open(path / 'flag.txt', 'w') as f:
        f.write(flag)


def generate_makefile(name, content, path):
    with open(path / 'Makefile', 'w') as f:
        f.write(f"""
SHELL := env PATH= /bin/bash
.PHONY: {name}
{name}: flag.txt
\t{content}
""")


@app.route('/', methods=['GET'])
def index():
    return send_file('index.html')


@app.route('/src/', methods=['GET'])
def src():
    return send_file(__file__)


# made functional
@app.route('/make', methods=['POST'])
def make():
    target_name = request.form.get('name')
    code = request.form.get('code')

    print(code)
    if not re.fullmatch(r'[A-Za-z0-9]+', target_name):
        return 'no'
    if '\n' in code:
        return 'no'
    if re.search(r'/', code):
        return 'no'

    with tempfile.TemporaryDirectory() as dir:
        run_dir = Path(dir)
        write_flag(run_dir)
        generate_makefile(target_name, code, run_dir)
        sp = subprocess.run(['make'], capture_output=True, cwd=run_dir)
        return f"""
<h1>stdout:</h1>
{sp.stdout}
<h1>stderr:</h1>
{sp.stderr}
    """


app.run('localhost', 8000)
