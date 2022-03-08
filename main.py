import random

from flask import Flask, redirect, render_template

app = Flask(__name__)


@app.route('/')
def friendmovie():
    return render_template('friendmovie.html')


@app.route('/friend')
def random_friend():
    return redirect(
        random.choice([
            'https://steamcommunity.com/profiles/76561198866668208',
            'https://steamcommunity.com/profiles/76561198169341140',
            'https://steamcommunity.com/profiles/76561198132942054',
            'https://steamcommunity.com/profiles/76561198850161732',
            'https://steamcommunity.com/profiles/76561198046082680',
            'https://steamcommunity.com/profiles/76561198133234284'
        ])
    )


@app.route('/tgu')
def tgu():
    return redirect('https://steamcommunity.com/profiles/76561198866668208')


@app.route('/peptic')
def peptic():
    return redirect('https://steamcommunity.com/profiles/76561198169341140')


@app.route('/yuhnwood')
def yuhn():
    return redirect('https://steamcommunity.com/profiles/76561198132942054')


@app.route('/yuhn')
def yuhn2():
    return redirect('https://steamcommunity.com/profiles/76561198132942054')


@app.route('/syren')
def syren():
    return redirect('https://steamcommunity.com/profiles/76561198850161732')


@app.route('/sirty')
def sirty():
    return redirect('https://steamcommunity.com/profiles/76561198046082680')


@app.route('/moo')
def moo():
    return redirect('https://steamcommunity.com/profiles/76561198046082680')


@app.route('/fiona')
def fiona():
    return redirect('http://steamcommunity.com/profiles/76561198133234284')

@app.route('/lucid')
def lucid():
    return redirect('https://steamcommunity.com/profiles/76561198043754845')

@app.route('/klown')
@app.route('/acapella')
def klown():
    return redirect('https://youtu.be/UGKwqPAKdkc')


if __name__ == '__main__':
    app.run()
