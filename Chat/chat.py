from flask  import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqldb://chatter:password@db:3306/messages"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class ChatRecord(db.Model):
    __tablename__ = "messages"

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(511), nullable=False)
    user = db.Column(db.String(255), nullable=False)


@app.route("/", methods=["GET"])
def list_all():
    chat_dicts = [
        { "message": chat.message, "user": chat.user }
        for chat in ChatRecord.query.all()
    ]
    return jsonify(chat=chat_dicts)


@app.route("/add", methods=["POST"])
def add():
    message = request.json.get("message")
    user = request.json.get("user")

    chat = ChatRecord(message=message, user=user)
    db.session.add(chat)
    db.session.commit()

    return jsonify({}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)