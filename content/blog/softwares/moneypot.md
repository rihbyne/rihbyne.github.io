Title: Moneypot Project - the betting app
Date: 2016-03-14 22:01
Slug: the-moneypot-project
Tags: nodejs, postgresql, generators, btc, satoshi, kelly criteron
Authors: Rihan Pereira
Summary: A case study on the moneypot project - its design, architecture

Moneypot is a bitcoin wallet but not a full fledge hot wallet out there like blockchain’s “my wallet” or
coinbase’s wallet.Money wallet handles bitcoin money for its users. Usually, all the transactions take place
in __bits(1BTC = 106)__ or __satoshi(1BTC = 108)__. Besides this, Moneypot  serves as a platform for application
developers who make gambling games to handle the mathematics behinding casino logic, the betting criteria,
user authentication,etc. Before any app can use Moneypot services, that particular app is approved and
authorized  by Moneypot and then the services are made available.Since, Moneypot act as a bitcoin fund
manager.It can be used to receive bitcoins from cold storage using cold addresses or from existing hot
wallet using hot bitcoin addresses.It can also be used to send bitcoins to others using receiver's bitcoin
address. The Apps which use moneypot's API allows its users to get btc's in bits from its moneypot wallet as
well as withdraw deposited funds back into the wallet once done with game playing or betting.This allows
users who play betting games to transfer losable money from moneypot wallet to apps and vice versa.So the
moneypot wallet serves as a sandbox for money transfer between games that use its API.

Components of Moneypot :
----------------------------

![overview\_moneypot]({attach}../../images/moneypot/image04.png)

A bitcoin wallet implementation requires the use of bitcoin-core. The bitcoin-core, also called as a
full-node is a program that is used to validate transactions and blocks.Since bitcoin doesn’t have a
centralized governing body, anyone who runs a bitcoin-core helps the peer-to-peer network. So if you are
running a full-node you become the volunteer.Your full-node accepts transactions and blocks from other full
nodes, validating those and relaying them to next full nodes.In moneypot’s case, running bitcoin-core is
required because it gives them full control over their node and take special safety precautions. To interact
with bitcoin-core, bitcoind is required. bitcoind is a daemon which runs in the background and talks with
bitcoin-core. The talking takes place in JSON-RPC.There is a seperate CLI utility which is also a RPC client
which connects to bitcoind.So bitcoind serves as a RPC server.In order to programmatically talk with bitcoind
there are languages bindings available. For javascript, this project makes use of bitcoinjs and bitcoinjs-lib.

The __node-pg__ is node-postgres db driver used in Moneypot to fire queries to postgresql DB.

The diagram clearly illustrates the five core components of Moneypot:

-  The __moneypot-api__ implements Oauth framework version 2.0. It acts as a Oauth provider for apps like
exampleapp.com as shown in the figure. Any external app which uses moneypot-api gets user authentication
handling, and other resources served via http.

-  The __moneypot-web__ is web application which allows users to sign into the wallet and manage funds like receive
and move around its approved apps for betting.Along with this, it gives you meta-data about your money in
wallet.

-  The __moneypot-depositor__ talks with bitcoind which in turn talks to full node connected to blockchain
network.

-  The __socketpot__ is moneypot’s websocket server and its main purpose is to stream notification and alerts over
the network in real time to the apps which connect to it.

Apps on Moneypot:
--------------------

![apps\_moneypot]({attach}../../images/moneypot/image10.png)

From the above figure,  an exampleBet.com built by its developers uses Moneypot’s API for its services.
exampleBet.com is deployed seperately on different machine but uses moneypot’s services served at
api.moneypot.com. Before any app can use moneypot-api, they need to register the app on moneypot-web.On
registering the app, moneypot-web will generate 'app_id' followed by other params like 'app_secret' which are
required if using confidential flow or access_token is required if using implicit flow. So, the moneypot api
handles the third-party authentication. Now, the application developer can make request on moneypot api from
the browser app or from the server app.Just remember that, every time you make a request to api server you
have to include app_id and (access_token or app_secret) depending on the flow type, not doing so, will get
403 status code. All the endpoints are  located at api-docs.


Users on Moneypot:
---------------------

![api\_web]({attach}../../images/moneypot/image08.png)

The diagram illustrates how user uses moneypot-api and moneypot-web.The moneypot-web offers administrative
dashboard UI for its users.User plays any of the approved games(Apps) listed on moneypot.com.Assuming User
is not logged into any app. Before using any app, the user should login into the app he/she wishes to play.
Mosts apps will include the login UI, but, in the background it will call moneypot.com/oauth/authorize?<PARAMS>
to login the user on moneypot’s server instead of their own app server.The javascript app behind the scene will
parse out  the access_token and auth_id which will have a two-weeks expiration timeout. Once logged inside,
user may deposit bits he wishes to gamble from moneypot dashboard to that app and vice versa.Every bet the user
makes,whether its a win or loss, the app developer gets the steady commission, the moneypot gets some percentage
of steady commission. If user losses the bet, the wagered amount is lost and taken by the bankroll. If the user
wins the user wins the betted amount along with the winning odds.

Application Architecture:
----------------------------

![app\_stacks]({attach}../../images/moneypot/image05.png)

The above three figures provides a top-to-bottom view of how the services in moneypot are layered.One thing you
will notice missing is the socketpot code layout. Thats because I dont have access to socketpot yet.All the three
figures have the “libs” block which is the library block.It contains common javasript modules which are accessed
and used more than once across most of the application.

Moneypot-api App Stack:
---------------------------

moneypot-api running on NodeJS instance version 5.x. Its ES-6 compatible.Meaning that it supports new js features
like promises, generators,iterators,sync, etc.The koa-middleware block, koa is a web-framework used for building
web apps and API’s.you get koa-core and depending on your need can install middlewares for your application. The
koa compatible middlewares are named like koa-*(eg-> koa-bodyparser, koa-acl, koa-json-parser,etc). It plays well
and inherently supports ES6 features.

The api at request/response level is a object contains an array which hold generator functions which executed in
“U” shaped stack like manner as per the request.The array holds middlewares in use. Koa uses “yield” and “next”
to pass control between the series of functions(middlewares).When any middleware down the “U” shape invokes “yield
next” down the stream, the function suspends its execution and passes the control to the next function. Until
there are no more middlwares down the stream to execute, the request follows back to the initial middleware and
resumes to execute the remaining code from where it got suspending by “yield next”.This way, Moneypot-api uses
many koa-* middlewares in its codebase.Its simple and pluggable.

A short code excerpt from moneypot-api just shows that.

```
:::js
app.use(bodyparser({
  // Treat 'Content-Type: text/plain' body as JSON
  extendTypes: { json: ['text/plain'] }
}));

// x-response-time
app.use(function *(next){
 var start = new Date;
 yield next;
 var ms = new Date - start;
 this.set('X-Response-Time', ms + 'ms');
});

// logger
app.use(function *(next){
 var start = new Date;
 yield next;
 var ms = new Date - start;
 console.log('%s %s - %s', this.method, this.url, ms);
});
```
