from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404
from paypal.standard.forms import PayPalPaymentsForm
from django.urls import reverse
from orders.models import TRTLOrder, is_valid_trtlOrder
from django.urls import reverse
from django.conf import settings

#payment handle

@csrf_exempt
def payment_done(request):
    return render(request, 'payment/done.html')


@csrf_exempt
def payment_canceled(request):
    return render(request, 'payment/canceled.html')


def payforTRTL(request):

	# What you want the button to do.
	PAYPAL_RECEIVER_EMAIL = settings.PAYPAL_RECEIVER_EMAIL
	usdamount = request.GET.dict()['amountInUSD']
	trtlamount = request.GET.dict()['amountInTRTL']
	toWallet = request.GET.dict()['sendToWallet']
	nickname = request.GET.dict()['nickname']

	if is_valid_trtlOrder(float(trtlamount)):
		order = TRTLOrder.objects.create(sendToWallet = toWallet,
										amountInTRTL = trtlamount,
										amountInUSD = usdamount, 
										nickname = nickname)

		paypal_dict = {
			"business": PAYPAL_RECEIVER_EMAIL,
			"amount": usdamount,
			"item_name": "TRTL ATM",
			"invoice": str(order.id),
			"notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
			"return": request.build_absolute_uri(reverse('payment:done')),
			"cancel_return": request.build_absolute_uri(reverse('payment:canceled')),
		}

		# Create the instance.
		form = PayPalPaymentsForm(initial=paypal_dict)
		context = {"form": form}
		return render(request, "payment/payment.html", context)

	else:
		return render(request, "payment/canceled.html")