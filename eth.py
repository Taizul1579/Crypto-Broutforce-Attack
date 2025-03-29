import time
import requests
from mnemonic import Mnemonic
from eth_account import Account
Account.enable_unaudited_hdwallet_features()

from web3 import Web3

# Infura API Key
INFURA_API_KEY = "fab929f397ef4fd69d13602fed1fb591"
INFURA_URL = f"https://mainnet.infura.io/v3/{INFURA_API_KEY}"

# Web3 instance
w3 = Web3(Web3.HTTPProvider(INFURA_URL))


def generate_wallet():
    """ নতুন Ethereum Wallet তৈরি করে """
    mnemo = Mnemonic("english")
    mnemonic_phrase = mnemo.generate(strength=128)  # 12-word phrase
    seed = mnemo.to_seed(mnemonic_phrase)
    acct = Account.from_mnemonic(mnemonic_phrase)

    return mnemonic_phrase, acct.address


def check_balance(address):
    """ Ethereum Wallet-এর ব্যালেন্স চেক করে """
    balance_wei = w3.eth.get_balance(address)
    balance_eth = w3.from_wei(balance_wei, 'ether')
    return balance_eth


while True:
    # নতুন ওয়ালেট তৈরি
    phrase, eth_address = generate_wallet()
    print(f"Checking Wallet: {eth_address}")

    # ব্যালেন্স চেক
    balance = check_balance(eth_address)
    print(f"Balance: {balance} ETH")

    # যদি ব্যালেন্স থাকে, তাহলে Mnemonic Phrase দেখাও
    if balance > 0:
        print("\n🎉 Valid Wallet Found!")
        print(f"Mnemonic Phrase: {phrase}")
        print(f"Ethereum Address: {eth_address}")
        print(f"Balance: {balance} ETH")
        break  # প্রোগ্রাম বন্ধ

    # ব্যালেন্স না থাকলে কিছুক্ষণ অপেক্ষা করে আবার চেষ্টা করো

