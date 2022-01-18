echo "Checking Python version..."
python3.9 --version
retVal=$?
if [ $retVal -ne 0 ]
then
    echo "Running initial setup..." 
    source ./setup.sh
    retVal=$?
    if [ $retVal -ne 0 ]
    then
      exit 1
    fi
fi

# echo
# echo "Building application..."
# python3.9 -m transcrypt 
# npm start
# npm run build

# echo
# echo "Starting dev server"
# npm run dev

