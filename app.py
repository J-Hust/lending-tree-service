from flask import Flask, request
import src.review_service
import re


app = Flask(__name__)

@app.route('/')
def my_index():
    print('some index stuff')
    src.review_service.hi()

    return 'this is the index'


@app.route('/testing', methods=['GET'])
def sure_kid():

    lender_url = 'lendingtree.com/reviews/personal/cashnetusa/81638970'

    if is_invalid_url(lender_url):
        return 'bad url, homie'
    lender_id = grab_id_from_url(lender_url)
    final_stuff = src.review_service.get_everything(lender_id)
    return final_stuff

@app.route('/reviews', methods=['POST'])
def fetch_reviews():

    string_thing = str(request.data)
    print('you sent {}'.format(str(request.data)))
    if is_invalid_url(string_thing):
        return 'bad url, homie'
    lender_id = grab_id_from_url(string_thing)
    src.review_service.get_everything(lender_id)


def is_invalid_url(url):
    my_regex = re.compile(r'lendingtree')
    
    if my_regex.match(url) is None:
        return True

def grab_id_from_url(url):
    return url[url.rfind('/')+1::]





if __name__ == '__main__':
    app.run()