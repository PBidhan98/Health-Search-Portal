from flask import Flask, render_template, url_for, redirect, jsonify
from forms import SearchForm
from elasticsearch import Elasticsearch
from spell import spell_correct

app = Flask(__name__)
es = Elasticsearch()

app.config['SECRET_KEY'] = 'c42b00f99387accd6fc4f85cb2f7cc32'


@app.route("/", methods=['GET', 'POST'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        q = form.str.data
        print(q)
        q = spell_correct(q);
        body = {
            "_source": "title",
            "query": {
                "match": {
                    "storyline": {
                        "query": q
                    }
                }
            }
        }
        if q is not None:
            results = es.search(index='movies', doc_type='_doc', body=body)
            print(results)
            if len(results['hits']['hits']) == 0:
                return render_template('home.html', results=[], show='No movie:(')
            else:
                return render_template('home.html', results=results, show='')

    return render_template('search.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
