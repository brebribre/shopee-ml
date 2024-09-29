# Shopee ML Backend

This repository contains the backend implementation for the **Shopee ML** project, which focuses on applying machine learning models to predict sales and improve performance analytics for Shopee, an e-commerce platform. The backend is built using Python and Flask, and it provides the necessary API endpoints to support the machine learning models and data processing tasks.

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
