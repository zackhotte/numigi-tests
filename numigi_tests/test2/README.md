# Requests & Factory Design Pattern

An analysis of the Factory design pattern used by the [Requests](https://github.com/requests/requests) package.

## Factory Design Pattern

The main philosophy behind the Factory design pattern is to not use a constructor to create
new instances of classes, but instead, the Factory should provide an interface to create instances based on different 
criteria and parameters.<br>
<br>
One of the Factory patterns main advantages is to abstract away the high level of complexity of setting up objects.
It is also ideal when working with many components that share many of the same properties.

## Requests & Factory
With the Requests module, you make an HTTP web request to a url and the module will return a **Response** object.
However, there are many different types of web requests we can make, for example:

* GET
* POST
* PUT
* DELETE
* PATCH
* HEAD
* OPTIONS

Instead of first creating a Session object, and then creating a Request object and then creating an instance of the final 
Response object that we are looking for, all while taking into account which HTTP method we are using, the Requests module
has a number of Factory methods for instantiating the proper Response object based on the HTTP method that we are using.

```
>>> import requests
>>> res = requests.get('https://httpbin.org/get')
>>> type(res)
<class 'requests.models.Response'>
```

```
>>> import requests
>>> res = requests.post('https://httpbin.org/post')
>>> type(res)
<class 'requests.models.Response'>
```

The setup of the Session, Request and Response objects are quite complex, and the Factory design pattern allows us to 
abstract away that complexity. This pattern is also ideal for Requests as most HTTP requests share similar properties, 
and the Factory pattern allows the sharing of these properties across HTTP request types that the user makes.
