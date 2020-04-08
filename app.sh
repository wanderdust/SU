CA_DIR="$PWD"

echo "Warning, you must be inside the Conversational Agents directory to run this script"
echo "Warning,must have the Alana environment on or the dependencies installed before running this script"

gnome-terminal -- /bin/sh -c "cd $CA_DIR/eot/ && ./start.sh; exec bash"
gnome-terminal -- /bin/sh -c "cd $CA_DIR/interface/ && npm start; exec bash"
gnome-terminal -- /bin/sh -c "cd $CA_DIR/prediction/ && rasa run actions --v; exec bash"
gnome-terminal -- /bin/sh -c "cd $CA_DIR/prediction/ && rasa run; exec bash"
gnome-terminal -- /bin/sh -c "cd $CA_DIR/bot/ && echo Run python start.py to start a conversation. Make sure you have all the libraries installed; exec bash"