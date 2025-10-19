#!/bin/bash

select_env() {
    local env="$1"

    if [ -z "$env" ]; then
        echo "Please Select the env test / staging / prod"
        read env
    fi 

    env=${env:-test}

    case $env in
        test)
            export TEST_ENV_FILE=".config/.test.env"
            ;;
        staging)
            export TEST_ENV_FILE=".config/.pre-prod.env"
            ;;
        prod)
            export TEST_ENV_FILE=".config/.prod.env"
            ;;
        *)
            echo "Invalid selection. Defaulting to test."
            export TEST_ENV_FILE=".config/.test.env"
            ;;
    esac

}