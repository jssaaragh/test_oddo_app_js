# README.md

# My Python Docker App
A FastAPI CRUD app integrated with Odoo and deployed via Docker.

## Key Features
- Full CRUD operations using FastAPI.
- PostgreSQL database integration.
- Pre-configured for Docker and Docker Compose.

## Installation
Follow the standard Odoo app installation process.

<img src="static/description/icon.png" alt="App Icon" width="128">

This module is a basic example for creating an Odoo app that can be listed on the Odoo Marketplace. It includes:
- A model (`my.docker.model`) with name and description fields.
- A controller for a basic "Hello, world" webpage.
- Tree and form views for managing records.
- Docker configuration (Dockerfile and docker-compose.yml) for deploying the app.

## Installation
1. Clone or download the module into your Odoo `addons` directory.
2. Ensure your SSH configuration is set up for `git`.
3. Update the module list: `odoo -u all`.
4. Install the module via the Odoo Apps menu.