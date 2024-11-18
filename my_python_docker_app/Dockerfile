# Dockerfile
# Docker configuration for your Odoo app.
FROM odoo:16.0

COPY . /mnt/extra-addons/my_python_docker_app

RUN pip install --no-cache-dir -r /mnt/extra-addons/my_python_docker_app/requirements.txt

ENTRYPOINT ["python3", "/mnt/extra-addons/my_python_docker_app/app.py"]
