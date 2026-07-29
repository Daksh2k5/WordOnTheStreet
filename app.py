from flask import Flask, render_template, request, jsonify
import requests
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

try:
    analyzer = SentimentIntensityAnalyzer()
except LookupError:
    nltk.download('vader_lexicon')
    analyzer = SentimentIntensityAnalyzer()

app = Flask(__name__)

def fetch_sentiment_data(keyword, limit=30):
    url = "https://api.pullpush.io/reddit/search/comment/"
    params = {
        "q": keyword,
        "size": min(limit, 100),
        "sort": "desc"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        comments = data.get("data", [])

        if not comments:
            return {"error": f"No comments found containing '{keyword}'."}

        total_score = 0
        samples = []

        for comment in comments:
            body = comment.get("body", "").strip()
            if not body or body == "[deleted]" or body == "[removed]":
                continue

            scores = analyzer.polarity_scores(body)
            total_score += scores["compound"]

            clean_body = body.replace('\n', ' ').strip()
            snippet = clean_body[:120] + "..." if len(clean_body) > 120 else clean_body

            samples.append({
                "snippet": snippet,
                "score": round(scores["compound"], 2)
            })

        count = len(samples) if samples else 1
        avg_score = round(total_score / count, 3)

        return {
            "keyword": keyword,
            "average_score": avg_score,
            "count": count,
            "samples": samples[:6]
        }

    except requests.exceptions.RequestException as e:
        print(f"PullPush API Error: {e}")
        return {"error": "Failed to connect to the Reddit archive API. Please try again later."}
    except Exception as e:
        print(f"Unexpected Error: {e}")
        return {"error": f"An error occurred during analysis: {str(e)}"}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    keyword = request.json.get("keyword", "").strip() if request.json else ""
    if not keyword:
        return jsonify({"error": "Please enter a keyword."}), 400

    result = fetch_sentiment_data(keyword, limit=50)
    if "error" in result:
        return jsonify(result), 500

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, port=5000)