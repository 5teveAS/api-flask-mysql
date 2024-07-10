class DevelomentConfig():
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''  # Deja esto vacío si no has establecido una contraseña
    MYSQL_DB = 'api_flask'
    
config = {
    'development': DevelomentConfig
}