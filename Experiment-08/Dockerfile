# Experiment 08: Simple Dockerfile leveraging official Nginx Alpine image
FROM nginx:alpine

# Metadata labels
LABEL maintainer="Nithyashree D S <2025cs_nithyashreeds_e@nie.ac.in>"
LABEL institute="The National Institute of Engineering, Mysuru"
LABEL experiment="08 - Simple Containers"

# Copy custom application page to default nginx document root
COPY application/index.html /usr/share/nginx/html/index.html

# Expose standard HTTP port
EXPOSE 80

# Start Nginx server in foreground mode
CMD ["nginx", "-g", "daemon off;"]
