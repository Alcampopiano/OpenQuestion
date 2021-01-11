# Installation

OpenQuestion is available from the Python Package Index and can be installed using `pip`. 

```
pip install OpenQuestion
```

## Adding developers as users
Before OpenQuestion can be used, developers must be added as registered users to the app's database. 
This is described in the following sections (click [here]() for more information on the
available authentication services).

### Accessing OpenQuestion's Python Shell
From the command line (where the OpenQuestion is below the current directory) run the app server 
with the `--shell` option. This will drop you into a Python interpreter that is 
connected to OpenQuestion's database.

```
anvil-app-server --app OpenQuestion --shell
```

Now add yourself as a user and, depending on the desired authentication 
service, give yourself a password. 

```python
# add a new row to the Users table
new_user=app_tables.users.add_row(email='your_username@example.com', enabled=True, admin=True)

# these steps are not needed if using Google or Microsoft Authentication
import bcrypt
password_hash = bcrypt.hashpw(b'new password', bcrypt.gensalt(16))
new_user['password_hash'] = password_hash.decode()
```

For more information on how to interact with the app's database using code, please click [here]().

## Launching OpenQuestion
Now that OpenQuestion has been installed, and you have added yourself as a user,
the following command will launch the app and you can sign in with the 
username and password associated with the previous step.

```
anvil-app-server --app OpenQuestion
```

## Cloud deployment
OpenQuestion is built using the open source [Anvil App Server](https://anvil.works/open-source).
If you would like more information on how to deploy OpenQuestion on the cloud, Anvil has put together
excellent how-to guides:

- [Amazon Lightsail](https://anvil.works/docs/how-to/app-server/cloud-deployment-guides/aws-lightsail-app-server-deployment)
- [Microsoft Azure](https://anvil.works/docs/how-to/app-server/cloud-deployment-guides/azure-app-server-deployment)
- [DigitalOcean Droplet](https://anvil.works/docs/how-to/app-server/cloud-deployment-guides/digitalocean-app-server-deployment)
- [Google Compute Engine](https://anvil.works/docs/how-to/app-server/cloud-deployment-guides/google-cloud-app-server-deployment)
- [Linode](https://anvil.works/docs/how-to/app-server/cloud-deployment-guides/linode-app-server-deployment)

