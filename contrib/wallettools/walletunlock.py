from jsonrpc import ServiceProxy
access = ServiceProxy("http://127.0.0.1:32152")
pwd = raw_input("Enter wallet passphrase: ")
access.walletpassphrase(pwd, 60)
