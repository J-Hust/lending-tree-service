from flask import Blueprint
from src.review_service import fetch_all_reviews
import re


reviews = Blueprint('reviews', __name__, url_prefix='/review')


@reviews.route('/<path:link>')
def get_reviews(link):
    if is_valid_url(link):
        return fetch_all_reviews(link)
    else:
        raise ValueError('The supplied url must begin with "https://www.lendingtree.com/" and end with a number')


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

