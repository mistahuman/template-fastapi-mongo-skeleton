# template-fastapi-motor-skeleton
![Python3.13](https://img.shields.io/badge/Python-3.13-brightgreen.svg?style=flat-square)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115.8-brightgreen.svg?style=flat-square)
![Motor](https://img.shields.io/badge/Motor-3.7.0-brightgreen.svg?style=flat-square)
![Svelte](https://img.shields.io/badge/Svelte-4.2.7-brightgreen.svg?style=flat-square)
![Skeleton](https://img.shields.io/badge/Skeleton-v2-brightgreen.svg?style=flat-square)

## Introduction
A simple template for building applications with [FastAPI](https://fastapi.tiangolo.com/), [Motor](https://motor.readthedocs.io/), and [MongoDB](https://www.mongodb.com/) on the backend, and [SvelteKit](https://kit.svelte.dev/) with [Skeleton.dev](https://www.skeleton.dev/) on the frontend.

## Prerequisites
Before running the project, ensure you have the following installed on your system:
- python
- npm
- make

## Installation
To set up the project, follow these steps:
1. Sign in (or sign up) MongoDB Atlas and create a database. After that, save connection string and copy to MONGO_URI into env files.

2. Set up enviroments files (i.e. env.sample) in fastapi and ui for local and production:
   ```sh
   cp env.sample .env.production 
   cp env.sample .env
   ```

3. Install dependencies and set up the virtual environment using Makefile:
   ```sh
   make install
   ```

## Getting Started
Manage the application using Make commands:

- Show available commands:
  ```sh
  make help
  ```
- Start development:
  ```sh
  make dev
  make ui
  ```
- Start the web application with docker-compose:
  ```sh
  make run
  ```
- Stop the web application:
  ```sh
  make stop
  ```
- Run tests with pytest:
  ```sh
  make test
  ```
