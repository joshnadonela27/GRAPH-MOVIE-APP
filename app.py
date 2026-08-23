import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from neo4j import GraphDatabase

load_dotenv()

app = Flask(__name__)
CORS(app)  # Enables frontend requests

URI = os.getenv("COGNODB_URI")
USER = os.getenv("COGNODB_USER")
PASSWORD = os.getenv("COGNODB_PASSWORD")

@app.route('/api/recommend', methods=['GET'])
def get_recommendations():
    movie_title = request.args.get('title')
    
    if not movie_title:
        return jsonify({"error": "Please enter a movie title"}), 400

    # Multi-hop graph query with case-insensitive search
    query = """
    MATCH (m:Movie)<-[:ACTED_IN]-(a:Actor)-[:ACTED_IN]->(rec:Movie)-[:IN_GENRE]->(g:Genre)
    WHERE toLower(m.title) = toLower($title) AND toLower(rec.title) <> toLower($title)
    RETURN rec.title AS recommended_title, a.name AS actor, g.name AS genre
    LIMIT 5
    """

    try:
        driver = GraphDatabase.driver(URI, auth=(USER, PASSWORD))
        with driver.session() as session:
            result = session.run(query, title=movie_title)
            recommendations = [
                {
                    "title": record["recommended_title"],
                    "actor": record["actor"],
                    "genre": record["genre"]
                }
                for record in result
            ]
        driver.close()
        return jsonify(recommendations), 200
    except Exception as e:
        return jsonify({"error": "Failed to query database"}), 500

if __name__ == '__main__':
    print("Starting Flask server on http://127.0.0.1:5000")
    app.run(port=5000, debug=True)