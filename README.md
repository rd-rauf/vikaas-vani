# VikasVaani

CONTAINER DEPLOYMENT:

Build:
docker build -t raufabdul/vikaas-vani:v4 --platform=linux/amd64 .

Push:
docker push raufabdul/vikaas-vani:v4

Run:
docker run --privileged -d -p 8000:8000 raufabdul/vikaas-vani:v4
