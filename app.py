from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    sentiment = None
    sentiment_category = ""
    sentiment_class = ""
    
    if request.method == 'POST':
        user_text = request.form['user_text']
        blob = TextBlob(user_text)
        sentiment_score = round(blob.sentiment.polarity * 100)
        
        if sentiment_score <= -50:
            sentiment_category = "very negative"
            sentiment_class = "very-negative"
        elif -50 < sentiment_score <= 0:
            sentiment_category = "somewhat negative"
            sentiment_class = "somewhat-negative"
        elif sentiment_score == 0:
            sentiment_category = "neutral"
            sentiment_class = "neutral"
        elif 0 < sentiment_score <= 50:
            sentiment_category = "somewhat positive"
            sentiment_class = "somewhat-positive"
        else:
            sentiment_category = "very positive"
            sentiment_class = "very-positive"
        
        sentiment = sentiment_score

    return render_template('index.html', sentiment=sentiment, sentiment_category=sentiment_category, sentiment_class=sentiment_class)


if __name__ == '__main__':
    app.run(debug=True)
