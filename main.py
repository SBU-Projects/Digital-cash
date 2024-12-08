from functions.initialization import Initialization
from functions.bank import Bank
from functions.spender import Spender

init1 = Initialization(28871271685163)
bank1 = Bank("Dr.Ziba Eslami", init1.get_public_arguments())
spender1 = Spender("Sajjad", init1.get_public_arguments())

print(bank1.creating_coin_bank("gw-betha", [1]))
"""
print(bank1.get_conected_spenders())
spender1.connect_with_bank(bank1)
print(bank1.get_conected_spenders())
"""
