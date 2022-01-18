# React to Python: Standalone example

[![Run on Repl.it](https://repl.it/badge/github/JennaSys/replit_rtp_standalone)](https://repl.it/github/JennaSys/replit_rtp_standalone)

To generate the development JavaScript bundle, run `. ./build-dev.sh` in the shell.  After that, you can also run `npm run bul` in the shell to generate the production JavaScript bundle.

Running the repl will serve up the pre-generated JavaScript files.

### Setup
The first time you run the `build-dev.sh` script, it will check for installed dependencies.  If not found, it will do the following:  
- Install Python 3.9 (required by Transcrypt)
- Install Python dependencies
- Install JavaScript dependencies

Once that is done, it will transpile and bundle the generated JavaScript files and then launch a development server. The development server can be stopped with `Ctrl-c`.

