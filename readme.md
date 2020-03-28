## Install requirements

Install all the requirements for each module. These modules are
* /eot -> requirements.txt
* /prediction -> Before installing rasa, install first these requirements first: [requirements url](https://github.com/HWUConvAgentsProject/CA2020_instructions/blob/master/rasa_tutorial/requirements.txt). Then run `pip install rasa`.
* /interface -> package.json (requires node.js)

## Run the program

1. Open a terminal tab go to /eot and run `./start.sh`

2. Open another tab in the terminal go to /interface and run `npm run start-db`

3. Open another tab in the terminal go to /interface and run `npm start`

4. Open another tab in the terminal go to /rasa/test and run `rasa run actions -v`

5. Open another tab in the terminal go to /rasa/test and run `rasa run`

6. Run `python main.py` in bot/ to start the bot.

