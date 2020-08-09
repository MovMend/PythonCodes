# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 21:21:16 2020

@author: ASUS
"""
from neo4j import GraphDatabase
graphdb = GraphDatabase.driver(uri="bolt://localhost:7687", auth=("neo4j", "Saloni@24"))

session = graphdb.session()
print('Enter the username:')
x = input()

q1="""MATCH    (b:User)-[r:RATED]->(m:Movie), (b)-[s:SIMILARITY]-(a:User {username:'"""+x+"""'})
WHERE    NOT((a)-[:RATED]->(m))
WITH     m, s.similarity AS similarity, r.rating AS rating
ORDER BY m.title, similarity DESC
WITH     m.title AS movie, COLLECT(rating)[0..3] AS ratings
WITH     movie, REDUCE(s = 0, i IN ratings | s + i)*1.0 / SIZE(ratings) AS reco
ORDER BY reco DESC
RETURN   movie AS Movie, reco AS Recommendation"""
    
nodes = session.run(q1)

for node in nodes:
    print(node)