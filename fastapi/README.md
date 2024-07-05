# Hot reload of FastAPI

Version no longer required in compose file.

`compose.yaml` can replace `docker-compose.yaml` as default compose file.

### Tested 02JUL2024

Based on https://www.youtube.com/watch?v=CzAyaSolZjY but I have split COPY into first time just requirements.txt to cache this and then another copy for rest of files. This prevents reinstalling requirments on rebuild when only the code changes.

non docker CLI: `uvicorn main:app --reload --port=8000 --host=0.0.0.0`

`http://localhost:8000/` not `http://0.0.0.0:8000` even though:

```
INFO: Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)` as per console
```

It will watch for changes as show in logs:
```
INFO:     Will watch for changes in these directories: ['C:\\Users\\mrcra\\Desktop\\YT\\yt-docker-to-go\\fastapi']
```

## Docker commands

First time run `docker compose up --build` to build image

Then next time `docker compose up` is fine

You will see in console `fastapi-web-1  | WARNING:  WatchFiles detected changes in 'main.py'. Reloading...` when you change main.py as hot reloading is active due to bind mount and the --reload flag in sh command.

Changes to .env file are not detected seemingly so one will need to rebuild. These do not change often unlike code.

## Multistage

Copy contents of `DockerfileMultiStage` to `Dockerfile` and repeat steps.

`docker run -it --rm fastapi-test sh` opens shell.

`ls`
`cat test.txt` will display contents of artifact created in dev part of multistage build and copied into dev stage.

A dangling image `none` is created.

This can be removed with `docker image prune` in CLI or in a script.