#!/usr/bin/env bash
# AirBnB Clone Test and Style Check Script

# Requirements
# Please ensure that the following packages are installed before running the script:
# - pycodestyle version 2.7.0
# - pep8 version 1.7.0

## Code tests
# This section runs the unit tests for the AirBnB Clone project in both interactive and non-interactive modes.
# It first executes the unit tests for the FileStorage module, followed by the unit tests for the DBStorage module.
# The environment variables are set accordingly to facilitate the testing process.
echo -e "\e[104m Running Unit Tests [FileStorage] \e[0m\e[33m"
env HBNB_MYSQL_USER="" \
    HBNB_MYSQL_HOST="" \
    HBNB_MYSQL_DB="" \
    HBNB_ENV="test" \
    HBNB_TYPE_STORAGE="file" \
    HBNB_MYSQL_PWD="" \
    'python3' '-m' 'unittest' 'discover' 'tests' \
&& echo -e "\e[0m\e[104m Running Unit Tests [DBStorage] \e[0m\e[33m" \
&& env HBNB_MYSQL_USER="hbnb_test" \
    HBNB_MYSQL_HOST="localhost" \
    HBNB_MYSQL_DB="hbnb_test_db" \
    HBNB_ENV="test" \
    HBNB_TYPE_STORAGE="db" \
    HBNB_MYSQL_PWD="hbnb_test_pwd" \
    'python3' '-m' 'unittest' 'discover' 'tests'

# Check the exit status of the previous command to determine if the tests passed or failed.
[ "$(echo -n $?)" == "0" ] && echo -ne "\e[100m\e[32m PASSED "
echo -e "\e[0m"

## Python code style checks
# This section performs code style checks on the Python files in the project.
# It first retrieves a list of all Python files in the current directory and its subdirectories.
# The pycodestyle command is then used to check the style of the code, followed by the pep8 command.
# If both checks pass without any issues, the script displays a "PASSED" message.
echo -e "\e[104m Running Style Checks \e[0m\e[31m"
Src_Files="$(find . -type f -regex '.*.py' | tr '\n' ' ')"
# shellcheck disable=SC2086
pycodestyle $Src_Files
if [[ "$(($? + 0))" == "0" ]]; then
    # shellcheck disable=SC2086
    ~/.local/bin/pep8 $Src_Files
    [ "$(echo -n $?)" == "0" ] && echo -ne "\e[100m\e[32m PASSED "
fi
echo -ne "\n\e[0m"
