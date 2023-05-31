import os
ROOT_DIR = os.path.join(os.path.dirname(__file__),"../")

class Base_Config(object):
    def getDBConnectionString():
        config= {}
        config["username"] = os.getenv('DB_USERNAME')
        config["host"] = os.getenv('DB_HOST')
        config["password"] = os.getenv('DB_PASSWORD')
        config["database"] = os.getenv('DATABASE')
        config["port"] = os.getenv('DB_PORT')
        
        return f"mysql+pymysql://{config['username']}:{config['password']}@{config['host']}:{config['port']}/{config['database']}"
    
    SQLALCHEMY_DATABASE_URI = getDBConnectionString()