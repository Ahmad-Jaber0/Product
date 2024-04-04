
jQuery(document).ready(function($) {
    console.log("Document ready!"); 
    
    $('#save-btn').on('click', function(event) {
        event.preventDefault(); 
        
        console.log("Button clicked!");

        var formData = $('#product-form').serialize();
        console.log("Form data:", formData); 

        $.ajax({
            url: "{% url 'add_product' %}",
            type: 'POST',
            data: formData,
            success: function(response) {
                console.log("Product added successfully!");
                alert("Product added successfully!");
                window.location.href = '/'; 
            },
            error: function(xhr, status, error) {
                console.error("Error adding product:", error);
                alert("Error adding product: " + error);
            }
        });
    });
});
