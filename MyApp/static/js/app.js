
// Retrieve data from the CSV file and execute everything below
(async function(){
    console.log("in function")
    const defaultURL = `/getnames`
    let myData = await d3.json(defaultURL);
        console.log(myData);
        print(myData)
        d3.select(".mytext").text = "hello everyone!"
        console.log("here is my data!")
})()
