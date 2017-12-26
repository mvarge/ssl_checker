# Python SSL Cert Date Checker
Simple and Native Python SSL Cert Date Expiration Checker

## About
This program is written aiming to use the most simple and native tools that are available with Python in order to check any SSL Certificate expiration date. More validations are possible 

## Further Use
The `get_cert()` function already returns a Certificate object that can be used to any other certificate validation besides an expiration date check. For using it just iterate over the object to understand its attributes, that are dinamically generated.

## Examples

```
$ python
Python 2.7.5 (default, Nov 20 2015, 02:00:19) 
[GCC 4.8.5 20150623 (Red Hat 4.8.5-4)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> from ssl_expiration import get_cert
>>>
>>> cert = get_cert('www.uol.com.br')
>>>
>>> cert
<ssl_expiration.Certificate object at 0x01FB20D0>
>>>
>>> c.valid
True
>>> c.notAfter
'Feb 17 23:59:59 2018 GMT'
```

## Author

Marcelo Marques da Silva Varge
(marcelo.varge@gmail.com)
