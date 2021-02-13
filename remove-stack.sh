#!/usr/bin/env bash

# getting env
env=$(cat conf/current.env)

# configuration values
stackName=$(cat conf/$env/stack.name) 
storageBucket=$(cat conf/$env/storage-bucket.name)

# clean bucket
aws s3 rm s3://$storageBucket --recursive
# delete stack
aws cloudformation delete-stack --stack-name $stackName