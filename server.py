from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)


@app.route("/")
def intro():
    return render_template("index.html")


# incase of other pages to display---
# eg: 127.0.0.1:5000/about.html
# eg: 127.0.0.1:5000/contact.html

# @app.route("/<string:page_name>")
# def route_to(page_name):
#     return render_template(page_name)

def write_to_txt(data):
    with open('./database.txt', "a") as fileDB:
        name = data['name']
        email = data['email']
        message = data['message']
        fileDB.write(f"{name}, {email}, {message} \n")


def write_to_csv(data):
    with open('./database.csv', "a", newline="") as csv_db:
        name = data['name']
        email = data['email']
        message = data['message']
        csv_writer = csv.writer(csv_db, delimiter=',', quotechar='"',
                                quoting=csv.QUOTE_MINIMAL)

        csv_writer.writerow([name, email, message])


@app.route("/submit_form", methods=["POST", "GET"])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            # write_to_txt(data)
            write_to_csv(data)
            return redirect("/")
        except:
            return "Something went wrong...🎃"
    return "Form NOT submitted!!"


# @app.route("/thankyou")
# def thankyou():
#     return render_template("thankyou.html")
