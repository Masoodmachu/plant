$(document).ready(function () {
           $('.razorpay').click(function (e){
                     e.preventDefault();
                     var first_name = $("[name = 'first_name']").val();
                     var last_name = $("[name = 'last_name']").val();
                     var phone = $("[name = 'phone']").val();
                     var email = $("[name = 'email']").val();
                     var address = $("[name = 'address']").val();
                     var city = $("[name = 'city']").val();
                     var house = $("[name = 'house']").val();
                     var postal_code = $("[name = 'postal_code']").val();

                     if(first_name == "" || last_name == "" || phone == "" || email == "" || address == "" || city == "" || house == "" || postal_code == "")
                     {
                            swal("Alert","All Fields are Required","error");
                            return false;

                     }
                     else
                     var options = {
                                "key": "rzp_test_IzIBFTmzd3zzKk",
                                "amount": "50000",
                                "currency": "INR",
                                "name": "Machu",
                                "description": "Test Transaction",
                                "image": "https://example.com/your_logo",
                                "handler": function (response){
                                    alert(response.razorpay_payment_id);
                                },
                                "prefill": {
                                     "name": first_name, //your customer's name
                                     "email": email,
                                     "contact": phone
                                },
                                "theme": {
                                    "color": "#3399cc"
                                }
                            };
                            var rzp1 = new Razorpay(options);
                            rzp1.on('payment.failed', function (response){
                                    alert(response.error.metadata.payment_id);
                            });
                                rzp1.open();

                     });

           });