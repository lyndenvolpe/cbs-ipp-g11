# First we imported the pieces we would need
import os
from flask import Flask, render_template, request
import giphypop
app = Flask(__name__)

# Then we set the giphypop library equal to g for ease of use
g = giphypop.Giphy()

# Next we defined a function to return a list of results when a keyword is passed through
# This function also includes an if clause in case the keyword is blank
def get_gifs(keyword):
    if keyword.lower() == "":
        results = ""
    else:
        results = g.search(keyword)
    return results

# Next we defined the pages of our web app, starting with index
@app.route("/")
def index():
    return render_template("gifs_index.html")

# Each page of the web app renders one of our HTML templates
@app.route("/about")
def about():
    return render_template("gifs_about.html")

# The results page pulls in a keyword from the search box on the index page
# The code below passes that keyword through our get_gifs function
# The results of the function are set equal to results
# Then, the HTML of the results page can arrange the resulting gifs in the template
@app.route("/results")
def results():
    keyword = request.values.get("keyword")
    results = get_gifs(keyword)
    return render_template("gifs_results.html", keyword=keyword, results=results)

# Finally, this code directs the site to the right port
port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)