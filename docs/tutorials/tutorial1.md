# Paystack Command line Client

This tutorial aims to expose you to how to use `pypaystack2` in your python projects for paystack integrations.
We'll be building a simple command line application that integrates with paystack's services.

## Project Setup

We'll start by setting up our project. We'll be using `pipenv` for managing this project's dependencies and
environment. you're free to use your preferred choice like `virtualenv`. if you don't have `pipenv`
installed yet, you can install it with `pip install pipenv`. it's important to note that `pipenv` should be
installed globally and not within a virtual environment. You're good to proceed if this prerequisite is met.

- Create a directory to house our project.

```bash
mkdir paystack_cli_client && cd paystack_cli_client
```

- Initialize a virtual environment for the project.

```bash
pipenv shell
```

- Install the projects dependencies. We'll be needing `pypaystack2`, `python-dotenv`, and `typer`.
  `pypaystack2` package is an API wrapper for paystack's services. `python-dotenv` helps us manage our
  environmental variables and `typer` makes building command line apps in python super simple.

```bash
pipenv install pypaystack2 python-dotenv typer
```

If all work's fine, you're good to proceed.

## Environmental Variables

`pypaystack2` depends on your paystack authorization key that you get from signing up to paystack.
Paystack provides you with two pairs. A pair of public and secret key for live mode and another set
for test mode. You can find them in your account settings. Since this is just a tutorial we'll be
using only the test secret key. create a new file named `.env` within your project's root directory.
Now put in your test secret key in the `.env` file like so.

```env
PAYSTACK_AUTHORIZATION_KEY = "<your paystack test secret key>"
```

!!! warning

    Because this is just a tutorial, no extra measure is made to protect this environmental.
    In a more serious project or production code, extra care should be taken to protect it and
    also avoid pushing it to a remote source control.

## Let the games begin

It's time to start building! create a new file named `main.py` in your root directory.

```python
# root-dir/main.py
from dotenv import load_dotenv

load_dotenv()
```

What we have just done is loaded our secret test key within the `.env` file. You may be
wondering why do we need that, here's why `pypaystack2` needs this key to communicate with
paystack's api. alternatively, you can pass your authorization key into any of the api wrappers
provided by `pypaystack2` via their `auth_key` parameter. Here's a list of all the API wrappers
currently available as at the time of writing of this tutorial.

- ApplePay
- BulkCharge
- Charge
- ControlPanel
- Customer
- DedicatedAccount
- Dispute
- Invoice
- Miscellaneous
- Page
- Plan
- Product
- Refund
- Settlement
- Split
- SubAccount
- Subscription
- Terminal
- Transaction
- TransferReceipt
- TransferControl
- Transfer
- Verification

So in a situation where you don't have your `PAYSTACK_AUTHORIZATION_KEY` as an environmental variable,
you can pass it into any of the API wrappers. e.g.

```python
# When you don't have PAYSTACK_AUTHORIZATION_KEY(paystack secret key) in your environmental variables
from pypaystack2 import Paystack

paystack = Paystack(auth_key="<your test secret key>")

# When you have PAYSTACK_AUTHORIZATION_KEY(paystack secret key) set in your environmental variables
paystack = Paystack()
```

???+ note

    You don't have to provide your authorization key on the instantiation of any of the API wrappers
    as long as you have it set in your environmental variables like this tutorial does.

## On your marks!

The first feature we'll be implementing for our **Paystack Command line Client** is the ability to create
new customers on our paystack integration. so now update your `main.py` file with the code below.

```python
# root-dir/main.py
from dotenv import load_dotenv
from typer import Typer

load_dotenv()

app = Typer()


@app.command()
def new_customer():
    print("new customer successfully created!")


if __name__ == "__main__":
    app()
```

This is a minimum setup to building cli apps with `Typer`. Now try this in your project's root directory.

```bash
python main.py --help
```

You should see.

```bash
Usage: main.py [OPTIONS]

Options:
--install-completion [bash|zsh|fish|powershell|pwsh]
                                Install completion for the specified
                                shell.
--show-completion [bash|zsh|fish|powershell|pwsh]
                                Show completion for the specified shell,
                                to copy it or customize the installation.
--help                          Show this message and exit.
```

You can see that we now have a command line app that's responding to our command in this case `--help`. Let's
try out the custom command we just added.

```bash
python main.py
```

You should see

```bash
new customer successfully created!
```

At the moment, no new customer is actually getting created on your paystack integration. let's bring in
`pypaystack2` to help us get the job done. For this to work, `pypaystack2` provides wrappers for the
restful APIs provided by Paystack. These wrappers are named to closely match the API they wrap and methods
on these wrappers correspond to endpoints on the Paystack services you're interested in so in this case,
for us to create a customer on our integration, we need to use the `Customer` API wrapper which connects
to Paystack's Customer Services API. More info
at [Paystack's Customer Services API](https://paystack.com/docs/api/#customer)

```python
# root-dir/main.py
from typing import Optional
from dotenv import load_dotenv
from pypaystack2 import Paystack
from typer import Typer

load_dotenv()
app = Typer()

paystack = Paystack()


@app.command()
def new_customer(
        email: str,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        phone: Optional[str] = None,
):
    response = paystack.customers.create(
        email=email, first_name=first_name, last_name=last_name, phone=phone
    )
    print(response.status_code)
    print(response.status)
    print(response.message)
    print(response.data)


if __name__ == "__main__":
    app()
```

???+ note
All API wrappers are available on `pypaystack`. as attributes e.g. `paystack.transactions` for the Transactions API

Now if you run the script again.

```bash
python main.py
```

You get error saying you have a missing argument 'EMAIL'

```bash
Usage: main.py [OPTIONS] EMAIL
Try 'main.py --help' for help.

Error: Missing argument 'EMAIL'.
```

Now let's try out our script with the email of the customer
we want to create.

```bash
python main.py email@example.com
```

Now if all goes fine. "An Internet connection is required", you should
get something similar to this

```bash
200
True
Customer created
{'transactions': [], 'subscriptions': [], 'authorizations': [], 'first_name': '', 'last_name': '', 'email': 'email@example.com', 'phone': '', 'metadata': None, 'domain': 'test', 'customer_code': 'CUS_kd197ej30zxr34v', 'risk_action': 'default', 'id': 47748473, 'integration': 630606, 'createdAt': '2021-06-20T05:16:20.000Z', 'updatedAt': '2021-06-20T05:16:20.000Z', 'identified': False, 'identifications': None}

```

**Yay! You've just created a new customer on your integration** You can check out the customer's tab in  
your Paystack account to confirm this.

???+ tip

    You can also create new customers with a first name and last name like so.

    ```bash
    python main.py email@example.com --first-name John --last-name Doe
    ```

## What just happened?

You have just created a new customer on your integration with the CLI app you just built. But how? If you've followed
this tutorial to this point you already know what wrappers are, or you can quickly skim through the chapters before to
get a refresher. The right question should be what is the `create` method on the `Customer` wrapper for. You guess
right if what's on your mind is that it creates the new customer on your integration. So as it was said earlier, all
wrappers have methods on them that correspond to an endpoint on paystack and all of this methods will return
a `Response`
object based on the response it gets from Paystack. This `Response` is just a `NamedTuple` that holds the
`status,status_code,message` and `data`. So this call

```python
response = paystack.customers.create(email=email, first_name=first_name, last_name=last_name, phone=phone)
```

in our script returns the `Response` object just described, and you can access each of these attributes with
`response.status`, `response.status_code`, `response.message`, `response.data`

## More Commands!

Let's add a few more commands to our **Paystack Command line Client**

```python
# root-dir/main.py
from typing import Optional
from dotenv import load_dotenv
from pypaystack2 import Paystack
from typer import Typer

load_dotenv()

app = Typer()

paystack = Paystack()


@app.command()
def new_customer(
        email: str,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        phone: Optional[str] = None,
):
    response = paystack.customers.create(
        email=email, first_name=first_name, last_name=last_name, phone=phone
    )
    print(response.status_code)
    print(response.status)
    print(response.message)
    print(response.data)


@app.command()
def list_customers():
    response = paystack.customers.get_customers()
    print(response.status_code)
    print(response.status)
    print(response.message)
    print(response.data)


@app.command()
def get_customer(ec: str):
    response = paystack.customers.get_customer(email_or_code=ec)
    print(response.status_code)
    print(response.status)
    print(response.message)
    print(response.data)


@app.command()
def update_customer(code: str, last_name: str, first_name: str):
    response = paystack.customers.update(
        code=code, last_name=last_name, first_name=first_name
    )
    print(response.status_code)
    print(response.status)
    print(response.message)
    print(response.data)


if __name__ == "__main__":
    app()
```

We now have 3 new commands for our cli app. you can check them out with

```bash
python main.py --help
```

Now under the available command you should see get-customer, list-customers, new-customer,
update-customer

```bash
Usage: main.py [OPTIONS] COMMAND [ARGS]...

    Options:
    --install-completion [bash|zsh|fish|powershell|pwsh]
                                    Install completion for the specified
                                    shell.
    --show-completion [bash|zsh|fish|powershell|pwsh]
                                    Show completion for the specified shell,
                                    to copy it or customize the installation.
    --help                          Show this message and exit.

    Commands:
    get-customer
    list-customers
    new-customer
    update-customer
```

You can try out the new command with the following commands

## Where to go from here

**It's all in your hands now**. We now have a working cli app, but it does not have all the features
to make it a fully fledged **Paystack command line client** you can bring in more wrappers and implement
new commands. It also does not handle all the likely exception that can occur, but then, the purpose of
the tutorial is to expose you to `pypaystack2`. Not sure how something works, you can always search the
documentation. Good luck on your next project!