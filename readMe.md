This project was created as a school project wherein the goal was to use multiple programming languages to learn how they communicate with each other. Communication methods for this project consist of REST api to send data from a web page to a Flask server, and use of a shared object file to call C code from a python script.

To run with Docker:
    
    docker build -t flaskapp.
    
    docker run --publish 5000:5000 --detach --name app flaskapp

    open up a web browser and navigate to "localhost:5000"

To run outside of Docker:
    
    python app.py

Python libraries used:
    
    flask
    plotly

Command to get new .so file (to apply changes to c file)
    
    cc -fPIC -shared -o tinyexpr.so tinyexpr.c
    
    must be uesd if any changes are made to tinyexpr.c. replace current version in static folder with this


languages used:
    
    Python: using flask as a server to host the webpage, as well as plotly to generate graphs
    Javascript: adds functionality to the webpage such as typing in the calculator and sending data back to the Flask server
    C: calculates the values for the graph. While fairly simple examples are provided C is theoretically able to perform advanced calculations much faster than the other languages used
