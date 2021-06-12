This project allows you to find the optimal plan for you based on your Communauto invoice(s).

To run, inside ```main.py``` change ```INVOICE_STRING``` to your invoice contents:

![caption](showcase_communauto.gif)

Then simply run 
```shell script
python3 main.py
```

An example of my ivoice is already in there for you to play around with.

KNOWN ISSUES:

1) Works well only for Calgary rates.
2) Some PDF-viewers (e.g. macOS preview) select in a way that is not compatible with current parser function. 
   Works in Chrome.
   
   
Requires ```pytest``` for unit tests