# Simple Python Test Application

## Run locally in VSCode

Super ddetailed instructions
1. Start vscode in this folder with - code .
2. Create an environment - <ctrl><shift>P
3. Install Flash - python3 -m pip install flask
4. Run app - python3 -m flask run

## Run in a docker container

1. git clone https://github.com/davidmattice/flask-testing.git
2. docker build --tag flask-testing .
3. docker run -d -p 5001:5000 --name flask-testing flask-testing
4. docker stop flask-testing;docker rm flask-testing
