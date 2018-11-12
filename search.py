import requests


class Post:
    def __init__(self, title, author, url, points, text):
        self.title = title
        self.author = author
        self.url = url
        self.points = points
        self.text = text

    def print_post(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("URL:", self.url)
        print("Points:", self.points)
        print("Text:", self.text)


class Search:
    def __init__(self):
        self.query = ''
        self.sort_by_date = False
        self.tags = ''
        self.page_number = 0

    def set_query(self, terms):
        """
        Given the terms for the search, set them equal to query
        """
        self.query = str(terms)

    def set_sort_by_date(self, sort):
        """
        Given a string representing 'y' or 'n' as the user's response to having the search sorted by date or not,
        set the sort by date value
        """
        if sort == 'y':
            self.sort_by_date = True
        else:
            self.sort_by_date = False

    def set_tags(self, tag):
        """
        Given a string representing the tag to look for,
        set it as the search tag
        """
        available_tags = ['story', 'comment', 'poll', 'pollopt', 'show_hn', 'ask_hn', 'front_page']
        for word in available_tags:
            if tag == word:
                self.tags = tag
                print("Tag", tag, "has been set")

    def set_page_number(self, pg_number):
        """
        Set the page number for the search
        """
        self.page_number = pg_number

    def run_query(self):
        """
        Given the previous answers and the query run the query using the Algolia API for Hacker News
        """
        if self.sort_by_date:
            request = requests.get('http://hn.algolia.com/api/v1/search_by_date?query=' + str(self.query)
                                   + '&tags=' + str(self.tags) + '&page=' + str(self.page_number))
        else:
            request = requests.get('http://hn.algolia.com/api/v1/search?query=' + str(self.query)
                                   + '&tags=' + str(self.tags) + '&page=' + str(self.page_number))
        request_json = request.json()

        posts = request_json["hits"]
        '''
        for post in posts:
            new_post = Post(post["title"], post["author"], post["url"], post["points"], post["story_text"])
            print(new_post.print_post())
            print("")
        '''
        return posts


if __name__ == "__main__":
    new_search = Search()
    # Set what the terms for the search are
    terms = input("What do you want to search:")
    new_search.set_query(terms)

    # Set whether to sort the results or not
    sort = input("Do you want to sort the results? (y/n)")
    new_search.set_sort_by_date(sort)

    # Set what tags will the content be filtered by
    print("Do you want to search a specific content by tag?")
    tag = input("(tags available: story, comment, poll, pollopt, show_hn, ask_hn, front_page)")
    new_search.set_tags(tag)

    # Ser the page number for the search
    pg_number = int(input("Which page number would you like to see first?"))
    new_search.set_page_number(pg_number)

    # Run the query with the given parameters
    print(new_search.run_query())
