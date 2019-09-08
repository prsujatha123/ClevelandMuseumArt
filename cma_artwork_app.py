from flask import redirect,render_template,Flask,make_response,jsonify,request
import artwork_api
app = Flask(__name__)
@app.route('/')
def display():
    response = make_response(render_template("museum.html"))
    return response


# Get the all work details and also get get the data based on search criteria
@app.route("/content/")
@app.route("/content/<search>")

def get_content(search=None):
    item = artwork_api.get_All_Arts_Based_On_Accession_Number(search)
    data = { "data": item }

    return jsonify(data)


# create a Art Details page
@app.route("/art/<accession_number>")
def get_ArtDetailsPage(accession_number):

    response = make_response(render_template("art_display.html",accession_number=accession_number))
    return response


#Get the art details based on accession_number
@app.route("/artDetails/<accession_number>")
def get_get_ArtDetails(accession_number):
    item = artwork_api.get_artStyles_Details(accession_number)
    data = { "data": item }
    return jsonify(data)

if __name__ == '__main__':
    app.run()