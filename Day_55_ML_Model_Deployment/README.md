# Day 55 - ML Model Deployment

## Overview

Day 55 of my 60-Day Data Science Challenge focused on deploying a trained Machine Learning model as a Flask REST API.

The project demonstrates the complete transition from a trained ML model to a usable prediction service.

## Learning Objectives

- Understand ML model deployment
- Understand training vs inference
- Save trained models
- Load persisted models
- Use Joblib
- Build Scikit-learn pipelines
- Preserve preprocessing during deployment
- Create ML prediction APIs
- Validate API input
- Implement health checks
- Handle API errors
- Test ML APIs using Postman

## Major Project

### House Price Prediction API

A Flask REST API that loads a trained house price prediction pipeline and provides predictions through HTTP requests.

## Architecture

```text
Client
  ↓
Flask REST API
  ↓
Input Validation
  ↓
Saved ML Pipeline
  ↓
Preprocessing
  ↓
Machine Learning Model
  ↓
Prediction
  ↓
JSON Response
