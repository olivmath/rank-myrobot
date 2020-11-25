let request = new XMLHttpRequest();
request.open("GET", "http://127.0.0.1:5000");
request.send();
request.onload = () => {
    console.log(request);
    if (request.status === 200) {
        console.log(JSON.parse(request.response));
    } else {
        console.log(`ERROR ${request.status} => ${request.statusText}`)
    }
}