import anvil
import anvil.server
import anvil.users


if not anvil.get_url_hash():

    while not anvil.users.login_with_form():
        pass

    # disabling report module
    # anvil.open_form('landing.main')
    anvil.open_form("landing.select_action_survey")

else:
    schema = anvil.server.call("get_form", anvil.get_url_hash())
    anvil.open_form("form.main", schema)
