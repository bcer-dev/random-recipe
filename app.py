from creds import API_KEY
import spoonacular as sp
import flask

app = flask.Flask(__name__)
api = sp.API(API_KEY)


class Recipe:
    def __init__(self, name: str, link: str, image: str, minutes: int):
        self.name = name
        self.link = link
        self.image = image
        self.ready_minutes = minutes


def random_recipe() -> Recipe:
    raw_data = api.get_random_recipes(number=1)
    parsed_data = raw_data.json()
    recipe_data = parsed_data["recipes"][0]

    recipe = Recipe(
        recipe_data["title"],
        recipe_data["sourceUrl"],
        recipe_data["image"],
        recipe_data["readyInMinutes"]
    )

    return recipe

   
@app.get("/")
def index():
    recipe = random_recipe()
    return flask.render_template("recipe.html", recipe=recipe)