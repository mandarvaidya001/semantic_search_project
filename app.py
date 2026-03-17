from flask import Flask, request, jsonify, render_template
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import json

app = Flask(__name__)

# Load dataset
with open("posts.json") as f:
    posts = json.load(f)

texts = [p["text"] for p in posts]

# Load AI model
model = SentenceTransformer("all-MiniLM-L6-v2")
post_embeddings = model.encode(texts)


# ------------------- WEBSITE PAGES -------------------

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/searchpage")
def searchpage():
    return render_template("search.html")


@app.route("/dataset")
def dataset():
    sample_posts = posts[:20]   # show first 20 posts
    return render_template("dataset.html", posts=sample_posts)


# ------------------- SEARCH API -------------------

@app.route("/search")
def search():
    query = request.args.get("q")
    mode = request.args.get("mode", "semantic")

    interpreted_meaning = f"The system interprets this query as related to: {query}"

    # Keyword search
    if mode == "keyword":
        results = []
        for p in posts:
            if query.lower() in p["text"].lower():
                results.append({
                    "username": p["username"],
                    "platform": p["platform"],
                    "text": p["text"],
                    "likes": p["likes"],
                    "score": 1.0,
                    "reason": "Matched by exact keyword"
                })

        return jsonify({
            "meaning": interpreted_meaning,
            "results": results
        })

    # Semantic search
    query_embedding = model.encode([query])
    scores = cosine_similarity(query_embedding, post_embeddings)[0]

    top_results = [
        {
            "username": posts[i]["username"],
            "platform": posts[i]["platform"],
            "text": posts[i]["text"],
            "likes": posts[i]["likes"],
            "score": float(scores[i]),
            "reason": f"Matched semantically with similarity score {scores[i]:.2f}"
        }
        for i in sorted(range(len(scores)), key=lambda x: scores[x], reverse=True)[:3]
    ]

    return jsonify({
        "meaning": interpreted_meaning,
        "results": top_results
    })


if __name__ == "__main__":
    app.run(debug=True)