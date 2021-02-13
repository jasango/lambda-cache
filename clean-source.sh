#!/usr/bin/env bash

# getting env
env=$(cat conf/current.env)

sourceBucket=$(cat conf/$env/source-bucket.name)
aws s3 rm s3://$sourceBucket --recursive