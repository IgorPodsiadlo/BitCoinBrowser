import time
from tkinter import *
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

# Funkcja do pobierania i wyświetlania informacji o blokach
def get_block_info():
    try:
        block_hash = block_hash_entry.get().strip()
        if not block_hash:
            raise ValueError("Please enter a valid block hash.")

        # Pobierz informacje o bloku na podstawie podanego hash
        block_info = rpc_connection.getblock(block_hash)
        block_info_var.set(f"Block info: {block_info}")
        time.sleep(1)

        # Przykładowe pobieranie transakcji z bloku
        tx_list = block_info['tx']
        tx_list_var.set(f"Transactions in the block: {tx_list}")
        time.sleep(1)

    except JSONRPCException as e:
        block_info_var.set(f"An error occurred: {e}")
    except ValueError as e:
        block_info_var.set(str(e))

# Konfiguracja RPC
rpc_user = "ogor1"
rpc_password = "admin"
rpc_port = 18332
rpc_host = "localhost"

# Połączenie z Bitcoin Core za pomocą AuthServiceProxy
rpc_url = f"http://{rpc_user}:{rpc_password}@{rpc_host}:{rpc_port}"
rpc_connection = AuthServiceProxy(rpc_url)

# Konfiguracja GUI
root = Tk()
root.title("Bitcoin Block Explorer")

Label(root, text="Enter block hash:").pack()

block_hash_entry = Entry(root, width=50)
block_hash_entry.pack()

block_info_var = StringVar()
tx_list_var = StringVar()

Label(root, textvariable=block_info_var, wraplength=500).pack()
Label(root, textvariable=tx_list_var, wraplength=500).pack()

Button(root, text="Get Block Info", command=get_block_info).pack()

root.mainloop()
