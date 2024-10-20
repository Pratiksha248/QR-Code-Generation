#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Import the library
import qrcode

# Generate the QR code
img = qrcode.make('https://www.linkedin.com/in/pratiksha-sahoo/')

#Save the QR code image using an image extension
img.save("Pratiksha Sahoo's LinkedIn QRCode.png")

