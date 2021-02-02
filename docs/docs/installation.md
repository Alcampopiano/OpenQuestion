# Installation

OpenQuestion is available from the Python Package Index and can be installed using `pip`. 

```
pip install OpenQuestion
```

## Adding developers and administrators as users
Before OpenQuestion's GUI can be used, survey developers and app administrators must be added as 
registered users to the app's database. This is described in the following 
sections (click [here](faq.md#can-i-change-the-default-authentication-services-for-admins) 
for more information on the available authentication services).

From the command line (where the OpenQuestion is below the current directory) run the app server 
with the `--shell` option. This will drop you into a Python interpreter that is 
connected to OpenQuestion's database.

```
anvil-app-server --app OpenQuestion --shell
```

Now add a user (i.e., a survey developer and/or app administrator) and, depending on the desired authentication 
service, set a password. 

```python
# add a new row to the Users table
new_user=app_tables.users.add_row(email='your_username@example.com', enabled=True)

# these steps are not needed if using Google or Microsoft Authentication
import bcrypt
password_hash = bcrypt.hashpw(b'new password', bcrypt.gensalt(16))
new_user['password_hash'] = password_hash.decode()
```

## Launching OpenQuestion
Now that OpenQuestion has been installed, and there are one or more valid users (i.e., developers and admins),
the following command will launch the app which will prompt the user for 
their authentication details associated with the previous step.

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

