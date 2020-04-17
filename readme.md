## 1. Install requirements

Install all the requirements for each module. These modules are
* `/eot` -> requirements.txt
* `/prediction` -> Before installing rasa, install these requirements first: [requirements url](https://github.com/HWUConvAgentsProject/CA2020_instructions/blob/master/rasa_tutorial/requirements.txt). Then run `pip install rasa`.
* `/interface` -> package.json (requires node.js). Make sure you grant execute pemissions to `start-db.sh`

## 2. Running IntelliJ IDEA:

Import the Quiz project as JVM IDEA and then select Quiz.

then in Run -> Edit configurations add Kotlin by pressing on "+" in upper left corner. in main class-> select 
furhatos.app.quiz.MainKt and set JRE to default.

In main.kt file import gradle.

MAke sure your Furhat SDK is open in http://localhost:8080/#/dashboard

Run the quiz file and check if it shows Skill Running at the top left corner of localhost:8080.

### Option A:

Run `./app.sh`. Multiple bash terminals will open each running a unique service.

The last terminal will ask you to run `python start.sh`. Run it.

### Option B:

Run each service manually.

1. Open a terminal tab go to `/eot` and run `./start.sh`

3. Open another tab in the terminal go to `/interface` and run `npm start`

4. Open another tab in the terminal go to `/prediction` and run `rasa run actions --v`

5. Open another tab in the terminal go to `/prediction` and run `rasa run`

6. Run `python server.py` in `bot/` to start the bot.

7. Run `python start.py` in `bot/` to start the bot.

8. Run `kotlin file`. 

