# MP Vehiclesearch API

##Usage
Python scrape.py

# API Usage
### API Base URL: `http://localhost:5000/num/<registrationnum>`

## Endpoint
* GET: [`/num/<registrationnum>`]
 
#### Example
Example usage: `GET http://localhost:5000/num/MP04A2300`

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
