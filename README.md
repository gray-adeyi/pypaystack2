# PyPaystack2

[![Downloads](https://static.pepy.tech/badge/pypaystack2)](https://pepy.tech/project/pypaystack2)
[![Downloads](https://static.pepy.tech/badge/pypaystack2/month)](https://pepy.tech/project/pypaystack2)
[![Downloads](https://static.pepy.tech/badge/pypaystack2/week)](https://pepy.tech/project/pypaystack2)

A developer friendly [Paystack](https://paystack.com/) API wrapper.

## Installation

1. Create your [Paystack account](https://paystack.com/) to get your Authorization key that is required to use this
   package.
2. Store your authorization key in your environment variable as `PAYSTACK_AUTHORIZATION_KEY` or pass it into the
   pypaystack api wrappers at instantiation.
3. Install pypaystack2 package.

```bash
pip install -U pypaystack2
```

## What's Pypaystack2

So Paystack provides restful API endpoints for developers from different platforms
to integrate their services into their projects. So for python developers, to use
these endpoints, you might opt for a package like `requests` to handle all the
API calls which involves a lot of boilerplate. Pypaystack2 abstracts this process
by handling all these complexities under the hood and exposing simple APIs for
your python project.[See Pypaystack2's Documentation](https://gray-adeyi.github.io/pypaystack2/). You're encouraged to
use this documentation alongside [Paystack's official documentation](https://paystack.com/docs/)

```python
from pypaystack2 import Paystack  # assumes you have installed pypaystack2
from pypaystack2.utils import Country

paystack = Paystack()  # assumes that your paystack auth key is in 
# your environmental variables i.e. PAYSTACK_AUTHORIZATION_KEY=your_paystack_secret_key otherwise instantiate 
# the Miscellaneous API wrapper as it is done below.
# paystack = Paystack(auth_key=your_paystack_secret_key)
response = paystack.miscellaneous.get_banks(country=Country.NIGERIA, use_cursor=False)  # Requires internet connection.
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
manages the headers and URL routes to endpoints, so you can focus more on the actions. with the `paystack`
in the example above, you can call all endpoints provided by paystack via `paystack.[api_group_name].[method]` so for
example associated with the Miscellaneous API with
methods
provided like `.get_banks`, `.get_providers`, `.get_countries` and `.get_states` to use them, you can that by
`paystack.miscellaneous.get_banks()`, `paystack.miscellaneous.get_providers`. Say you wanted to verify a transaction
with Paystack's Transaction API you can achieve that like
so `paystack.transactions.verify(reference="transaction-reference")`

Pypaystack2 currently provides wrappers to the following Paystack APIs via

```python
from pypaystack2 import Paystack  # assumes you have installed pypaystack2

paystack = Paystack()  # assumes that your paystack auth key is in 
# your environmental variables i.e. PAYSTACK_AUTHORIZATION_KEY=your_paystack_secret_key otherwise instantiate 
# the Miscellaneous API wrapper as it is done below.
# paystack = Paystack(auth_key=your_paystack_secret_key)
paystack.apple_pay  # Apple Pay API e.g paystack.apple_pay.get_domains()
paystack.bulk_charges  # e.g. paystack.bulk_charges.get_batch()
paystack.charge  # e.g. paystack.charge.check_pending_charge()
```

For more, [See Documentation](https://gray-adeyi.github.io/pypaystack2/)