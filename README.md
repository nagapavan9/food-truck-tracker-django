# Food Trucks Tracker

![demo](https://github.com/nagapavan9/food-truck-tracker-django/assets/41633095/98a254ab-1bff-4efa-a2e2-fd22103f12a1)

## 📝 Description
**Food Trucks Tracker** 
Food Truck Tracker is your ultimate guide to savoring the best street eats San Francisco has to offer, right at your fingertips.

<details><summary><b>Folder Structure</b></summary>

```bash
food_truck_tracker/
├── food_truck/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── startup_service.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/
│   │   └── __init__.py
│   ├── data/
│   └── static/
│       └── templates/
├── food_truck_tracker/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── db.sqlite3
│   ├── manage.py
│   ├── .gitignore
│   ├── Dockerfile
│   ├── bgdal_installation.txt
│   ├── poetry.lock
│   ├── pyproject.toml
│   └── README.md
├── templates/
│   ├── food_truck_list.html
└── static/
    ├── styles.css
    └── food_truck_bg.jpg
```
</details>

## 📖 Table of Contents

<details><summary>Table of Contents</summary>

- [Description](#-description)
- [Technologies Used](#-technologies-used)
- [Get Started](#-get-started)
  - [Prerequisites](#-prerequisites)
  - [Installation and Run Locally](#-installation-and-run-locally)
- [Environment Variables](#-environment-variables)
- [Contributing](#-contributing)
</details>

## ✨ Technologies Used

<details><summary><b>Food Trucks Tracker</b> is built using the following technologies:</summary>

- [Python](https://www.python.org/): Python is a programming language that lets you work quickly and integrate systems more effectively.
- [Django](https://www.djangoproject.com/): Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.
- [Django REST framework](https://www.django-rest-framework.org/): Django REST framework is a powerful and flexible toolkit for building Web APIs in Django.
- 
</details><br/>

[![Technologies Used](https://skillicons.dev/icons?i=python,django,djangorestframework)](https://skillicons.dev)

## 🧰 Get Started

To get this project up and running in your development environment, follow these step-by-step instructions.

### 📋 Prerequisites

In order to install and run this project locally, you would need to have the following installed on your local machine.

- [Python](https://www.python.org/) (3.x recommended)
- [Django](https://www.djangoproject.com/)
- [Poetry](https://python-poetry.org/)
- [Git](https://git-scm.com/downloads)

### ⚙️ Installation and Run Locally

**Step 0:**

> [!IMPORTANT]
> - The application requires a specific version of Python and GDAL. Start by creating a Conda environment with the required Python version.
> - GDAL binaries compatible with your Python version and OS can be found [here](https://github.com/cgohlke/geospatial-wheels/releases). Download the appropriate GDAL binary for your system.
> - Install the GDAL binary in your Conda environment using pip.
> - Set the necessary environment variables in settings.py to configure GDAL and GEOS paths based on their locations within your Conda environment.

**Detailed Steps:**
- *Create a Conda Environment:*
   - Open your terminal and create a new Conda environment by running:
```bash
conda create -n food_truck_tracker python=3.10.14
```
   - Activate the environment:
```bash
conda activate food_truck_tracker
```
- *Download and Install GDAL:*
  - Find the unofficial GDAL binaries compatible with your Python version and OS from the [Geospatial Wheels page](https://github.com/cgohlke/geospatial-wheels/releases).
  - Download the appropriate binary for GDAL.
  - Install the binary within your Conda environment:
```bash
python -m pip install <path-to-your-downloaded-gdal-binary>
```
- *Create a Conda Environment:*
  - Navigate to your Conda environment directory to find the GDAL and GEOS library files:
```bash
cd C:\ProgramData\miniconda3\envs\food_truck_tracker
dir /s /b gdal*.dll
```
   - Copy the path output from the command above and set it in your settings.py:
```bash
GDAL_LIBRARY_PATH = r"C:\ProgramData\miniconda3\envs\food_truck_tracker\Lib\site-packages\osgeo\gdal.dll"
os.environ["GDAL_LIBRARY_PATH"] = GDAL_LIBRARY_PATH
```
  - Similarly, find the GEOS library path:
```bash
dir /s /b geos*.dll
```
  - Set the GEOS library path in your settings.py:
```bash
GEOS_LIBRARY_PATH = r'C:\ProgramData\miniconda3\envs\food_truck_tracker\Lib\site-packages\osgeo\geos_c.dll'
os.environ["GEOS_LIBRARY_PATH"] = GEOS_LIBRARY_PATH
```
**Step 1:**

Download or clone this repo by using the link below:

```bash
git clone https://github.com/nagapavan9/food-truck-tracker-django.git
```

**Step 2:**

Navigate to the project directory:

```bash
cd <project_directory>
```
**Step 3:**

Execute the following command in the root directory of the downloaded repo in order to install dependencies:

```bash
poetry install
```

**Step 4:**

Execute the following command in order to run the development server locally:

```bash
python manage.py runserver
```

**Step 5:**

Open [http://localhost:8000](http://localhost:8000) with your browser to see the result.

## 🔒 Environment Variables

Environment variables can be used for configuration. They must be set before running the app.

> [Environment variables](https://en.wikipedia.org/wiki/Environment_variable) are variables that are set in the operating system or shell, typically used to configure programs.


## 🔧 Contributing

[![contributors](https://contrib.rocks/image?repo=nagapavan9/food-truck-tracker-django)](https://github.com/nagapavan9/food-truck-tracker-django/graphs/contributors)

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.