from flask import Flask, render_template, request
from requests_html import HTMLSession
import helpers

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def scraper():
    if request.method == 'POST':
        site = request.form['myUrl']
        session = HTMLSession()
        abs_urls = session.get(site).html.absolute_links
        helpers.process_data(abs_urls)
        print(abs_urls)
        return render_template('index.html', links=abs_urls)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
