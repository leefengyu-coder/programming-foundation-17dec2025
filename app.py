from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()
    income = float(data.get("income", 0))
    expense = income * 0.10   # 10% rule
    return jsonify({"expense": round(expense, 2)})

if __name__ == "__main__":
    app.run(debug=True)
