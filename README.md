# Wiki_API instructions

Start the API server by running the script. This can be done by navigating to the directory containing the script in your terminal and running the command python <filename>.py, where <filename> is the name of the Python script file.

Once the server is running, you can access the API at http://localhost:5000/wiki.

To search for a Wikipedia article, append the search query to the end of the URL as a query parameter called q. For example, to search for articles about cats, the URL would be http://localhost:5000/wiki?q=cats.

The API supports the Accept-Language header to specify the language of the Wikipedia articles returned. By default, the language is set to Czech (cs). To specify a different language, include the Accept-Language header in the request with the appropriate language code. For example, to search for articles in English, include the header Accept-Language: en.

The API will return a JSON response with either the first paragraph of the first article found with the search term in its title, or a list of article titles if no article was found with the search term in its title but articles were found containing the search term anywhere in their text. If no article is found, the API will return a 404 error.

Use a tool such as curl or a web browser to make requests to the API. For example, to search for articles about rum in Czech, run the following command in your terminal: curl -H "Accept-Language: cs" http://localhost:5000/wiki?q=rum. The response will be a JSON object containing the first paragraph of the first article about Rum found in Czech.
