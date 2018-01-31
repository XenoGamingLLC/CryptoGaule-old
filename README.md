CryptoGaule Script Blockchain 
================================

http://www.cryptogaule.fr

Copyright (c) 2009-2014 Bitcoin Developers

Copyright (c) 2011-2014 CryptoGaule Developers

What is CryptoGaule?
----------------

CryptoGaule is a lite version of Bitcoin using scrypt as a proof-of-work algorithm.
Block reward

500

Block Reward Halving Rate

120,000

Premine

30 000 000

Total Coins

150 000 000


Coinbase maturity
20
Number of blocks before a mined block can be spend.

-----------------------------
Number of confirmations
6
Number of blocks before a transaction is confirmed.

-------------
Target timespan in minutes
10
Number of minutes before difficulty of the network is re-adjusted.

--------------------
Target spacing in minutes
5
Number of minutes it should take to mine a block.

CryptoGaule is an experimental digital currency that enables instant payments to anyone, anywhere in the world. CryptoGaule uses peer-to-peer technology to operate with no central authority: managing transactions and issuing money are carried out collectively by the network. CryptoGaule Core is the name of open source software which enables the use of this currency.

For more information, as well as an immediately useable, binary version of the CryptoGaule Core software, see httpss://cryptogaule.fr.
License

CryptoGaule Core is released under the terms of the MIT license. See COPYING for more information or see https://opensource.org/licenses/MIT.
Development Process

The master branch is regularly built and tested, but is not guaranteed to be completely stable. Tags are created regularly to indicate new official, stable release versions of CryptoGaule Core.

The contribution workflow is described in CONTRIBUTING.md.

The developer mailing list should be used to discuss complicated or controversial changes before working on a patch set.

Developer IRC can be found on Freenode at #litecoin-dev.
Testing

Testing and code review is the bottleneck for development; we get more pull requests than we can review and test on short notice. Please be patient and help out by testing other people's pull requests, and remember this is a security-critical project where any mistake might cost people lots of money.
Automated Testing

Developers are strongly encouraged to write unit tests for new code, and to submit new unit tests for old code. Unit tests can be compiled and run (assuming they weren't disabled in configure) with: make check

There are also regression and integration tests of the RPC interface, written in Python, that are run automatically on the build server. These tests can be run (if the test dependencies are installed) with: qa/pull-tester/rpc-tests.py

The Travis CI system makes sure that every pull request is built for Windows, Linux, and OS X, and that unit/sanity tests are run automatically.
Manual Quality Assurance (QA) Testing

Changes should be tested by somebody other than the developer who wrote the code. This is especially important for large or high-risk changes. It is useful to add a test plan to the pull request description if testing the changes is not straightforward.
Translations

We only accept translation fixes that are submitted through Bitcoin Core's Transifex page. Translations are converted to CryptoGaule periodically.

Translations are periodically pulled from Transifex and merged into the git repository. See the translation process for details on how this works.

Important: We do not accept translation changes as GitHub pull requests because the next pull from Transifex would automatically overwrite them again.



