#! /bin/bash
if [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
    # Do something under GNU/Linux platform
    python3 -m venv legworkENV
    source legworkENV/bin/activate
elif [ "$(expr substr $(uname -s) 1 10)" == "MINGW64_NT" ]; then
    # Do something under GNU/Linux platform
    python -m venv legworkENV
    source legworkENV/Scripts/activate
fi
pip3 install -r requirements.txt