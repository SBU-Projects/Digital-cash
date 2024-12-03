from functions.initialization import Initialization
from functions.bank import Bank

init1 = Initialization(28871271685163)
print(init1.get_public_arguments())
print(init1.get_private_arguments())

bank1 = Bank("Dr.Ziba Eslami", init1.get_public_arguments())
