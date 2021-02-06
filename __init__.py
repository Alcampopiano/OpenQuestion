#
# This repository is an Anvil app. Learn more at https://anvil.works/
# To run the server-side code on your own machine, run:
# pip install anvil-uplink
# python -m anvil.run_app_via_uplink YourAppPackageName


root_path=__path__[0] # so tests can be found
__path__ = [__path__[0]+"/server_code", __path__[0]+"/client_code"]
__path__.append(root_path)
