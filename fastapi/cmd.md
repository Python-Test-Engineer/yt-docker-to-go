docker build -t fastapi-docs . 

docker run -d --name fastapi-test -p 80:80 fastapi-docs

http://127.0.0.1/docs

http://localhost/

http://localhost/items/2