Title: Keywo's Auto Withdrawal system [on-going]
Date: 2016-12-03 14:09
Slug: auto-withdrawal
Summary: Auto Withdrawal system makes mass payouts against qualified withdrawal requests by propagating them through programmed software policies. Doing this offloaded laborious task, to some extend, performed by humans

Wallet Anatomy:
-----------------

![block\_diagram]({attach}../images/diy/wallet_as_a_whole.png)

Above diagram displays the wallet's building blocks, which work together to make it function as a whole.
Each block, also called as, unit, stacked top to bottom, starting from Two-factor Authentication(2FA) all the
way to Transactions Unit(T.U) operates within its boundaries. The wallet requires its users to have 2FA enabled 
to perform and take advantage of the units below it.

* __Two-factor Authentication (2FA)__ - Important layer. Pairs user's identity to their respective handled
devices, thereby adding an extra layer of security. All operations happen only after 2FA is enabled.

* __Send-Receive Unit__ - This unit is responsible for sending/receiving money within its local user base.

* __Purchase Unit__ - Allows users of the wallet to buy app's assets, virtual currency called as ITD(Internet dollars) against bitcoin, ethereum, litecoin, stripe(USD).

* __Payout Unit__ - Runs as background job within the wallet ecosystem, responsible for processing mass send transfers.

* __Know-Your-Customer Unit__ - Manages, controls resources that can be made available to wallet userbase. Comprised of 3-levels, regulates how many send-receive, purchase, payout operations can be performed on daily basis.

* __Transaction Unit__ - Records wallet operations as a transaction. Leverages MongoDB for data persistence.

Payout & Purchase Unit Workings:
----------------------------------

For both these units, I aspired to make them Fault-tolerant but my lack of know-how about it kept me away from
implementating it. I went ahead to code crash/failure events by making each of them save their state before
terminating. How did I achieve this ? - very simple. I watch for SIGTERM, SIGKILL, SIGINT, and SIGUSR2 events
within the units. On next app boot, the app resumes from the state retained in JSON file thus resuming pending
operations before proceeding with new operations in a queue.

The illustration gives self-explainatory guidance on behaviours of the units.

![block\_diagram]({attach}../images/diy/punit.png)
