def display_options():
    print('Choose from the following actions: ')
    action_menu = '''
    Root (R)
    Retrieve account details (RAD)
    Create account funding source (CAFS)
    Create account VAN (CAVAN)
    List account funding sources (LAFS)
    List and search account transfers (LASAT)
    List account mass payments (LAMP)
    Create receive only customer (CROC)
    Create unverified customer (CUVC)
    Create verified personal customer (CVP)
    Retrieve customer (RC)
    List and search customers (LASC)
    Update customer (UC)
    List customer business classifications (LCBC)
    retrieve business classification (RBC)
    initiate KBA (IKBA)
    retrieve KBA (RKBA)
    verify KBA (VKBA)
    Create beneficial owner (CBO)
    Retrieve beneficial owner (RBO)
    list beneficial owners (LBO)
    update beneficial owner (UBO)
    Remove beneficial owner (DBO)
    Retrieve beneficial ownership status (RBOS)
    Certify beneficial ownership (CBOS)
    Quit (Q)
    '''
    print(action_menu)

def get_user_input():
    return input('Enter your action: ')

def handle_input(input, DWOLLA_APP_KEY, DWOLLA_APP_SECRET):
    client = dwollav2.Client(key = DWOLLA_APP_KEY, secret = DWOLLA_APP_SECRET, environment = 'sandbox')
    application_token = client.Auth.client()
    if input == 'R':
        root(application_token)
    elif input == 'RAD':
        get_account_details(application_token)
    elif input == 'CAFS':
        create_account_funding_source(application_token)
    elif input == 'CAVAN':
        create_account_van(application_token)
    elif input == 'LAFS':
        list_account_funding_sources(application_token)
    elif input == 'LASAT':
        list_and_search_account_transfers(application_token)
    elif input == 'LAMP':
        list_account_mass_payments(application_token)
    elif input == 'CROC':
        create_receive_only_customer(application_token)
    elif input == 'CUVC':
        create_unverified_customer(application_token)
    elif input == 'CVP':
        create_verified_personal_customer(application_token)
    elif input == 'RC':
        retrieve_customer(application_token)
    elif input == 'LASC':
        list_and_search_customers(application_token)
    elif input == 'UC':
        update_customer(application_token)
    elif input == 'LCBC':
        list_customer_business_classifications(application_token)
    elif input == 'RBC':
        retrieve_business_classification(application_token)
    elif input == 'IKBA':
        initiate_kba(application_token)
    elif input == 'RKBA':
        retrieve_kba(application_token)
    elif input == 'VKBA':
        verify_kba(application_token)
    elif input == 'CBO':
        create_beneficial_owner(application_token)
    elif input == 'RBO':
        retrieve_beneficial_owner(application_token)
    elif input == 'LBO':
        list_beneficial_owners(application_token)
    elif input == 'UBO':
        update_beneficial_owner(application_token)
    elif input == 'DBO':
        remove_beneficial_owner(application_token)
    elif input == 'RBOS':
        retrieve_beneficial_ownership_status(application_token)
    elif input == 'CBOS':
        certify_beneficial_ownership(application_token)
    elif input == 'Q':
        quit()