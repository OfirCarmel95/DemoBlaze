class Locators:

    # Login elements
    login_button = "login2"
    login_username = "loginusername"
    login_password = "loginpassword"
    login_submit_button = f'//*[@id="logInModal"]/div/div/div[3]/button[2]'
    name_of_user = "nameofuser"

    # Signup elements
    signup_button = "signin2"
    signup_username = "sign-username"
    signup_password = "sign-password"
    signup_submit_button = f'//*[@id="signInModal"]/div/div/div[3]/button[2]'

    # Contact elements
    contact_button = f'//*[@id="navbarExample"]/ul/li[2]/a'
    contact_email = "recipient-email"
    contact_name = "recipient-name"
    contact_message = "message-text"
    contact_submit_button = f'//*[@id="exampleModal"]/div/div/div[3]/button[2]'

    # Product elements
    product_link = ''

    # Order elements
    add_to_cart_button = "Add to cart"
    go_to_cart_button = "cartur"
    place_order_button = f'button[data-target="#orderModal"]'
    order_name = "name"
    order_country = "country"
    order_city = "city"
    order_credit_card = "card"
    order_month = "month"
    order_year = "year"
    order_purchase_button = f'//button[text()="Purchase"]'
    order_success_message = "sweet-alert"
    order_success_message_title = "/html/body/div[10]/h2"
    order_success_message_body = "text-muted"

