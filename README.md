# lambda-cache

**Memory Service for the Internet Operating System**

Welcome to this project!

If you are seeking a cost-effective, simple to use, serverless cache, persisted on S3 and loaded in cloudfront's edge locations memory, with a simple SDK (put and get) and overcome the stateless nature of AWS Lambda your are in the right place.


if you would like to get started fast, have a working demo in 10 minutes and use in your applications, continue reading. 


## How do I get started fast?

* The easiest approach is to use the AWS Serverless Application Repository (SAR) to install lambda-cache from this link: [Quick install](https://serverlessrepo.aws.amazon.com/applications/us-east-1/484660614037/lambda-cache)
* It is recommended to create a new account (in AWS Organizations) to treat the lambda-cache as an independent microservice.
* You are going to have some lambda functions demo applications that you can analize to undertand how lambda-cache works.
* Two SDKs (python and nodejs) based on lambda layers will be created and will be ready to use by you applications quickly.


## How easy is to use it?

### Python

```python
import memory

def lambda_handler(event, context):
    mem_conf = {
        "DISTRIBUTION": os.environ['DISTRIBUTION'],
        "BUCKET_NAME": os.environ['STORAGE_BUCKET'],
        "REGION": os.environ['REGION']
    }
    mem = memory.MemoryService(mem_conf,"memory-service-python-demo")
    print("Memory Service version: " + mem.getVersion())
    # Number
    print("Putting and getting number: 123")
    mem.put("var1",123)
    print(mem.get("var1"))
    # Boolean
    print("Putting and getting boolean: True")
    mem.put("var2",True)
    print(mem.get("var2"))
    # String
    print("Putting and getting string: Hello World!")
    mem.put("var3","Hello World!")
    print(mem.get("var3"))
    # Array
    print("Putting and getting array: [1,2,3] and printing size")
    mem.put("var4",[1,2,3])
    print(len(mem.get("var4")))
    # Object
    print('Putting and getting object: { "Name" : "Joe" }')
    mem.put("var5",json.loads('{ "Name" : "Joe" }'))
    print(mem.get("var5")['Name'])
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
```




### Nodejs

```javascript
const memory = require('sdk-memory-service');

exports.handler = async(event) => {
    const params = {
        "DISTRIBUTION": process.env.DISTRIBUTION,
        "BUCKET_NAME": process.env.STORAGE_BUCKET
    };
    console.debug("Creating memory object..")
    var mem = new memory(params,"memory-service-nodejs-demo");
    // Number
    console.log("Putting and getting number: 123")
    await mem.put("var1",123)
    console.log(mem.get("var1"))
    // Boolean
    console.log("Putting and getting boolean: True")
    await mem.put("var2",true)
    console.log(mem.get("var2"))
    // String
    console.log("Putting and getting string: Hello World!")
    await mem.put("var3","Hello World!")
    console.log(mem.get("var3"))
    // Array
    console.log("Putting and getting array: [1,2,3] and priting size")
    await mem.put("var4",[1,2,3])
    console.log(mem.get("var4").length)
    // Object
    console.log('Putting and getting object: { "Name" : "Joe" }')
    await mem.put("var5",JSON.parse('{ "Name" : "Joe" }'))
    console.log(mem.get("var5")['Name'])

    const response = {
        statusCode: 200,
        body: JSON.stringify('Done!'),
    };
    return response;
}
```



## What Programming Languages are supported by lambda-cache

* Currently Python and Nodejs SDKs are provided as lambda layers.


## What is the Application Programming Interface (API)

 * The API has a simple contract and it is designed to avoid casting operations by developers. 
 * The SDKs get operations will always return the same data types previously provided to the put operations.

### Python API

* `def put(self,varName,varValue) `
* `def get(self,var_name)`

* The cache returns the same data types it recieves.
* int, bool, str, list and dict types are supported.



### Nodejs

* `async put(varName, varValue)` 
* `get(varName)`


* The cache returns the same data types it recieves.
* string, number, object and boolean types are supported.



## What resources are created by the cloudformation template?

* One public cloudfront distribution for public data.
* One private cloudfront distribution for authenticated data.
* One S3 bucket for cache storage.
* The python SDK lambda layer.
* The nodejs SDK lambda layer.
* Demo Application: Python lambda function.
* Demo Application: Nodejs lambda function.
* Demo Application: Nodejs lambda function with authentication.


## How do I use authentication?

* Authentication is based on pre-signed urls.
* It is currently only supported by the Nodejs SDK.
* You need to create a Public Key and a Key Group entities in CloudFront Console and provide the resulted Key Group Id as a parameter at the stack creation or update. 
* In order to generate a key pair to use you can see this link: [Cloudfront documentation](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-trusted-signers.html#private-content-creating-cloudfront-key-pairs) If you would like the fast-track here you are [RSA Key Generator](https://cryptotools.net/rsagen). You should choose 2048 key length.
* Once you have created the Public Key and a Key Group entities in CloudFormation and updated your stack with your Key Group Id as a parameter you can test your private cache following these 2 steps: 1. Go to the AWS console and find the lambda function called "lambda-cache-nodejs-auth-demo" and change the PUBLIC_KEY_ID enviroment variable with the public key id that you can find in cloudfront. 2. Add your private key in the file private_key.pem located in the same lambda function and run it.


### Nodejs with Authentication


```javascript
const memory = require('sdk-memory-service');

exports.handler = async(event) => {
    const params = {
        "DISTRIBUTION": process.env.DISTRIBUTION,
        "BUCKET_NAME": process.env.STORAGE_BUCKET,
        "PK_PATH": process.env.PK_PATH,
        "PUBLIC_KEY_ID": process.env.PUBLIC_KEY_ID
    };
    console.debug("Creating memory object..")
    var mem = new memory(params,"memory-service-nodejs-auth-demo");
    // Number
    console.log("Putting and getting number: 123")
    await mem.put("var1",123)
    console.log(mem.get("var1"))
    // Boolean
    console.log("Putting and getting boolean: True")
    await mem.put("var2",true)
    console.log(mem.get("var2"))
    // String
    console.log("Putting and getting string: Hello World!")
    await mem.put("var3","Hello World!")
    console.log(mem.get("var3"))
    // Array
    console.log("Putting and getting array: [1,2,3] and priting size")
    await mem.put("var4",[1,2,3])
    console.log(mem.get("var4").length)
    // Object
    console.log('Putting and getting object: { "Name" : "Joe" }')
    await mem.put("var5",JSON.parse('{ "Name" : "Joe" }'))
    console.log(mem.get("var5")['Name'])

    const response = {
        statusCode: 200,
        body: JSON.stringify('Done!'),
    };
    return response;
}
```


## Why this project?

### What is the internet operating system?

According to wikipedia an operating system (OS) is a system software that manages computer hardware, software resources, and provides common services for computer programs. Those programs were built historically on top of the operating system which provided memory, CPU, storage and other resources.

The internet era brought the neccesity to make the applications support millions of users, scale virtually infinitive and we were abbligated to go out-of-box literally.

The internet operating system is the ability of the cloud computing era to create applications on top of specialized building blocks, out-of-the-box, that provides resources to modern applications. These building blocks not only abstract the complexities of server installation and administration, they automatically provides systemic qualities like high availbility, fault-tolerance, infinit scaling, security and others. Last but not least these bulding blocks allow the possibility to really pay for the resources used and needed by applications.
 

###  What is a Memory Service for the Internet Operating System?

* It is an opensource service, deployed on top of Amazon Cloudfront and Amazon S3 that make easier the access to memory resource from AWS Lambda functions.
* It is a SDK for several programming languages with a simple contract to avoid the necessary stateless nature of AWS Lambda. 
* It is a cost-effective, simple to use, serverless cache, persisted on S3 and loaded in cloudfront's edge locations memory.


### Why you do not simply use AWS ElastiCache / DynamoDb Accelerator (DAX) or AWS API Gateway Cache?

* They do not have the simple "Internet Operating System" phylosofy. The simple put / get operations over the memory resource are well worth and  that keep code clean and understandable. 
* Those services are great but are not well suited for not internet-exposed Lambda function executions.
* The least monthly cost of AWS ElastiCache is 12.41 on one on-demand t2.micro server (not serverless / not high available / not fault-tolerant / not cost effective).
* The least monthly cost of DAX is 29.20 on one on-demand t2.small server (not serveless / not high  available / not fault-tolerant / not cost effective).   
* The least monthly cost of API Gateway Cache is 14.60 on a 0.5 GB server (only for APIs, not high available? / not fault-tolerant? / not cost effective).
* Amazon CloudFront and S3 are extremely cost-effective, high available, infinite scalable and serverless.


### What is the Roadmap / Wish list?

* Overload PUT method with TTL for the objects on cloudfront.
* Add local cache on SDKs for increased GET performance.
* Choose between S3 Standard / S3 Standard IA or Intelligent Tiering.
* Remove objects from Cache.
* Failover to S3 when GET not possible on the distribution.
* Generate CloudFront key pair automatically for users.
* Cost calculator.
* Cache explorer (only S3).
* Java SDK.
* Javascript SDK for browsers.

