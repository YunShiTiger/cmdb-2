from django.core.mail import send_mail as core_send_mail
from django.core.mail import EmailMultiAlternatives
import threading
from celery.task import task


class EmailThread(threading.Thread):
    def __init__(self, subject, body, from_email, recipient_list, fail_silently, html):
        self.subject = subject
        self.body = body
        self.recipient_list = recipient_list
        self.from_email = from_email
        self.fail_silently = fail_silently
        self.html = html
        threading.Thread.__init__(self)

    def run(self):
        msg = EmailMultiAlternatives(self.subject, self.body, self.from_email, self.recipient_list)
        if self.html:
            msg.attach_alternative(self.html, "text/html")
        print 'self.recipient_list : ', self.recipient_list
        msg.send(self.fail_silently)


def send_mail(subject, body, from_email, recipient_list, fail_silently=False, html=None, *args, **kwargs):
    print "subject: %s" % subject
    print "body: %s" % body
    print "html: %s" % html
    _send.delay(subject, body, from_email, recipient_list, fail_silently=False, html=None)
    #EmailThread(subject, body, from_email, recipient_list, fail_silently, html).start()


@task
def _send(subject, body, from_email, recipient_list, fail_silently=False, html=None):
    for _ in range(3):
        try:
            msg = EmailMultiAlternatives(subject, body, from_email, recipient_list)
            if html:
                msg.attach_alternative(html, "text/html")
            print 'recipient_list : ', recipient_list
            msg.send(fail_silently)
            print "_send mail success ..."
            break
        except Exception as e:
            print "_send mail failed ..."
            print str(e)
