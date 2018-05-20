from yandex_money.api import Wallet, ExternalPayment

scope = ['account-info', 'operation-history'] # etc..
auth_url = Wallet.build_obtain_token_url(client_id,
    redirect_uri, scope)

access_token = Wallet.get_access_token(client_id, code, redirect_uri,
    client_secret=None)

account_info = api.account_info()
balance = account_info['balance'] # and so on

request_options = {
    "pattern_id": "p2p",
    "to": "410011161616877",
    "amount_due": "0.02",
    "comment": "test payment comment from yandex-money-python",
    "message": "test payment message from yandex-money-python",
    "label": "testPayment",
    "test_payment": true,
    "test_result": "success"
};
request_result = api.request(request_options)
# check status

process_payment = api.process({
    "request_id": request_result['request_id'],
})
# check result
if process_payment['status'] == "success":
    # show success page
else:
    # something went wrong
