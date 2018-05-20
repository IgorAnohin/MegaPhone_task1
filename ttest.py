from yandex_money.api import Wallet, ExternalPayment

client_id = '6D3FD82502F95CC490D4297F871AB2B934597432FE48B681025011F50C079'

response = ExternalPayment.get_instance_id(client_id)
if reponse.status == "success":
    instance_id = response.instance_id;
else:
    # throw exception with reponse->error message

# make instance
external_payment = ExternalPayment(instance_id);

payment_options = {
    # pattern_id, etc..
}
response = external_payment.request(payment_options)
if response.status == "success":
    request_id = response.request_id
else:
    # throw exception with response->message

process_options = {
    "request_id": request_id
    # other params..
}
result = external_payment.process(process_options)
# process result according to docs
