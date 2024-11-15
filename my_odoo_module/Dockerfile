# Use an official Odoo base image
FROM odoo:16.0

# Copy the module to the Odoo addons directory
COPY .. /mnt/extra-addons/docker-based-app

# Set ownership and permissions (adjust user as needed)
RUN chown -R odoo:odoo /mnt/extra-addons/docker-based-app

# Install dependencies
RUN pip install --no-cache-dir -r /mnt/extra-addons/docker-based-app/requirements.txt

# Set the default entrypoint
ENTRYPOINT ["/entrypoint.sh"]
CMD ["odoo"]