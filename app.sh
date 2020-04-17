CA_DIR="$PWD"

echo "Warning, you must be inside the Conversational Agents directory to run this script"
echo "Warning,must have the Alana environment on or the dependencies installed before running this script"

gnome-terminal -- /bin/sh -c "cd $CA_DIR/interface/ && echo INTERFACE && npm run start-db; exec bash"
sleep 3s # This is a bad fix. DB needs to start before the server, or there will be an error.
gnome-terminal -- /bin/sh -c "cd $CA_DIR/eot && echo LSTM Server && ./start.sh; exec bash"
gnome-terminal -- /bin/sh -c "cd $CA_DIR/integrated_modelB_modelC/ && echo Rasa Actions && rasa run actions --v; exec bash"
gnome-terminal -- /bin/sh -c "cd $CA_DIR/integrated_modelB_modelC/ && echo Rasa Run && rasa run; exec bash"
gnome-terminal -- /bin/sh -c "cd $CA_DIR/interface/ && echo INTERFACE && node server/server.js; exec bash"
gnome-terminal -- /bin/sh -c "cd $CA_DIR/bot/ && echo Starting server.py && python server.py; exec bash"
#gnome-terminal -- /bin/sh -c "cd $CA_DIR/bot/ && echo Starting start.py && python start.py; exec bash"

gnome-terminal -- /bin/sh -c "cd $CA_DIR/bot/ && echo 1. RUN FURHAT AND FURHAT SKILLS TO CONTINUE. 2. RUN python start.py TO START; exec bash"