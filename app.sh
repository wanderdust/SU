CA_DIR="$PWD"

echo "Warning, you must be inside the Conversational Agents directory to run this script"
echo "Warning,must have the Alana environment on or the dependencies installed before running this script"

gnome-terminal -- /bin/sh -c "cd $CA_DIR/eot && echo LSTM Server && ./start.sh; exec bash"
gnome-terminal -- /bin/sh -c "cd $CA_DIR/integrated_modelB_modelC/ && echo Rasa Actions && rasa run actions --v; exec bash"
gnome-terminal -- /bin/sh -c "cd $CA_DIR/integrated_modelB_modelC/ && echo Rasa Run && rasa run; exec bash"
gnome-terminal -- /bin/sh -c "cd $CA_DIR/interface/ && echo INTERFACE && npm run start-db; exec bash"
sleep 3s # This is a bad fix. DB needs to start before the server, or there will be an error.
gnome-terminal -- /bin/sh -c "cd $CA_DIR/interface/ && echo INTERFACE && node server/server.js; exec bash"

gnome-terminal -- /bin/sh -c "cd $CA_DIR/bot/ && echo Run python start.py to start a conversation. Make sure you have all the libraries installed; exec bash"