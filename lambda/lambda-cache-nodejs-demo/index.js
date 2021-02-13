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
