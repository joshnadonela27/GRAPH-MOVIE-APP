# 🎬 Movie Graph Recommendation Engine

A full-stack movie recommendation web application built with Python, Flask, and a CognoDB Graph Database. Unlike simple keyword matching, this application uses graph relationship traversal to recommend movies based on shared actor connections and genre associations.

---

## 📖 Project Overview

When a user searches for a movie title, the backend queries a graph database to trace connected entities:
1. **Locates the target movie** specified by the user.
2. **Traverses relationships** to find all actors (`:ACTED_IN`) who starred in that movie.
3. **Finds related movies** starring those same actors, excluding the original search query.
4. **Retrieves associated genres** (`:IN_GENRE`) to enrich the final recommendation output.

The query logic handles case-insensitive inputs (`toLower()`) to ensure searches succeed regardless of capitalization.

---

## 🛠️ Tech Stack & Architecture

* **Frontend:** Standard HTML5, CSS3, and Vanilla JavaScript (ES6+ using `fetch()` API for seamless asynchronous backend calls).
* **Backend:** Python 3 with Flask web framework to serve API endpoints.
* **Database Driver:** `neo4j` official driver used to connect securely to CognoDB Cloud.
* **Configuration:** `python-dotenv` for local environment variable management to protect sensitive credentials.

---

## 🚀 Setup & Installation Guide

Follow these steps to set up and run the application on your local machine:

### 1. Clone the Repository
Open your terminal or command prompt and clone the project:
```bash
git clone [https://github.com/joshnadonela27/GRAPH-MOVIE-APP.git](https://github.com/joshnadonela27)
cd GRAPH-MOVIE-APP
