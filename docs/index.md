## What's Pypaystack2

So Paystack provides restful API endpoints for developers from different platforms
to integrate their services into their projects. So for python developers, to use
these endpoints, you might opt for a package like `requests` to handle all the
API calls which involves a lot of boilerplate. Pypaystack2 abstracts this process
by handling all these complexities under the hood and exposing simple APIs for
your python project. for example

```python
from pypaystack2 import Paystack  # assumes you have installed pypaystack2
from pypaystack2.utils import Country

paystack = Paystack()  # assumes that your paystack auth key is in 
# your enviromental variables i.e. PAYSTACK_AUTHORIZATION_KEY=<paystack-secret-key> otherwise instatiate 
# the Miscellaneous API wrapper as it is done below.
# paystack = Paystack(auth_key=<paystack-secret-key>)
response = paystack.miscellaneous.get_banks(country=Country.NIGERIA,
                                            use_cursor=False)  # Requires internet connection.
print(response)
```

With the code snippet above, you have successfully queried Paystack's Miscellaneous API
to get a list of banks supported by paystack. A `requests` equivalent of the above will
be like

```python
import requests  # assumes you have requests installed.

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer <your_auth_key>"
}
paystack_url = 'https://api.paystack.co/bank?perPage=50&country=ng&use_cursor=false'
response = requests.get(paystack_url, headers=headers)  # requires internet connection
print(response.json())
```

While both approaches achieve the same goal, `pypaystack2` uses `requests` under the hood and
manages the headers and URL routes to endpoints, so you can focus more on the actions. with the `miscellaneous_wrapper`
in the example above. you can call all endpoints associated with the Miscellaneous API with methods
provided like `.get_banks`, `.get_providers`, `.get_countries` and `.get_states`.

Pypaystack2 provides wrappers to all of Paystack APIs in its `pypaystack2.api` subpackage.
each of the wrapper classes is named to closely match the Paystack API. so say you want
to use Paystack's Invoices API, you'd import the wrapper with `from pypaystack2.api import Invoice`
for the Invoices API. All endpoints available on the Invoices API are available as methods
in the `Invoice` wrapper. Say you wanted to create an invoice by sending a
`POST` request to Paystack's Invoice API endpoint `/paymentrequest`, you'll call
`Invoice` wrapper's `.create` method.

```python
from pypaystack2 import Paystack

paystack = Paystack()
response = paystack.invoices.create(customer="CUS_xwaj0txjryg393b",
                                    amount=1000)  # Creates an invoice with a charge of ₦100
```

From here you can check out the tutorials section to get more examples and get familiar or surf the
documentation for wrappers and methods you'll need for your next project. Hurray!
