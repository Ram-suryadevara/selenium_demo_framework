import logging
# predefined package
import os


class LogGen:
    """
    loading the log file
    """
    @staticmethod
    def loggen():
        """
        we can call directly without creating object using static method.
        we dont need self keyword here.
        """
        filename = os.path.join(os.path.dirname(__file__),
                                "../logs/automation1.log")
        logging.basicConfig(filename=filename,
                            format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p', force=True)
        # logging.basicConfig(filename=".\\logs\\automation1.log",
        #                     format='%(asctime)s: %(levelname)s: %(message)s',
        #                     datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
