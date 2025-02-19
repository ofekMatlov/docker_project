from flask import Flask
import json
import logging
import os
import printColors

logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s|%(funcName)s|%(levelname)s|%(message)s',
                    handlers = [logging.FileHandler("app.log"),
                               logging.StreamHandler()]
                    )

app = Flask(__name__)
@app.route("/")
def systemPage() -> str:
    logging.info("The user has accessed the path /")
    return printColors.printBlack("Welcome to my system, Please login")

@app.route("/login/<name>")
def loginPage(name : str) -> str:
        logging.info(f'"The user has accessed the login with name " {name}')      
        if name in my_list:
            logging.info(f"Name {name} exist in list, access granted")
            return  printColors.printGreen("Access Granted")
        else:
            logging.warning(f"Name {name} does not exist, access denied")
            return printColors.printRed("Access Denied")

@app.route("/addName/<name>")
def addName(name : str) -> str:
    logging.info(f'"The user has added the name " {name}')     
    if name in my_list:
        logging.info(f"Name {name} exist in list, access granted")
    else:
        my_list.append(name)
        with open("config.json", 'w') as config:
            json.dump(my_list, config, indent=4)
        return printColors.printGreen(f"{name} Access Granted") 
try:
    with open("config.json") as config:
        my_list = json.load(config)
except FileNotFoundError:
    logging.critical("Error: config file is missing")    
            
if __name__ == "__main__":        
    app.run(host=os.environ.get("HOST_IP"), port=5000, debug=True)
        

