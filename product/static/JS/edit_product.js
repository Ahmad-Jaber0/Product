jQuery(document).ready(function($) {
    console.log("Document ready!");

    $('#save-btn1').on('click', function(event) {
        event.preventDefault();

        console.log("Button clicked!");

        var formData = $('#product-form1').serialize();
        console.log("Form data:", formData);
        $.ajax({           
            url: NewUrl,
            type: 'POST',
            data: formData,

            success: function(response) {
                console.log(NewUrl);
                alert("Product update successful!");
                window.location.href = '/'; 
            },
            error: function(xhr, status, error) {
                console.error("Error updating product:", error);
                alert("Error updating product: " + error);
            }
        });
    });
});