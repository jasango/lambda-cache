import os
import json
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
