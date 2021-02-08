# Feedback and contribution

Feedback, bug reports, and contributions are welcome via the 
[OpenQuestion GitHub Repository](http://github.com/Alcampopiano/OpenQuestion/).

### Setting up your Git environment

1. Fork the repository on GitHub and clone the fork to you local
machine. For more details on forking see the [GitHub
Documentation](https://help.github.com/en/articles/fork-a-repo).
    
    ```
    $ git clone https://github.com/YOUR-USERNAME/OpenQuestion.git
    ```

2. Create a sync to the original upstream repository by creating a 
[remote](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/configuring-a-remote-for-a-fork).

    ```
    $ git remote add upstream https://github.com/Alcampopiano/OpenQuestion.git
    $ git checkout master
    $ git pull upstream master
    ```

Now you will have all of the updates in the master branch of your local fork.
Note that git will complain if you've committed changes to your local master
branch that are not on the upstream repository. This is one reason why it's good practice to avoid
working directly on your master branch.

### Commiting new code to OpenQuestion

1. Create an issue on GitHub to discuss the changes before you start working on a pull request.

2. Create a new local branch, commit changes to your local branch and push those changes to your github fork:

    ```
    $ git checkout -b <branch-name>
    ```
    
    With this branch checked-out, make the desired changes to the package.
    When you are happy with your changes, you can commit them to a remote branch by running
    
    ```
    $ git add <modified-file>
    $ git commit -m "Some descriptive message about your change"
    $ git push origin <branch-name>
    ```

3. Write a unit test for your code (optional)

    OpenQuestion uses `pytest` for unit testing. To run the test suite,
    first navigate to the "tests" directory then use the `pytest` command from your terminal.

4. Submit a pull request (PR) to merge your new branch to OpenQuestion's master branch

    For details on creating a PR see GitHub documentation [Creating a pull
    request](https://help.github.com/en/articles/creating-a-pull-request). 


### Working with OpenQuestion locally

When working with OpenQuestion locally, it is best to create a virtual environment.

```bash
# inside the OpenQuestion directory
$ venv -m env
$ source env/bin/activate
(env) $ pip install -r requirements.txt
```

To set up the app server you will need to cd into the parent directory. The anvil-app-server expects to find the OpenQuestion folder in the current directory. For trouble shooting check the anvil-app-server docs.

```bash
(env) $ cd ..
(env) $ anvil-app-server --app OpenQuestion --shell
>>> # set up an admin user - follow the instructions in the OpenQuestion docs
(env) $ anvil-app-server --app OpenQuestion
```

The app should be running at `localhost:3030`. You can make changes locally, refresh the app to see those changes.
Note you will now have a `.anvil-data` folder in the parent directory. Deleting this folder will remove all the local data associated with your instance of OpenQuestion.