import json
import s3
import https
import sys
import util


class MemoryService:
    def __init__(self, memory_conf, app_name):
        self.distribution=memory_conf['DISTRIBUTION']
        self.bucket_name=memory_conf['BUCKET_NAME']
        self.region=memory_conf['REGION']
        self.app_name=app_name
        self.s3Manager = s3.S3Manager(self.bucket_name,self.region) 
        self.https_client = https.Connector()
        
    def getVersion(self):
        return '0.0.1'
        
        
    def put(self,varName,varValue):
        types = {
            int: "int",
            bool: "bool",
            str:  "str",
            list: "list",
            dict:  "dict"
        }
        strType = types[type(varValue)]
        return self.putVar(varName,varValue,strType,"high")      
        
    def putVar(self,var_name,var_value,object_type,access_frequency):
        sufix = "public/" + self.app_name + "/" + var_name 
        document = {
	        "objectKey": sufix,
            "accessFrequency" : access_frequency,
            "objectType": object_type,
            "objectValue": var_value
        } 
        json_dump = json.dumps(document)
        return self.s3Manager.write(sufix,json_dump)
        
        
    def get(self,var_name):
        try:
            url = "https://" + self.distribution + "/" + self.app_name + "/" + var_name + ".json"
            body = self.https_client.connect(url)
            jsonDoc = json.loads(body)
            varValue = jsonDoc["objectValue"]  
            return varValue 
        except Exception as e:
            if "403" not in str(sys.exc_info()[1]):
                print("MemoryServiceException: ", e.__class__, "occurred.")
                print("Variable url: " + url)
                print("Detail:", sys.exc_info()[1])
                #raise
        return None
        
 
def test():       
    print("test")
    conf = {
        "DISTRIBUTION": "d33fwx7e14khkx.cloudfront.net",
        "BUCKET_NAME": "storage-bucket-123",
        "REGION": "us-east-1"
    }
    mem = MemoryService(conf,"APP100")
    mem.put("var1",123)
    print(mem.get("var1"))
    mem.put("var2",True)
    print(mem.get("var2"))
    mem.put("var3","Hola")
    print(mem.get("var3"))
    mem.put("var4",[1,2,3])
    print(len(mem.get("var4")))
    x = {
        "Name": "John"
    }
    mem.put("var5",x)
    print(mem.get("var5")['Name'])
    
#test()
    
        