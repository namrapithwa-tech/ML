from flask import Flask, request, render_template
import pandas as pd
from sklearn.model_selection import KFold, cross_val_score
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)

# Load the diabetes dataset
data = pd.read_csv('diabetes.csv')

# Features and target
X = data.drop(columns=['Outcome'])
y = data['Outcome']

@app.route("/", methods=["GET", "POST"])
def index():
    accuracy = None
    if request.method == "POST":
        # Number of folds input
        n_splits = int(request.form.get("folds", 5))

        # KFold cross-validation logic
        kf = KFold(n_splits=n_splits, shuffle=True, random_state=42)
        model = LogisticRegression(max_iter=200)
        scores = cross_val_score(model, X, y, cv=kf)

        # Accuracy results
        accuracy = scores.mean() * 100

    return render_template("index.html", accuracy=accuracy)

if __name__ == "__main__":
    app.run(debug=True)
