import re
from flask import Blueprint, Response
from src.review_service import fetch_all_reviews



reviews = Blueprint('reviews', __name__, url_prefix='/review')


@reviews.route('/<path:link>')
def get_reviews(link):
    if is_valid_url(link):
        reviews_json = fetch_all_reviews(link)
        resp = Response(reviews_json, status=200, mimetype='application/json')
        return resp

    resp = Response('The supplied url must begin with "https://www.lendingtree.com/" and end with a number',
                    status=400,
                    mimetype='text/plain')
    return resp


def is_valid_url(url):
    """
    Returns True if the supplied url begins with 'https://www.lendingtree.com/' and ends with a number.

    Parameters:
    url (str): the lender's url

    Returns:
    bool: the validity of the supplied url

    """
    matches_found = re.match(r'https://www\.lendingtree\.com.+/[0-9]+$', url)

    if matches_found is not None:
        return True
    return False
