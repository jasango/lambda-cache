#!/usr/bin/env bash
rm -rf output/
git add --all
commit=$(date +"%m-%d-%y-%H-%M")
git commit -m "lambda-cache: serverless memory service $commit"
git push