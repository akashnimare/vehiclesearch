# MP Vehiclesearch API

##Usage
<code>pip install -r requirements.txt</code><br>
<code>Python scrape.py </code>

## API Usage
### API Base URL: `http://mprest.herokuapp.com/num/<registrationnum>`

## Endpoint
 GET: [`/num/<registrationnum>`]
 
#### Example
Example usage: `GET http://mprest.herokuapp.com/num/MP04A2300` <br>
See the permalink version of the request [here](http://hurl.eu/hurls/02782022b80ea993baa491eb5be1129b37001d7b/c4353d68c932a726d92998d3c17fd8e280d61a18).

Example result:
```json
{
  "Model": "BAJAJ SUPER", 
  "Owner Name": "SANTOSH KUMAR  SAXENA", 
  "RTO NAME": "BHOPAL", 
  "Regis Date": "01-04-2002", 
  "Registration num": "MP04A2300"
}
```

## TODO
* Proper error handling.
