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