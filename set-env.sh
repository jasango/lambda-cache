#!/usr/bin/env bash
if [ $# -eq 0 ]
  then
    echo "You need to pass desa or prod argument..."
     exit 1
  else
    if [ $1 == 'desa' ]
    then
        env="desa"
    else    
        if [ $1 == 'prod' ]
        then
        env="prod"
        else
        echo "Incorrect argument..."
        exit 1
        fi
    fi
fi
echo $env>conf/current.env
