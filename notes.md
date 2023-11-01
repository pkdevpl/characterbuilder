## Order models example

Base Models:
* user
  * default_email
  * default_address
* email
  * email
* address
  * postcode
  * street 
  * number
* order
  * date_created
  * status
* product
  * name
  * price
  * unit

Additional connecting models:
* user_address
  * user
  * address
* order_product
  * order
  * product
  * amount
  * price
* user_order
  * user
  * order