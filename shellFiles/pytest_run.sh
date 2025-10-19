#!/bin/bash

source shellFiles/envSelection.sh

select_env "$1"

echo "Selected Env: $TEST_ENV_FILE"

set -a 
source "$TEST_ENV_FILE"
set +a

echo "Enter the command index:"
echo "1. For logged Execution with HTML report"
echo "2. For Parallel Execution"
echo "3. For Signup Test and Family Addition"
echo "4. for All Scripts "
echo ""
 
read command

if [ "$command" = "1" ]; then
    echo "Enter the log level:"
    read log_level
    echo "Enter the test file:"
    read path

    # echo "DEBUG: log level entered: $log_level"
    # echo "DEBUG: Test file entered: $path"

    pytest -v --log-cli-level="${log_level:-info}" --html=reports/reportSingleRun.html tests/"${path}"


elif [ "$command" = "2" ]; then
    # echo "Max Workers for this local (Prasad) is 12 to locate your count use if its linux npro"
    echo "Enter the thread count:"
    read thread_count
    echo "Enter the test file:" 
    read path

    # echo "DEBUG: Thread count entered: $thread_count"
    # echo "DEBUG: Test file entered: $path"

    pytest -v --html=reports/reportMultiThreadRun.html -n "${thread_count:-3}" -m "not sign_up" tests/"$path" 

elif [ "$command" = "3" ]; then
    echo "Enter the log level:"
    read log_level
    
    pytest -v -m sign_up --html=reports/reportSignupMarker.html --log-cli-level="${log_level:-info}"

elif [ "$command" = "4" ]; then
    # echo "Max Workers for this local (Prasad) is 12 to locate your count use if its linux npro"
    echo "Enter the thread count:"
    read thread_count

    # echo "DEBUG: Thread count entered: $thread_count"
    # echo "DEBUG: Test file entered: $path"

    pytest -v --html=reports/reportAllFiles.html -n "${thread_count:-8}" -m "not sign_up" tests 

else
    echo "Invalid command"
fi