# Serii Skincare 
Serii Skincare is an indie skincare brand that allows users to purchase products for the face and body.

Visit the live site [here](https://serii-skincare.herokuapp.com/)

![Main site image](docs/readme-header-image.PNG)

---
---
# Contents



# User Experience
## User Stories
---

### As an unregistered, I want to :

+ Browse all available products
+ Browse each product category 
+ View each product individually 
+ View my bag and and unpurchased products in it 
+ Add, edit quantity and remove items from my bag
+ Purchase a product without registering for an account
+ Be able to register for an account if I don't have one

### As a registered user, I want to:

+ Log into the site with own account
+ Save products to my favourites and view in my profile
+ See a record of past purchases
+ Be able to navigate to each past purchase product page
+ Be able to save my delivery information
+ Be able to change/update my delivery information
+ Have the access and functionality as unregistered users

### As the site administrator, I want to:

+ Be able to log into the admin panel
+ Be able to add, edit or remove products, without vistiting the admin panel.
+ Be able to view all orders and site info via the admin panel



## Design

For this site, I wanted something soft and a bit playful but not too busy so it feels like a place for quality products. 


### Colour Scheme
The colour scheme is made up of soft pinks, pale blue and a deep ultramarine 

![colour scheme](docs/colour-scheme.PNG)

The colours, while not the most neutral, are still soft enought not to overwhelm the user.
I used the ultramarine for text and buttons to make them stand out. It's a better alternative to black or dark grey as it has high contrast, but still fits the brand image. 
The gold adds a touch of decadance.


### Typography
For the general font throught the site I chose [Mukta Malar](https://fonts.google.com/specimen/Mukta+Malar?query=mal)as it is clean, easy to read and contrast well with the brand name font

The brand font I chose is [STIX Two Text](https://fonts.google.com/specimen/STIX+Two+Text?query=stix)as it felt grounded but not too serious and would be good for drawing attention to various area of the site against the other simpler Mukta Malar font. 


## Wireframes and Initial Design

[Initial design idea here](docs/MS4-design.pdf)

As the project went on, the wireframe design changed do to design limiations and time constraints. 


# Features
## Current Features
### **Navigation menu displayed on pages**

The navigation menu on all pages hepls users move easily through the site.

The navigation buttons update depending on whether a user is logged in, logged out or logged in as Admin:

| Nav Link              |Not logged in  |Logged in as user|Logged in as admin
|:-------------         |:------------- |:----------------|:------------- |
|Logo(back to home)     |yes            |yes              |yes
|Product Management     |no             |no               |yes
|My Profile             |no             |yes              |yes
|Sign Out               |no             |yes              |yes
|Register               |yes            |no               |no
|Sign In                |yes            |no               |no
|All Nav Products       |yes            |yes              |yes



### **Registration not required to browse**

Perhaps the most importaqnt feature as most users will simply want to browse the site out of curiosity. 


### **Registration not required to purchase**

This was the second important feature as the majourity of users will want to buy quickly so being required to have an account to buy would be time consuming and off putting to users.  

### **User profile creation**

If a user wants to create a profile, they can. The features of registations are:

+ Username
   + A user can choose a unique username thats not taken but any other user
   + A notification will tell user if their undername is avaialble

+ Email address
   + A user needs to create a profile using an email address
   + The email is required twice to decrease chance of user error
   + An automatic email is sent to the user to confirm it is their the email address and set up their account 

+ Password
   + The password must be entered twice to decrease chance of user error 

A user with a profile can:
+ Access order history displayed in their profile.
+ Save default delivery information to their profile from the checkout page
+ Update default delivery information to their profile from their profile page


---

### **Products Page**

Both authorised and unorthorised users can browse the products.
They browse the following product options
Products can be sorted by:

+ Shop All:
   + All products
   + By Price
   + By Rating
   + By Category


+ Skincare:
   + Face wash
   + Moisturisers
   + Toners
   + Serums
   + All skincare


+ Bodycare:
   + Body wash
   + Body lotion
   + Body scrub
   + All Bodycare
+ Fragrance:
   + Perfumes


+ Special offers:
   + New arrivals
   + Sale
   + All special offers

All product options can be sorted by:

   + Price (low to high)
   + Price (high to low)
   + Rating (low to high)
   + Rating (high to low)
   + Name (A-Z)
   + Name (Z-A)
   + Catergory (A to Z)
   + Catergory (Z to A)


---


### **Product Details Page**

From the product detail page, the user can:
+ View Product name
+ View Product description
+ Select a quantity 
+ Add product to bag 
+ Go back to all products page 



### **Admin CRUD functionality**

Admin users have all the features of non admin users with the addition of CRUD functionality. From the site admin can add, edit and delete products, without the admin panel
+ Add Product: 
Located in the 'My Account' dropdown, in 'Product Management'.


+ Edit Product: 
Located in the 'My Account' dropdown, in 'Product Management'. Or from the products catergory pages or the individual product detail page will naviagate to the edit product form in 'Product Management'. 

+ Delete Product:
From the products catergory pages or the individual product detail page. 







