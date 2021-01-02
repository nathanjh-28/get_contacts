from get_contacts_app import app

@app.route("/")
def home():
    return 'hello world'