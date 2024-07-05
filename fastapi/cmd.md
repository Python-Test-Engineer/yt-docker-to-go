
docker build -t fastapi-test

docker run -it --rm fastapi-test sh   

docker run -it --rm -p 8000:8000 fastapi-test:12