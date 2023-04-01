import requests
from flask import Flask, request, jsonify

app = Flask(__name__)


def get_wiki_response(wiki_url):
    """
    Sends a GET request to the Wikipedia API and returns the JSON response.
    Args:
        wiki_url (str): The URL to send the GET request to.
    Returns:
        dict: The JSON response from the Wikipedia API.
    """
    response = requests.get(wiki_url)
    return response.json()


@app.route('/wiki')
def wiki():
    # parse input parameters
    search_term = request.args.get('q')
    language = request.headers.get('Accept-Language', 'cs')

    # search articles with search_term in title
    response_json = get_wiki_response(
        f"https://{language}.wikipedia.org/w/api.php?action=query&list=search&srsearch=intitle:{search_term}&format=json")

    # if no articles found with search term in the title, search for articles that contain search term anywhere
    if not response_json['query']['search']:
        response_json = get_wiki_response(
            f"https://{language}.wikipedia.org/w/api.php?action=query&list=search&srwhat=text&srsearch={search_term}&format=json")

        # if still no articles found, abort with 404 error
        if not response_json['query']['search']:
            return jsonify({'error': 'no article was found'}), 404

        new_list = [{'title': dictionary['title']} for dictionary in response_json['query']['search']]
        return jsonify({'articles': new_list}), 303

    # if articles found with search term in the title, get the first article's title and extract its first paragraph
    title = response_json['query']['search'][0]['title']
    response_json = get_wiki_response(
        f"https://{language}.wikipedia.org/w/api.php?action=query&prop=extracts&exintro&explaintext&titles={title}&format=json")
    extract = response_json['query']['pages'][list(response_json['query']['pages'].keys())[0]]['extract']
    first_paragraph = extract.split('\n')[0]
    return jsonify({'first_paragraph': first_paragraph}), 200


if __name__ == '__main__':
    app.run()
