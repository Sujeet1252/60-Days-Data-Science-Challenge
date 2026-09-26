# Day 57 — Docker & Deployment Basics

## 📌 Overview

Day 57 focuses on Docker and containerized deployment for a Machine Learning application.

The House Price Prediction Streamlit application developed in Day 56 was packaged into a Docker container containing the required Python environment, dependencies, application code, and trained ML model.

---

## 🎯 Learning Objectives

By completing Day 57, I learned:

- What Docker is
- Why Docker is used
- Docker Images
- Docker Containers
- Dockerfiles
- Docker Engine
- Port mapping
- Docker build process
- Container lifecycle
- Docker logs
- `.dockerignore`
- Docker image tagging
- Containerized Streamlit deployment
- Basic Docker troubleshooting

---

## 🧠 Key Concepts

### Docker

Docker is a platform used to package applications and their dependencies into portable containers.

### Docker Image

An image is a packaged blueprint used to create containers.

### Docker Container

A container is a running instance of a Docker image.

### Dockerfile

A Dockerfile contains instructions used to build a Docker image.

---

## 🏗️ Project

### House Price Prediction — Dockerized Streamlit Application

The Streamlit ML application from Day 56 was containerized using Docker.

### Application Features

- House price prediction
- Area input
- Bedroom input
- Bathroom input
- House age input
- ML model prediction
- Prediction history
- Prediction statistics
- Model information

---

## 🏗️ Architecture

```text
User
 ↓
Browser
 ↓
Docker Host Port
 ↓
Docker Container
 ↓
Streamlit Application
 ↓
Saved ML Pipeline
 ↓
Prediction
