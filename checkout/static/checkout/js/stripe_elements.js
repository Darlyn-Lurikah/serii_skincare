// Get element ids. Use slice to take quote marks off 
var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);
// Create stripe var
var stripe = Stripe(stripe_public_key);
// Create instance of stripe
var elements = stripe.elements();
// Use instance to make card element 
var card = elements.create('card');
// Mount card element to attr w/ this id 
card.mount('#card-element');