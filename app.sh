CA_DIR="$PWD"

echo "Warning, you must be inside the Conversational Agents directory to run this script"

conda activate Alana
gnome-terminal -- /bin/sh -c "cd $CA_DIR/eot/ && ./start.sh; exec bash"
gnome-terminal -- /bin/sh -c "cd $CA_DIR/interface/ && npm start; exec bash"
gnome-terminal -- /bin/sh -c "cd $CA_DIR/prediction/ && rasa run actions --v; exec bash"
gnome-terminal -- /bin/sh -c "cd $CA_DIR/prediction/ && rasa run; exec bash"


cd $CA_DIR/eot/ && ./start.sh &
cd $CA_DIR/interface/ && npm start &
cd $CA_DIR/prediction/ && rasa run actions & /rasa run