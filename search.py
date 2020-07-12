from flask import Flask, render_template, url_for, redirect, jsonify
from forms import SearchForm
from elasticsearch import Elasticsearch


app = Flask(__name__)
es = Elasticsearch()


app.config['SECRET_KEY'] = 'c42b00f99387accd6fc4f85cb2f7cc32'


@app.route("/", methods=['GET', 'POST'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        q = form.str.data

        body = {
            "_source": "title",
            "query": {
                "match": {
                    "year": q
                }
            }
        }
        if q is not None:
            results = es.search(index='movies', doc_type='_doc', body=body)
            if len(results['hits']['hits']) ==0:
                return render_template('home.html', results=[], show='No movie:(')
            else:
                return render_template('home.html', results=results, show='')

    return render_template('search.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
