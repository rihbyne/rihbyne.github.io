Title: Securing User Accounts
Date: 2016-02-03 13:45
Slug: user-auth
Tags: security, encryption, hashing, salting 
Authors: Rihan Pereira
Summary: My experiences on securing user accounts 

This post details the popular __Salt & Hashing__ technique used to safely store secret/confidential
information into a persistent db.

 
Some notes about the above practice:

 - Avoids the possibility of duplicate hash occurrence if a attribute of 2 distinct entities result in same
 value. For example, it is possible to receive similar passwords from multiple users while performing Basic Auth.
 In such a scenario, Salt transforms the input into completely random output which is finally followed by
 Hashing.

 - Good rule of thumb is to avoid storing plain text or raw password directly entered by the user. This technique
 stores the hash of the password along with its corresponding salt value generated.
 
 - In case the database gets breached, bad guys are left with only hash values of the passwords. They will try to
 detect hash collisions by guessing possible characters for a given hash. If they are patient enough,
 they may succeed and get hold of negligible number of accounts but chances are very rare.

During the following user interactions we make use of the technique. The below code snippets contains explainations in the form of comments.

* Register
* Login
* Forgot Password
* Reset Password

1. Register
------------
--------------------

```
:::js
// random value generator function

 function hashIt(data) {
  var sha = crypto.createHash('sha1')
  sha.update(data + '', 'ascii')
  return sha.digest('hex')
}

// salt generator function

function createSalt() {
  // this can go in environment variable
  var chars='liDvM/OpICyK3MQzSzt/60px+mEMGco4Z1VhCxWVpxsHDF+zQB1wrhW/LvKdM49Dw5cz6PNoQRF0hmQFfhz3Cg=='
  var salt=''
  for(var i=11; i>0; --i){
    salt += chars[Math.round(Math.random()*(chars.length-1))]
  }
  return salt
}

salt=createSalt() // generate salt
password=hashIt(salt+password) // mixture of plain text password and given salt
email=email.toLowerCase()
accountID=hashIt(email) // also hash email for user_id

// finally save the user object to the DB
var u = UserModel(object)
u.save() // something like that
```

2. Login
------
--------------------------------

```
:::js
UserModel.isActive() // before login make user to check whether user is activated.
                     // If not, promote the web console for activation link

// fetch saved salt & compute hash for current password
var current_hash=crypt.hashIt((saved_user_object.salt) + password) 

var saved_hash = saved_user_object.password // fetch hashed password from DB

return Boolean(current_hash + saved_hash) // evalues to true/false
```

3. Forgot Password
-----------------
-------------------------
```
:::js
var token = require('token')
token.defaults.secret = '<secret string>'
token.defaults.timeStep = 1 * 60 * 60 

function generate (data) {
  return token.generate(data.toString())
}

var time = Date.now()
var pattern = user_object._id + time.toString() // make one of your own
var auth = generate(pattern)

var accountInfo={
  'email':email,
  'first_name':result.first_name,
  'last_name':result.last_name,
  'vhash':auth,
  'flag':flag,
  'time':time,
  //other app specific params
}

mail_user(accountInfo) // mail user the link with vhash parameter
```

4. Reset Password
-------------------
---------------------

```
:::js
var pattern = user_obj._id + time.toString()
var tokenTest = token.verify(pattern.toString(), auth.toString()) // get the auth & time param from request body
                                                                  // to compose pattern
var tokenResponse = tokenFeedback(tokenTest) // only check valid token else say token is expired/wrong/invalid

//check for valid auth value 
Boolean(request[body].auth === user_obj.auth) //should be true

//reset password as follows
var salt=createSalt()
var hashpass=crypt.hashIt(salt + password)
```
