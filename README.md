# Shopee ML Backend

This repository contains the backend implementation for the **Shopee ML** project, which aims to visualize the performances of products in an easy-to-read way. The project also aims to apply machine learning models to give the user predictions regarding future sales performance.

## Features

- **Data Processing Pipelines** for cleaning and preparing the data for ML models.
- **Flask-based RESTful API**: Handles client requests and serves a processed data.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.8 or higher
- `pip` for managing Python packages

## Installation

To install and set up the project locally:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/brebribre/shopee-ml-backend.git
   cd shopee-ml-backend

2. **Activate virtual environment(optional):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
3. **Once installed, you can run the Flask development server by using:**
   ```bash
   flask run
