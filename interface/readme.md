## Download and install MONGODB
1. [MongoDB download](https://www.mongodb.com/download-center/community). Save it in your `/home` directory. If using Linux, select the **TGZ** package. If using mac, select the default package.
2. In the `/home` directory, create a folder called `mongodb-data`. This is where the mongodb data will be stored.
3. Run `/home/yourusername/mongodb/bin/mongod --dbpath=/home/yourusername/mongodb-data` , where the first part is the direction to the mongodb folder, and the second one is the folder you created in step 2. Verify it works, if it does, you can shut the database for now. Change `/yousername` for your username.

## Run web app
1. Install node.js
2. Go to the app directory `/interface` and run `npm install`
3. Add execute permissions to `start-db.sh` using the command `chmod +u start-db.sh`. This is the script that starts the database, so you need to be able to execute it.
4. Start the program by running `npm start`. If any problems are found, refer to point 3 in *Download and Install MONGODB* and make sure you have it installed correctly. Make sure you also have node.js installed correctly.
5. Look for the app in `localhost:3000`.

## Quick start (When everything has already has already been installed)
`npm start-db`
and then 
`npm start`

Now the api should be on `localhost:3000`.
________

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