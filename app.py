from flask import Flask, render_template, request
from models import db, connect_db, Users

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
# db.create_all()
# db.create_all()
with app.app_context():
    db.create_all()

@app.route('/')
def list_users():
    users = Users.query.all()
    return render_template('user.html', users=users)


@app.route('/<user_id>')
def details_users(user_id):
    userX = Users.query.get_or_404(user_id)
    return render_template('show.html', userX=userX)



@app.route('/creation')
def create_user():
    return render_template("creation.html")

@app.route('/creation/detailPage', methods=["POST"])
def page():
    first_name = request.form.get('firstName')
    last_name = request.form.get('lastName')
    image_url = request.form.get('ImageUrl')

    new_user = Users(first_name=first_name, last_name=last_name, image_url=image_url)
    db.session.add(new_user)
    db.session.commit()

    return render_template("detail.html", new_user=new_user)



# if __name__ == "__main__":

#     app.run(debug=True)


