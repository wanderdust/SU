## 1. Install requirements

Install all the requirements for each module. These modules are
* `/eot` -> requirements.txt
* `/prediction` -> Before installing rasa, install these requirements first: [requirements url](https://github.com/HWUConvAgentsProject/CA2020_instructions/blob/master/rasa_tutorial/requirements.txt). Then run `pip install rasa`.
* `/interface` -> package.json (requires node.js). Make sure you grant execute pemissions to `start-db.sh`

## 2. Run the program

### Option A:

Run `./app.sh`. Multiple bash terminals will open each running a unique service.

The last terminal will ask you to run `python start.sh`. Run it.

### Option B:

Run each service manually.

1. Open a terminal tab go to `/eot` and run `./start.sh`

3. Open another tab in the terminal go to `/interface` and run `npm start`

4. Open another tab in the terminal go to `/prediction` and run `rasa run actions --v`

5. Open another tab in the terminal go to `/prediction` and run `rasa run`

6. Run `python start.py` in `bot/` to start the bot.

