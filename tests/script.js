function getFunction() {
    var request = new XMLHttpRequest()

    // Open a new connection, using the GET request on the URL endpoint
    request.open('GET', 'https://t70d3kf5l8.execute-api.us-east-1.amazonaws.com/test', true)
    request.setRequestHeader('Access-Control-Allow-Origin', '*')
    request.onload = function () {
        // Begin accessing JSON data here
        var data = JSON.parse(this.response)

        if (request.status >= 200 && request.status < 400) {
            data.forEach((movie) => {
                console.log(movie.title)
            })
        } else {
            console.log('error')
        }
    }

    // Send request
    request.send()
}

// def get_image():
// driver.get("file:///Users\\rhysthomas\\Documents\\Tests\\ocr\\tests\\index.html")
// elem = driver.find_element_by_xpath("//*")
// source_code = elem.get_attribute("outerHTML")
// soup = BeautifulSoup(source_code, 'html.parser')
// image_array = soup.find_all('img')
// global image_link_array
// image_link_array = []
// for x in image_array:
//     image_url = x.get('src')
//     image_link_array.append(image_url)