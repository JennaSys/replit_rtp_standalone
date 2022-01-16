# React to Python: Standalone example

### Setup
The first time you run the repl, it will perform an initial setup routine that:  
- Creates a Python virtual environment
- Installs Python dependencies
- Installs JavaScript dependencies

Once that is done, it will transpile and bundle the generated JavaScript files and then launch a proxy server. The `dev-server.js` file can be modified as required to suit your needs.

If you've forked the repl and the build is crashing saying that the transcrypt module can't be found, delete the `venv/` folder and try running the repl again.  This will force the Python dependencies to be reinstalled.

