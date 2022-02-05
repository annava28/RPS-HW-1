# rps-starter

A Starter Repository for the [Rock Paper Scissors Exercise](https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md).

## Setup

Create a virtual environment:
No need to create a specific virtual environment! This program runs on the "base" environment. 

```sh
conda create -n rps-env python=3.8
```

Activate the virtual environment:

```sh
conda activate rps-env
```
## Usage

Install package dependencies (mainly for testing):
Navigate to the repository. For example, if saved in desktop:

```sh
pip install -r requirements.txt
cd ~/Desktop/RPS-HW-1
```

## Usage

Run the rock paper scissors game:

```sh
python game.py
```

## Testing

Run tests:

```sh
pytest
```