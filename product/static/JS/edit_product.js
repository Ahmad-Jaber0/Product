
    jQuery(document).ready(function($) {
        console.log("Document ready!");

        $('#save-btn').on('click', function(event) {
            event.preventDefault();

            console.log("Button clicked!");

            var formData = $('#product-form').serialize();
            console.log("Form data:", formData);

            $.ajax({
                url: "{% url 'edit_product' pk %}",
                type: 'POST',
                data: formData,
                success: function(response) {
                    console.log("Product update successful!");
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
