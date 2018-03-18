# Srt synchronizer

requires Python3.6+

## Purpose
Flask web app whose purpose is to help you offset your desynchronized files easily by selecting files from your computer 
or directly by enter the content to offset.
You can pass any value that you want in the offset. If you want to offset your subtitles
by 1 hour but only using seconds or minutes it should work.

## Clone the project  
    git clone git@github.com:sorasful/srt-synchronizer.git

## Run on local machine
  ### Install dependencies (with virtualenv)
    cd srt-synchronizer/
    virtualenv -p python3 venv
    source venv/bin/activate
    pip install -r requirements.txt
  ### Run it 
    python app.py
    
## Run on docker
    cd srt-synchrosizer/
    docker build -t srt-synchronizer .
    docker run -d -p 5000:5000

Then go to `http://localhost:5000/`

## Run tests
    pytest

## Todos : 

- Handle unicode error
- Add drag&drop zone