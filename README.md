# Technical Sample for Lyft Apprentiship 
## Code Objective
- If you don’t have a current code sample you can share, please write a small web application in one of the above languages (Python/Ruby/Javascript). The application only needs to do the following:
### Accept a POST request to the route “/test”, which accepts one argument “string_to_cut”
### Return a JSON object with the key “return_string” and a string containing every third letter from the original string

## Test:
-Test the example locally with the command: curl -X POST https://localhost:8080/test --data '{"string_to_cut": "iamyourlyftdriver"}' -H 'Content-Type: application/json'
