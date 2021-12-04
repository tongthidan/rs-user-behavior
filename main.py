import logging
import logging.config
import os

from controller.main_controller import MainController


def conf_log():
    log_filename = "logs/rs.log"
    os.makedirs(os.path.dirname(log_filename), exist_ok=True)

    logging.config.fileConfig('conf/logging.conf')
    logging.root.setLevel(logging.NOTSET)


if __name__ == '__main__':
    conf_log()
    main_ctl = MainController()

    # TODO: refactor code
    # replace print -> logger
#     print info -> logger info
#       print error -> logger expection
# log info in work flow

