# Day 56 - Streamlit ML Application

## Overview

Day 56 of my 60-Day Data Science Challenge focused on building an interactive Machine Learning application using Streamlit.

The project extends the ML model deployment work from Day 55 by providing a user-friendly web interface for house price prediction.

## Project

### House Price Prediction Streamlit Application

The application allows users to enter house characteristics and receive a predicted house price from a trained Machine Learning pipeline.

## Learning Objectives

- Understand Streamlit
- Build interactive ML applications
- Create Streamlit input widgets
- Load saved ML models
- Use Streamlit caching
- Validate user input
- Generate ML predictions
- Display prediction results
- Use Streamlit layouts
- Use columns and metrics
- Use sidebar controls
- Maintain session state
- Build prediction history
- Create simple ML dashboards

## Application Architecture

```text
User
 ↓
Streamlit Interface
 ↓
Input Validation
 ↓
Pandas DataFrame
 ↓
Saved ML Pipeline
 ↓
Preprocessing
 ↓
Regression Model
 ↓
Prediction
 ↓
Streamlit Result
