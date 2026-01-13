from flask import Flask, render_template, request
from textblob import TextBlob
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    score = 0
    emoji = ""
    sentiment_class = ""
    if request.method == "POST":
        text = request.form.get("text", "").strip()
        if text:
            analysis = TextBlob(text)
            polarity = analysis.sentiment.polarity  # -1 to +1
            score = int(abs(polarity) * 100)
            if polarity > 0:
                result = "Positive"
                emoji = "😊"
                sentiment_class = "positive"
            elif polarity < 0:
                result = "Negative"
                emoji = "😠"
                sentiment_class = "negative"
            else:
                result = "Neutral"
                emoji = "😐"
                sentiment_class = "neutral"
    return render_template(
        "index.html",
        result=result,
        score=score,
        emoji=emoji,
        sentiment_class=sentiment_class
    )
if __name__ == "__main__":
    app.run(debug=True)
