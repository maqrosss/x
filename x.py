from tronpy import Tron
from tronpy.keys import PrivateKey
from tronpy.providers import HTTPProvider
from tronpy.contract import Contract

# Connect to the TRON network (mainnet or testnet)
full_node = HTTPProvider("https://api.trongrid.io")
solidity_node = HTTPProvider("https://api.trongrid.io")
event_server = HTTPProvider("https://api.trongrid.io")
client = Tron(full_node)

# Replace with your private key
private_key = PrivateKey(bytes.fromhex("0"))

# Define the USDT contract address
usdt_contract_address = "0"

# Create a Contract instance for the USDT contract
usdt_contract = Contract(client=client, addr=usdt_contract_address)

# Define the recipient address and the amount of USDT to send (in SUN)
recipient_address = "0"
usdt_amount = 100000  # 1 USDT (in SUN)

# Build the USDT transfer transaction
transfer_txn = (
    usdt_contract.functions.transfer(recipient_address, usdt_amount)
    .with_owner(private_key)
    .build()
)

# Sign and broadcast the transaction
signed_txn = client.trx.sign(transfer_txn)
tx_id = signed_txn.txid
response = client.trx.broadcast(signed_txn)
receipt = response.wait()

print(f"Transaction ID: {tx_id}")
print(f"Transaction Receipt: {receipt}")
