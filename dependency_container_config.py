import inject
from interfaces.i_hello_service import IHelloService
from services.hello_service import HelloService

def config(binder):
    binder.bind(IHelloService, HelloService())

inject.configure_once(config)
