Title: Putting together a basic, functional Crypto-Currency wallet
Date: 2017-12-03 14:09
Slug: digital-wallet
Summary: Involved in the design & architecture of digital wallet capable of making deposits, processing withdrawals in bulk through external payment gateways like bitgo, Infura. The version 2 replaces third-party payment gateway with very own bitcore SDK based hot wallet.


Wallet Anatomy:
-----------------

![block\_diagram]({attach}../images/diy/wallet_as_a_whole.png)

Above diagram displays the wallet's building blocks, which work together to make it function as a whole.
Each block, also called as, unit, stacked top to bottom, starting from Two-factor Authentication(2FA) all the
way to Transactions Unit(T.U) operates within its boundaries. The wallet requires its users to have 2FA enabled 
to perform and take advantage of the units below it.

* __Two-factor Authentication (2FA)__ - Important layer. Pairs user's identity to their respective handled
devices, thereby adding an extra layer of security. All operations happen only after 2FA is enabled.

* __Send-Receive Unit__ - The 'Send' operation works in 2 modes - on-chain & off-chain. This unit is responsible for sending/receiving money within its local/external user base.

* __Purchase Unit__ - Also referred to as Deposit unit. Allows users of the wallet to buy app's assets, virtual currency called as ITD(Internet dollars) against bitcoin, ethereum, litecoin, stripe(USD).

* __Payout Unit__ - Also known as Withdrawals unit, runs as a background job within the wallet ecosystem. Its job is to move funds from user local account into any other external wallet.

* __Know-Your-Customer Unit__ - Manages, controls resources that can be made available to wallet userbase. Comprised of 3-levels, regulates how many send-receive, purchase, payout operations can be performed on daily basis.

* __Transaction Unit__ - Records wallet operations as a transaction.

Payout(Withdrawals) & Purchase(Deposit) Unit Workings:
----------------------------------

For both these units, I aspired to make them fault-tolerant but my lack of know-how about it kept me away from
implementating it. I went ahead to handle code crash/failure events by making each of them save their state before
terminating. How did I achieve this ? - very simple. I watch for SIGTERM, SIGKILL, SIGINT, and SIGUSR2 events
within the units. On next app boot, the app resumes from the state retained in JSON file thus resuming pending
operations before proceeding with new operations in a queue.

The illustration gives self-explainatory guidance on behaviours of the units.

![block\_diagram]({attach}../images/diy/punit.png)

Version 2 update:
=================

On-chain Transactions(txns):
----------------------------
These transactions which happen, get propagated and recorded across blockchain/bitcoin network are called on-chain transactions.
On-chain operation include options for sending equivalent of bitcoin, ethereum, and other cryptocurrencies to external wallet. Typically, for multi-currency support function, one requires cryptocurrency exchange outlet. 


Off-chain Transactions(txns):
-----------------------------
Transactions which circulate within app’s boundaries and persist in app’s own persistent datastore are called off-chain
transactions. Off-chain txns do not tax txn fee when moving funds between users as opposed to on-chain one. But there are limits set on how many off-chain txn can be made per day. 


Q - How to move user’s ITD account’s off-chain balance into on-chain swiftly ? (Note - Just my opinion)
--------------------------------------------------------------------------

* First of all, user files a request saying that ‘transfer x amount from off-chain’s ABC pocket  to on-chain’s XYZ pocket’
* As soon as the request is registered, freeze(block) that x amount from off-chain’s ABC pocket, render the correct balance on refresh.
* The transfer request registered can be automatic, semi-automatic, entirely manual and gets approved from concerned admin.
* If approved, nullify the freezed amount, add x amount into his/her on-chain balance(do this by creating default wallet in
on-chain just like bitgo) and make a transaction entry sideby. 
* For on-chain, multi-currency outlets can be installed as adapters. Just like, as of now, we are/will be working  bitcoin-core,
bitcoin-cash, ripple, moneray, etc.
* On-chain will/can have duplex gateways for moving in/out the funds
