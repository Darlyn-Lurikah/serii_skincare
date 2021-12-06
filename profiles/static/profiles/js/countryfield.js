// For country field dropdown selected 

// Put value of country field in var
let countrySelected = $('#id_default_country').val();
// 'Country' placeholder val is empty string
// so its False. Use bool to check if its selected
// then set element to grey 
if(!countrySelected) {
    $('#id_default_country').css('color', '#aab7c4');
};
// Capture change event 
$('#id_default_country').change(function() {
    // Get the value of current selection
    countrySelected = $(this).val();
    // Check if False (placeholder) and set right colour 
    if(!countrySelected) {
        $(this).css('color', '#aab7c4');
    } else {
        $(this).css('color', '#000');
    }
});