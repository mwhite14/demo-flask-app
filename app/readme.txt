docker buildx create --use
docker buildx build --platform linux/amd64,linux/arm64 -t 365290772959.dkr.ecr.us-east-2.amazonaws.com/flask_app:latest --push .
