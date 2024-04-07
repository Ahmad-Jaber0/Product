jQuery(document).ready(function($) {
    console.log("Document ready!");

    $('#save-btn').on('click', function(event) {
        event.preventDefault();

        console.log("Button clicked!");

        var formData = $('#product-form').serialize();
        console.log("Form data:", formData);

        $.ajax({
            url: x,
            type: 'DELETE',
            beforeSend: function(xhr) {
                xhr.setRequestHeader("X-CSRFToken", csrfToken);
            },
            data: formData,
            success: function(response) {
                console.log("Product Delete successful!");
                alert("Product Delete successful!");
                window.location.href = '/'; 
            },
            error: function(xhr, status, error) {
                console.error("Error Delete product:", error);
                alert("Error Delete product: " + error);
            }
        });
    });
});