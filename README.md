# Audiobook CLI
This project is a CLI command with the objective of taking a pdf file and reading the content to the user.

## Requirements

- Python3

## Instalation

#### Create a virtual environment

```
python -m venv venv
```

#### Initialize the virtual environment

##### Windows

```
./venv/Scripts/activate
```

##### Mac

```
source venv/bin/activate
```

#### Install requirements

```
pip install -r requirements.txt
```

## Run the app

To run the app, you need a book imported into your `books` folder. Then you can reference the name in the CLI command below to read it, alog with the start and end pages.

```
flask read <NAME OF THE BOOK> 1 10
```
