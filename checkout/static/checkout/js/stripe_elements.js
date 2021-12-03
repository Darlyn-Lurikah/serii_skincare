
// -- Adding stripe to checkout --
// Get element ids. Use slice to take quote marks off 
var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);
// Create stripe var
var stripe = Stripe(stripe_public_key);
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