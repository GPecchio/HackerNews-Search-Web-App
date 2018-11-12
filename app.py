from flask import Flask, render_template, request, redirect, url_for
from search import Search

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['POST', 'GET'])
def search():
    """
    All of the parameters will be strings and then the backend will handle them
    """
    if request.method == 'POST':
        # Assign each search parameter to each given argument
        terms = request.form['terms']
        sort = request.form['sort']
        tags = request.form['tags']
        pg_number = request.form['pg_number']

        # instantiate a new search
        new_search = Search()

        # Set the arguments for the search
        new_search.set_query(terms)
        new_search.set_sort_by_date(sort)
        new_search.set_tags(tags)
        new_search.set_page_number(pg_number)

        # Run the query with the given parameters
        posts = new_search.run_query()

        return render_template('search_results.html', posts=posts)
    else:
        return redirect(url_for('/'))


if __name__ == '__main__':
    app.run()
