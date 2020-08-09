# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 14:42:07 2020

@author: Saloni
"""

from neo4j import GraphDatabase

class HelloWorldExample:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def print_greeting(self):
        with self.driver.session() as session:
            greeting = session.write_transaction(self._create_and_return_greeting)
            print(greeting)

    @staticmethod
    def _create_and_return_greeting(tx):
        result = tx.run("MATCH (g:Genre) RETURN g LIMIT 1")
        return result.single()[0] 
 

if __name__ == "__main__":
    greeter = HelloWorldExample("bolt://localhost:7687", "neo4j", "Saloni@24")
    greeter.print_greeting()
    greeter.close()