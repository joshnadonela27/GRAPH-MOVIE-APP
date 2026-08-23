import os
from dotenv import load_dotenv
from neo4j import GraphDatabase

load_dotenv()

URI = os.getenv("COGNODB_URI")
USER = os.getenv("COGNODB_USER")
PASSWORD = os.getenv("COGNODB_PASSWORD")

def seed_database():
    print("Connecting to CognoDB...")
    driver = GraphDatabase.driver(URI, auth=(USER, PASSWORD))
    
    with driver.session() as session:
        # Step 1: Clear existing data
        session.run("MATCH (n) DETACH DELETE n")
        
        # Step 2: Create graph nodes and relationships in a single CREATE query
        query = """
        CREATE 
          (m1:Movie {title: 'Inception', year: 2010}),
          (m2:Movie {title: 'Interstellar', year: 2014}),
          (m3:Movie {title: 'Titanic', year: 1997}),
          (a1:Actor {name: 'Leonardo DiCaprio'}),
          (a2:Actor {name: 'Anne Hathaway'}),
          (g1:Genre {name: 'Sci-Fi'}),
          (g2:Genre {name: 'Drama'}),
          (a1)-[:ACTED_IN]->(m1),
          (a1)-[:ACTED_IN]->(m3),
          (a2)-[:ACTED_IN]->(m1),
          (a2)-[:ACTED_IN]->(m2),
          (m1)-[:IN_GENRE]->(g1),
          (m2)-[:IN_GENRE]->(g1),
          (m3)-[:IN_GENRE]->(g2)
        """
        session.run(query)
        print("Success! Movie graph data loaded into CognoDB.")
        
    driver.close()

if __name__ == "__main__":
    seed_database()