from flask import Flask, render_template
from search import Search

app = Flask(__name__)


@app.route('/hello')
def hello_world():
    return 'Hello World!'


@app.route('/search/<terms>/<sort>/<tag>/<pg_number>')
def search(terms, sort, tag, pg_number):
    """
    All of the parameters will be strings and then the backend will handle them
    """
    new_search = Search()
    # Set what the terms for the search are
    new_search.set_query(terms)

    # Set whether to sort the results or not
    new_search.set_sort_by_date(sort)

    # Set what tags will the content be filtered by
    new_search.set_tags(tag)

    # Ser the page number for the search
    new_search.set_page_number(pg_number)

    # Run the query with the given parameters
    posts = new_search.run_query()

    return 'posts %s' % posts
    #return render_template('search_results.html', posts=posts)


if __name__ == '__main__':
    app.run()
