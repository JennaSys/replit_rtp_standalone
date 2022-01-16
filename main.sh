# Check to make sure virtual environment has been set up
if [ ! -d "./venv" ]
then
    echo "Running initial setup..." 
    source ./setup.sh
    retVal=$?
    if [ $retVal -ne 0 ]
    then
      exit 1
    fi
fi


# Run application
source ./venv/bin/activate
npm run dev
