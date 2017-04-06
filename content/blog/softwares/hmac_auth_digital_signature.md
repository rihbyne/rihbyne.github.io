Title: Securing APIs with HMAC Authentication and Digital Signature
Date: 2016-04-10 9:00
Slug: hmac-authentication
Tags: crytography, symmetric key encryption, digital signature, verification
Authors: Rihan Pereira
Summary: HMAC in general & applying it on service based APIs

In this blog post I discuss what HMAC is. Why would anyone wants to use it in practice and how to go about implementing it.

HMAC & why use it:
--------------------
Hash of Message Authentication Code(MAC) signs HTTP URL request or even JSON-RPC/XML communication interfaces 
& guarantees 2 things:

* Authentication - ensures receiving party that the request has come from the one who is in possession with SECREY_KEY
* Integrity - Small change in the values of arguments attached to the request produces completely different hash. Hence, maintaining originality.

It is able to produce Digital Signature(DS) by making use of symmetric key
crytography. This symmetric key cryptography makes use of shared secret key which the trusted two parties must 
possess before computing HMAC. However, this implementation comes at a price; employing this type of security 
requires secret key provider to secure its key data. 

Securing parameter around where your shared secret keys by considering this features -

* Good to store secret keys in distributed systems environment. Geo-replication state assures no single point of
  failure. Your application continues to map access key id to its secret key even in crash, attacked
  circumstances.
* DOS, DDOS attack proof
* Whitelisting only certain IPs to access key data server

Implementation:
-----------------

HMAC needs following functions to setup:

* __key pair generator__ - returns publishable/secret key pair for new device
* __message encryptor__ - returns signature produced for given text & key
* __signature validator__ - returns boolean; determines whether signature is valid/invalid for given text & key. Makes
use of '__message encryptor__' function internally

key pair generator
----------------------

```
:::js
var algorithm = "sha512"

//text -> mix in form details of company/individual/organization you are generating keys for
module.exports.createKeyPair = function (text) {
  var keyobj = {
    pubk:null,
    secretk:null
  }

  var pubk = crypto.createHash('sha512')
  var secretk = crypto.createHash('sha512')

  pubk.update((text + createSalt())) // randomizer - can be customized, requires to be confidential
  secretk.update((text + createSalt()))

  keyobj.pubk = pubk.digest('hex') // publishable key a.k.a access key id
  keyobj.secretk = secretk.digest('base64') // secret key. should be stored safe.

  return keyobj
}

```

messsage encryptor
----------------------
```
:::js
// k -> secret keyobj
// text -> arguments encoding with &,= order necessary, small change in text outputs completely different signature
// cb -> callback

function encryptMessage(text, k, cb) {
  var hash
  var hmac = crypto.createHmac(algorithm, k)

  hmac.setEncoding('hex')

  // callback is attached as listener to stream's finish event:
  hmac.end(text, function () {
    hash = hmac.read()
    cb(hash)
  })
}
```

signature validator
----------------------
```
:::js
// text -> arguments encoded with &, = order should be same as the one used to sign the request
// signature -> hex encoded value
// secretk -> shared secret key used between two trusted parties.

function validateSignature(text, signature, secretk, cb) {
  this.encryptMessage(text, secretk, function (hash) {
    if (signature === hash) {
      //log.info('Signature is Valid')
      cb(true)
    } else {
      log.info(signature + ' !== \n' + hash)
      cb(false)
    }
  })
}
```
