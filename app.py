from flask import Flask, request, render_template
from stories import Story

app = Flask(__name__)

story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

@app.route('/')
def home_page():
    prompts = list(story.prompts)
    
    return render_template('index.html', prompts=prompts)

@app.route('/story')
def story_page():
    text = story.generate(request.args)
    return render_template('/story.html', text=text)