# rps-starter

A Starter Repository for the [Rock Paper Scissors Exercise](https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md).

## Setup

Creating the virtual environment:

```sh
conda create -n rps-env python=3.8
```

Activating the virtual environment:

```sh
conda activate rps-env
```

Installing package dependencies (mainly for testing):
```sh
pip install -r requirements.txt
```

## Usage
Navigating to the repository. For example, if saved in desktop:

```sh
cd ~/Desktop/RPS-HW-1
```

Running the rock paper scissors game (see below for username customization):

```sh
python game.py
```

If user wishes to customize username - if uncustomized, default name is 'Player One':

```sh
PLAYER_NAME="Jon Snow" python game.py
```

## Testing

Running tests:

```sh
pytest
```