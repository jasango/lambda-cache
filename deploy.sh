#!/usr/bin/env bash

# getting env
env=$(cat conf/current.env)

# generating new version number
echo $((($(cat conf/$env/patch.version)+1)))>conf/$env/patch.version

./package.sh

sourceBucket=$(cat conf/$env/source-bucket.name) 
version=$(cat conf/$env/major.version).$(cat conf/$env/minor.version).$(cat conf/$env/patch.version)
stackName=$(cat conf/$env/stack.name) 
storageBucket=$(cat conf/$env/storage-bucket.name)
keyGroupId=$(cat conf/$env/key-group.id)


outputTemplate="output/template-output.json"


# creating and uploading lambda functions packages
lambdaFunctions=("lambda-cache-python-demo" "lambda-cache-nodejs-demo" "lambda-cache-nodejs-auth-demo")  

i=0
while [ $i -lt ${#lambdaFunctions[@]} ] 
do
    echo ${lambdaFunctions[$i]} 
    zip -rj output/${lambdaFunctions[$i]}-$version.zip lambda/${lambdaFunctions[$i]}
    aws s3 cp output/${lambdaFunctions[$i]}-$version.zip s3://$sourceBucket/lambda/
    i=`expr $i + 1` 
done

# create python sdk package
sdkPythonName=lambda-cache-python-sdk-$version.zip
cd  sdk/python/code
zip -r ../../../output/$sdkPythonName ./python
cd ../../../
aws s3 cp output/$sdkPythonName s3://$sourceBucket/sdk/

# create nodejs sdk package
sdkNodejsName=lambda-cache-nodejs-sdk-$version.zip
cd  sdk/nodejs/code
zip -r ../../../output/$sdkNodejsName ./nodejs/
cd ../../../
aws s3 cp output/$sdkNodejsName s3://$sourceBucket/sdk/


sam deploy --use-json --capabilities CAPABILITY_IAM --template-file $outputTemplate --stack-name $stackName --parameter-overrides \
ParameterKey=StorageBucketName,ParameterValue=$storageBucket \
ParameterKey=KeyGroupId,ParameterValue=$keyGroupId