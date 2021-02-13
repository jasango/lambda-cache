#!/usr/bin/env bash

# getting env
env=$(cat conf/current.env)

storageBucket=$(cat conf/$env/storage-bucket.name)
aws s3 rm s3://$storageBucket --recursive