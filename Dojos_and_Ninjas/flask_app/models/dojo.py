
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
from flask_app.models import ninja
# import re
# from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt(app)
# The above is used when we do login registration, be sure to install flask-bcrypt: pipenv install flask-bcrypt


class Dojos:
    db = "dojos_and_ninjas" #which database are you using for this project
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.ninjas = []
        # What changes need to be made above for this project?
        #What needs to be added her for class association?



    # Create Users Models
    @classmethod
    def create_dojo(cls, data):
        query = """
        INSERT INTO dojos (name)
        VALUES (%(name)s);
        """
        return connectToMySQL(cls.db).query_db(query, data)
    



    # Read Users Models
    @classmethod
    def get_all_dojos(cls):
        query = """
        SELECT * FROM dojos;
        """
        results = connectToMySQL(cls.db).query_db(query)
        all_dojos = []
        for dojo in results:
            all_dojos.append(cls(dojo))
            print (dojo)
        return all_dojos
    
    @classmethod
    def get_dojos_with_ninjas(cls, dojo_id):
        query = """
        SELECT * FROM dojos
        LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id
        WHERE dojos.id = %(id)s
        ; """
        results = connectToMySQL(cls.db).query_db(query, {'id': dojo_id})
        dojo = cls(results[0])
        for row_from_db in results:
            ninja_data = {
                'id': row_from_db['ninjas.id'],
                'dojo_id':  row_from_db['dojo_id'],
                'first_name': row_from_db['first_name'],
                'last_name': row_from_db['last_name'],
                'age': row_from_db['age'],
                "created_at": row_from_db["ninjas.created_at"],
                "updated_at": row_from_db["ninjas.updated_at"]
            }
            dojo.ninjas.append(ninja.Ninja(ninja_data))
        return dojo

        
    @classmethod
    def get_one_dojo(cls, dojo_id):
        query = """
        SELECT * FROM dojos
        WHERE id = %(id)s;
        """
        data = {'id': dojo_id}
        result = connectToMySQL(cls.db).query_db(query,data)
        return cls(result[0])


    # Update Users Models



    # Delete Users Models

