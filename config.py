from configparser import ConfigParser

def config(filename="database.ini", section="postgresql"):
    parser = ConfigParser()
    db = {}
    try:
        parser.read(filename)
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                db[param[0]] = param[1]
        else:
            raise Exception(f"Section '{section}' is not found in the '{filename}' file.")
    except Exception as e:
        print(f"An error occurred: {e}") #Prints error to console instead of raising

    return db