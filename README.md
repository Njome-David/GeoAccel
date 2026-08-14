# GeoAccel

Lightweight Python package and GUI for geospatial acceleration modeling and simulation.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Project structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Running the app](#running-the-app)
- [Usage](#usage)
  - [GUI](#gui)
  - [Programmatic / Core API](#programmatic--core-api)
- [Contributing](#contributing)
- [License](#license)
- [Authors](#authors)

## Overview
`GeoAccel` is a compact project for modeling and visualizing acceleration-related computations. It provides a core simulation library under `core/` and a small GUI frontend in `gui/` for interactive exploration.

## Features
- Core physics and acceleration utilities (`core/acceleration.py`).
- Data and model definitions (`core/models.py`).
- Minimal GUI application for visualization and interaction (`gui/app.py`).
- Single-file launcher at project root (`main.py`).

## Project structure
- `main.py` — application entrypoint.
- `requirements.txt` — Python dependencies.
- `core/` — core library modules:
  - `acceleration.py` — acceleration computations and helpers.
  - `models.py` — data models and structures.
- `gui/` — GUI code:
  - `app.py` — GUI application and window setup.
- `assets/` — static assets used by the app (images, icons, etc.).

## Requirements
- Python 3.10+ recommended
- See `requirements.txt` for pinned dependencies

## Installation
Create and activate a virtual environment, then install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## Running the app
From the project root run:

```bash
python main.py
```

This should launch the GUI (implemented in `gui/app.py`)


## Usage

### GUI
- Launch via `python main.py`.

### Programmatic / Core API
You can import core modules from scripts or an interactive REPL:

```python
from core import acceleration, models

# Example: compute an acceleration profile
params = models.SimulationParameters(...)  # adapt to your models
result = acceleration.compute_profile(params)
print(result)
```

Refer to the docstrings in `core/acceleration.py` and `core/models.py` for available functions and classes.


## Contributing
- Fork the repository and create feature branches.
- Open pull requests with clear descriptions and small, focused changes.
- Add tests for new features where appropriate.

## License
This project is licensed under the MIT License.

Copyright (c) 2026 David

## Authors
- Project maintained by repository owner.

