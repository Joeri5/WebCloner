from decorators.inject_logger import inject_logger
from interfaces.i_hello_service import IHelloService
from models.message import Message
import logging

class HelloService(IHelloService):

    @inject_logger
    def say_hello(self, logger: logging.Logger) -> None:
        message = Message("Hello, World!")
        logger.info(message.text)
