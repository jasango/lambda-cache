import json
import memory

def simple_test():
    #print(event)
    mem = memory.MemoryService("d6q2ft773kb04.cloudfront.net","app1","storage-bucket-123","us-east-1")
    #mem.putNumber("var4",0)
    #mem.incrementNumber("var4")
    print(mem.getNumber("var4"))
    
    
def benchmark():
    mem = memory.MemoryService("d6q2ft773kb04.cloudfront.net","app1","storage-bucket-123","us-east-1")
    millis1 = int(round(time.time() * 1000))
    mem.putNumber("var12",888888888888888)
    millis2 = int(round(time.time() * 1000))
    print("put milliseconds: " + str(millis2-millis1))
    millis3 = int(round(time.time() * 1000))
    print(mem.getNumber("var12"))    
    millis4 = int(round(time.time() * 1000))
    print("get no cache milliseconds: " + str(millis4-millis3))
    time.sleep(3)
    millis5 = int(round(time.time() * 1000))
    print(mem.getNumber("var12"))    
    millis6 = int(round(time.time() * 1000))
    print("get with cache milliseconds: " + str(millis6-millis5))


def unit_test(event, context):
    #print(event)
    mem = memory.MemoryService("d6q2ft773kb04.cloudfront.net","app1","storage-bucket-123","us-east-1")
    print("Put Number")
    mem.putNumber("var20",20)
    mem.incrementNumber("var20")
    print(mem.getNumber("var20"))
    print("Put String")
    mem.putString("var21","string 21")
    print(mem.getString("var21"))
    print("Put JSON")
    jsonDoc = { "att" : "valor" }
    mem.putJSON("var22",jsonDoc)
    print(mem.getJSON("var22")['att'])
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }