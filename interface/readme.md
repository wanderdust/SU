## Download and install MONGODB
1. [MongoDB download](https://www.mongodb.com/download-center/community). Save it in your home directory.
2. Go to your home directory `cd ~` and create a folder called `mongodb-data`.
3. Run `/home/username/mongodb/bin/mongod --dbpath=/home/username/mongodb-data` , where the first part is the direction to the mongodb folder, and the second one is the folder you created in step 2. Verify it works, if it does, you can shut the database for now.

## Run web app
1. Install node.js
2. Go to the app directory `/interface` and run `npm install`
3. Start the Database running `npm run start-db`. If that doesn't work, go to your home directory `cd ~` and run `/home/username/mongodb/bin/mongod --dbpath=/home/username/mongodb-data`, using your own paths. Then go to the app directory and run `npm run start-mongoose`. The db server should be up.
4. Run the web app using `npm start`

## Quick start
`npm run start-db`
`npm start`