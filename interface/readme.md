## Download and install MONGODB
1. [MongoDB download](https://www.mongodb.com/download-center/community). Save it in your home directory. If using Linux, select the TGZ option.
2. Go to your home directory `cd ~` and create a folder called `mongodb-data`.
3. Run `/home/username/mongodb/bin/mongod --dbpath=/home/username/mongodb-data` , where the first part is the direction to the mongodb folder, and the second one is the folder you created in step 2. Verify it works, if it does, you can shut the database for now.

## Run web app
1. Install node.js
2. Go to the app directory `/interface` and run `npm install`
3. Start the Database running `npm run start-db`. If that doesn't work, go to your home directory `cd ~` and run `/home/username/mongodb/bin/mongod --dbpath=/home/username/mongodb-data`, using your own paths. Then go to the app directory and run `npm run start-mongoose`. 
4. Stop the database. And add execute permission to `start-db.sh` file with the command `chmod +u start-db.sh`
5. Run the web app using `npm start`

## Quick start (When everything has already has already been installed)
`npm start`

Now the api should be on `localhost:3000`.

__________

## Making a request

**api**: `localhost:3000/webapp/api`

**posible requests:**

```
{object: "music", toggle: "off"} or {object: "music", toggle: "on"};
{object: "lights", toggle: "off"} or {object: "lights", toggle: "on"};
{object: "heating", toggle: "off"} or {object: "heating", toggle: "on"};
{object: "tv", toggle: "off"} or {object: "tv", toggle: "on"};
```

**Javascript Example**
```
let data = {object: "music", toggle: "on"};

fetch("localhost:3000/webapp/api", {
  method: "POST", 
  body: JSON.stringify(data),
  headers:{
    'Content-Type': 'application/json'
  }
}).then(res => {
  console.log("Request status ", res.status);
});
```