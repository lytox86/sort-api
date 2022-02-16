# sort-api

## Start

### Create virtualenv
Make sure you have a python 3.9.
- If not consider using [pyenv](https://github.com/pyenv/pyenv) or [asdf](https://github.com/asdf-vm/asdf) with the python plugin 

From the project root execute
```shell
pip3 install virtualenv
python3 -m venv ./venv/sort-api
source ./.venv/sort-api/bin/activate
```

### Install dependencies
If you just want to execute the code install production dependencies executing
```shell
pip install -r requirements.txt
```

In case you want to run tests, or contribute in developing the app,
you should install the dev dependencies as well
```shell
pip install -r requirements-dev.txt
```
After that export the python path in order to run the app as a module
```shell
export PYTHONPATH=$PYTHONPATH:`pwd`
```

### Run the app
Start the [uvicorn](https://www.uvicorn.org/) ASGI server in one of these ways: 
Either this
```shell
python -m src.app (or python src/app.py) (or ./src/app.py)
```
or this
```shell
uvicorn src.app:app --reload
```
or this
```shell
docker-compose -f docker_compose.yml up
```
or this
```shell
docker build . -t app
docker run -p 8000:8000 app  
```

### Test the app
You can send requests to the app via an HTTP client like postman or curl.

First of all test the healthiness of the app via
```shell
curl localhost:8000
```
`{"Hello":"World"}` will be printed.

Send sort requests via
```shell
curl --request POST 'localhost:8000/api/v1/sort/quick' --header 'Content-Type: application/json' --data-raw '{"numbers":[3,2,1,0,-1]}'
```
`{"result":[-1,0,1,2,3],"sortingSteps":3}` will be printed.

