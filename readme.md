## Install requirements

Install all the requirements for each module. These modules are
* `/eot` -> Follow the instructions in `./eot/Readme.md/`.
* `/interface` -> Follow instructions in `./interface/Readme.md`.
* `/prediction` -> Before installing rasa, install these requirements first: [requirements url](https://github.com/HWUConvAgentsProject/CA2020_instructions/blob/master/rasa_tutorial/requirements.txt). Then run `pip install rasa`.


## Running the Project:

### Step 1. Run Furhat and the Furhat Skill

Open IntelliJ and select `Create new Project`. Select `Kotlin` and` JVM | IDEA` and click Next. In Project name browse `Quiz2` and click Finish. 

At the bottom right of the screen you should see a small window that asks if you want to impport a gradle project. Click on `Import Gradle Project`. 

![image](/interface/public/images/gradle.png)

Then go to `Run` > `Edit Configurations`. Then add `Kotlin` by pressing on "`+`" in the upper left corner. In the next window select `Quiz2.main` for "`Use classpath for module`" and then in `Main class` browse and select `furhatos.app.quiz2.MainKt`. Click the "`Run`" button (green triangle) and the program should start running.

Run Furhat and make sure your Furhat SDK is open in `localhost:8080/#/dashboard`.

Run the quiz file and check if it shows Skill Running at the top left corner of `localhost:8080/#/dashboard`.

### Step 2. Running the program.

#### Option A:

Start Furhat. In `localhost:8080` > Dashboard add a new person by double clicking next to furhat.
Run `./app.sh`. Multiple bash terminals will open each running a unique service.

The last terminal will ask you to run `python start.sh`. Run it.

Finally Run Quiz2 from IntelliJ to run the furhat Skill.

#### Option B:

Run each service manually.

1. Open a terminal tab go to `/eot` and run `./start.sh`

2. Open another tab in the terminal go to `/interface` and run `npm start`

3. Open another tab in the terminal go to `/prediction` and run `rasa run actions --v`

4. Open another tab in the terminal go to `/prediction` and run `rasa run`

5. Run `python server.py` in `bot/` to start the bot.

6. Run `python start.py` in `bot/` to start the bot.

7. Run Furhat if you haven't done so yet. In `localhost:8080/#/dashboard` add a new person by double clicking next to furhat.

8. Run Quiz2 from IntelliJ. 

