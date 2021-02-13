#!/usr/bin/env bash

# getting env
env=$(cat conf/current.env)

sourceBucket=$(cat conf/$env/source-bucket.name) 

templateName="output/template-temp.json" 
outputTemplate="output/template-output.json"

rm -rf output
mkdir -p output

templateName="output/template-temp.json" 
outputTemplate="output/template-output.json"

cp template.json output/template-temp.json

# replacing values in template
bucketExp='s/SOURCE_BUCKET_NAME/'$sourceBucket'/g'

version=$(cat conf/$env/major.version).$(cat conf/$env/minor.version).$(cat conf/$env/patch.version)
versionExp='s/VERSION/'$version'/g'
echo 'Validating template...' 
sed -i $bucketExp output/template-temp.json
sed -i $versionExp output/template-temp.json

# copy docs
cp LICENSE.txt output/.
cp README.md output/.

sam package --template-file $templateName --use-json --output-template-file $outputTemplate --s3-bucket $sourceBucket