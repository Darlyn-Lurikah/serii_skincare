
// -- Adding stripe to checkout --
// Get element ids. Use slice to take quote marks off 
var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
// Create stripe var
var stripe = Stripe(stripePublicKey);
// Create instance of stripe
var elements = stripe.elements();

const appearance = {
    theme: 'bubblegum',
    variables: {
      fontWeightNormal: '500',
      borderRadius: '5px',
      colorBackground: 'white',
      colorPrimary: '#DF1B41',
      colorPrimaryText: 'white',
      spacingGridRow: '15px'
    },
    rules: {
      '.Label': {
        marginBottom: '6px'
      },
      '.Tab, .Input, .Block': {
        boxShadow: '0px 3px 10px rgba(18, 42, 66, 0.08)',
        padding: '12px'
      }
    }
  };
  

// Use instance to make card element 
var card = elements.create('card', {appearance: appearance});
// Mount card element to attr w/ this id 
card.mount('#card-element');


// -- Handling realtime validations on our card --
// On change event, get 'card-errors' element 
card.addEventListener('change', function (event) {
  var errorDiv = document.getElementById('card-errors');

  // If theres an error show error message and icon
  if (event.error) {
      var html = `
          <span class="icon" role="alert">
              <i class="fas fa-times"></i>
          </span>
          <span>${event.error.message}</span>
      `;
      $(errorDiv).html(html);
  // Else show nothing (empty string)
  } else {
      errorDiv.textContent = '';
  }
});


// -- Handling payment form submit --
var form = document.getElementById('payment-form');

// Listen for submit
form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    // Disable to prevent multiple submits
    card.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);
    $('#payment-form').fadeToggle(100);
    $('#loading-overlay').fadeToggle(100);
    // Call confirmCardPayment method & give stripe card
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
            // Adding form details to payment intent obj
            // so we can take it from webhook
            billing_details: {
              name: $.trim(form.full_name.value),
              phone: $.trim(form.phone_number.value),
              email: $.trim(form.email.value),
              address:{
                  line1: $.trim(form.street_address1.value),
                  line2: $.trim(form.street_address2.value),
                  city: $.trim(form.town_or_city.value),
                  country: $.trim(form.country.value),
                  state: $.trim(form.county.value),
              }
          }
      },
        shipping: {
            name: $.trim(form.full_name.value),
            phone: $.trim(form.phone_number.value),
            address: {
                line1: $.trim(form.street_address1.value),
                line2: $.trim(form.street_address2.value),
                city: $.trim(form.town_or_city.value),
                country: $.trim(form.country.value),
                postal_code: $.trim(form.postcode.value),
                state: $.trim(form.county.value),
            }
        },
    
    }).then(function(result) {
      // if error, show error message 
        if (result.error) {
            var errorDiv = document.getElementById('card-errors');
            var html = `
                <span class="icon" role="alert">
                <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>`;
            $(errorDiv).html(html);
            // Enable card & submit to correct error
            $('#payment-form').fadeToggle(100);
            $('#loading-overlay').fadeToggle(100);
            card.update({ 'disabled': false});
            $('#submit-button').attr('disabled', false);
        } else {
            // Else submit payment form
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});