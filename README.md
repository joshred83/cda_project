# Setting Up the Project

## Prerequisites
- Ensure that you have [Anaconda](https://www.anaconda.com/products/individual) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html) installed on your system.

## Cloning the Repository
First, you need to clone the repository using `git`. If you do not have `git` installed, download it from [Git's official website](https://git-scm.com/downloads).

### Instructions for Windows:
- Open Git Bash and navigate to the desired folder where you want the project to be downloaded.
- Run the following commands:
```bash
git clone https://github.com/joshred83/cda_project/
cd cda_project
```
### Instructions for macOS/Linux:
- Open the Terminal and navigate to the desired folder where you want the project to be downloaded.
- Run the same commands as for Windows.

## Setting Up the Conda Environment
To create a Conda environment with all the required dependencies, use the requirements.yml file in the project directory.

### Instructions for Windows:
- Open Anaconda Prompt and navigate to the project directory.
- Run the following command:
```
conda env create -f requirements.yml
```
### Instructions for macOS/Linux:
- Open the Terminal and navigate to the project directory.
- Run the same command as for Windows.
    - This command creates a new Conda environment named `cda_project` and installs all the necessary packages.

## Activating the Environment
Once the environment has been created, you need to activate it.

### Instructions for Windows:
- In Anaconda Prompt, run:
    ```bash
    conda activate cda_project
    ```
### Instructions for macOS/Linux:
- In the Terminal, run the same command as for Windows.

Depending on your coding setup you may need to take some additional steps to get notebook files using the correct conda environment. If you are using an IDE (like vscode) activating the environment from the commandline should be enough to get your editor using the right kernel. If you are using Jupyter, you will probably need to register the environment with Ipykernel. 
  ```bash
  python -m ipykernel install --user --name cda_project --display-name "Python (cda_project)"
  ```

## Committing Code Changes and Staying Current with the Remote Repository

Working with Git involves regularly committing your code changes to your local repository and synchronizing your work with the remote repository on GitHub. Here's how to do it:

### Committing Your Changes

After making changes to your project, you'll want to save these changes in your local Git repository. Here's the general workflow:

1. **Check the Status of Your Files**: First, see which files you've changed.

    ```
    git status
    ```

2. **Stage Your Changes**: Before committing, you need to stage the changes you want to include in your commit. To stage all changes, use:

    ```
    git add .
    ```

    If you only want to stage specific files, replace `.` with the filenames.

3. **Commit Your Changes**: Now, commit the staged changes to your local repository with a meaningful message.

    ```
    git commit -m "A descriptive message about what you've changed"
    ```

### Pushing Your Changes to the Remote Repository

After committing your changes locally, you'll want to share them with your team by pushing them to the remote repository:

```
git push origin main
```

Replace `main` with the name of the branch you're working on if it's different.

### Staying Current with the Remote Repository

To ensure your local repository is up to date with these changes, pull the latest changes from the remote:

```
git pull origin main
```

Again, replace `main` with your current branch name if necessary.


### Handling Merge Conflicts

You will want to run git pull frequently. Otherwise your local repository can get out of sync and there will be merge conflicts. Those can be a pain to resolve, especially for notebook files. 

This happens because Git cannot automatically reconcile differences between your local changes and the changes in the remote repository. Git will mark the files with conflicts, and you'll need to manually resolve these by editing the files as needed. After resolving conflicts, stage, and commit the resolved files. The locations of conflict markers in the file will help identify what needs resolution. 

### Additional Tips

- Regularly commit your changes and pull from the remote to minimize conflicts.
- Before starting new work, it's a good practice to `git pull` to ensure you're working with the most current version of the project.
- Use branches to keep the work organized and reduce conflicts in the main branch. This is especially important when we're working on the same files or scripts. 


