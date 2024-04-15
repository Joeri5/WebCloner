import logging
import inject
from interfaces.i_hello_service import IHelloService
import dependency_container_config

def main():
    hello_service = inject.instance(IHelloService)
    hello_service.say_hello()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
