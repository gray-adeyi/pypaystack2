.. pypaystack2 documentation master file, created by
   sphinx-quickstart on Fri Jul 22 04:34:09 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to pypaystack2's documentation!
=======================================
Pypaystack2 is a simple API wrapper for Paystack API Endpoints in python.
A fork of the initial pypaystack project. Inspired by the initial project,
It aims to improve on the good works of the initial project which is no 
longer actively maintained. I'm not sure I knew much about python and programming
in general when the original authors created it in 2016 but in my journey, the
project has proved useful in several python projects that I've written over
the years. The motivation for building on this package is that it's awesome,
but in recent years, the package breaks my django applications when deploying
to a hosting platform. So this is my attempt to provide a solution. Plus my
curiosity to feel what it's like to build and maintain a package. let's get
started!

What's Pypaystack2
------------------
So Paystack provides RESTful API endpoints for developers from different platforms
to integrate their services into their projects. So for python developers, to use
this endpoints, you might opt for a package like ``requests`` to handle all the
API calls which involves a lot of boilerplate. Pypaystack2 abstracts this process
by handling all this complexities under the hood and exposing simple APIs for
your python project. for example

.. code-block:: python
   
   from pypaystack2.api import Miscellaneous # assumes you have installed pypaystack2
   from pypaystack2.utils import Country
   miscellaneous_wrapper = Miscellaneous() # assumes that your paystack auth key is in 
   # your enviromental variables i.e PAYSTACK_AUTHORIZATION_KEY=your_key otherwise instatiate 
   # the Miscellaneous API wrapper as it is done below.
   # miscellaneous_wrapper = Miscellaneous(auth_key=your_paystack_auth_key)
   response = miscellaneous_wrapper.get_banks(country=Country.NIGERIA,use_cursor=False) # Requires internet connection.
   print(response)

With the code snippet above, you have successfully queried Paystack's Miscellaneous API
to get a list of banks supported by paystack. A ``requests`` equivalent of the above will
be like

.. code-block:: python

   import requests # assumes you have requests installed.
   headers = {
      "Content-Type":"application/json",
      "Authorization": "Bearer <your_auth_key>"
      }
   paystack_url = 'https://api.paystack.co/bank?perPage=50&country=ng&use_cursor=false'
   response = requests.get(paystack_url,headers=headers) # requires internet connection
   print(response.json())

While both approaches achieve the same goal, ``pypaystack2`` uses ``requests`` under the hood and
manages the headers and URL routes to endpoints so you can focus more on the actions. with the ``miscellaneous_wrapper``
in the example above. you can call all endpoints associated with the Miscellaneous API with methods
provided like ``.get_banks``, ``.get_providers``, ``.get_countries`` and ``.get_states``.

Pypaystack2 provides wrappers to all of Paystack APIs in its ``pypaystack2.api`` subpackage.
each of the wrappers are classes named to closely match the Paystack API. so say you want
to use Paystack's Invoices API, you'd  import the wrapper with ``from pypaystack2.api import Invoice``
for the Invoices API. All endpoints available on the Invoices API are available as methods
in the ``Invoice`` wrapper. Say you wanted to create an invoice by sending a
``POST`` request to Paystack's Invoice API endpoint ``/paymentrequest``, you'll call
``Invoice`` wrapper's ``.create`` method.

.. code:: python

   from pypaystack2.api import Invoice
   invoice_wrapper = Invoice()
   response = invoice_wrapper.create(custmer="CUS_xwaj0txjryg393b",amount=1000) # Creates an invoice with a charge of ₦100

From here you can check out the tutorials section to get more examples and get familiar or surf the
documentation for wrappers and methods you'll need for your next project. Hurray!

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   modules
   

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
