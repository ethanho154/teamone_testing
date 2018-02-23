# Assignment 5
import logging


class listOb:

    def __init__(self, myList=[], listSum=None,
                 maxMin=None, maxDiff=None):
        self.myList = myList
        self.listSum = listSum
        self.maxMin = maxMin
        self.maxDiff = maxDiff
        self.find_listSum()
        self.find_maxMin()
        self.find_maxDiff()

    def import_modules(self):
        logging.info('Importing numpy module')
        try:
            import numpy as np
        except BaseException:
            logging.warning('Please install numpy')
            raise ImportError('Module numpy not found!')
        return np

    def find_listSum(self):
        """
        Adds a lest of numbers

        :param list_var: Is a list of numbers (int, float, complex)
        :returns: Addition of values in list
        :raises ValueError: If list_var is empty
        :raises ImportError: If numpy or numbers not installed in environment
        :raises TypeError: If element in list is not an int, float, or complex
        """

        np = self.import_modules()
        if not isinstance(self.myList, list):
            logging.warning('Input is not a list')
        for i in self.myList:
            if isinstance(i, (int, float, complex)):
                continue
            else:
                logging.warning('List elements must be int, float or complex')
                raise TypeError('List elements must be int, float, or complex')
        logging.debug(self.myList)
        value = np.sum(self.myList)
        logging.info(value)
        self.listSum = value

    def find_maxMin(self):
        """
        Finds the max and min in a list of positive values and returns a tuple

        :param inputList: Is a list of positive values
        :returns: Tuple of the max and min values
        :raises ImportError: If numpy is not installed in the env
        :raises ValueError: If there are values less than 0
        :raises TypeError: If the inputList is not an actual list
        """

        logging.basicConfig(filename='log.txt', level=logging.DEBUG)

        for i in self.myList:
            if i < 0:
                logging.warning("Negative value detected")
                raise ValueError('Negative value detected')
        if not isinstance(self.myList, list):
            logging.warning('Input is not a list')
            raise TypeError('Input is not a list')
        myMin = min(self.myList)
        myMax = max(self.myList)
        logging.debug(self.myList)
        logging.debug('Min value: %s', myMin)
        logging.debug('Max value: %s', myMax)
        maxMinTuple = (myMin, myMax)
        logging.info(maxMinTuple)
        self.maxMin = maxMinTuple

    def find_maxDiff(self):
        """
        Finds maximum difference between two adjacent numbers in a list

        :param my_list: Is a list of numbers
        :returns: Largest difference between two adjacent numbers
        :raises ValueError: If my_list has 0 or 1 elements
        :raises ImportError: If numpy is not installed in environment
        :raises TypeError: If element in list is not an int, float, or complex
        """

        logging.basicConfig(filename='log.txt', level=logging.DEBUG)

        logging.info('Finding max difference between adjacent values in list')
        logging.debug('Printing %s', str(self.myList))
        n = 0
        if len(self.myList) < 2:
            logging.warning('Not enough values to calculate difference')
            raise ValueError('List too small, no difference to compare!')
        for i in range(len(self.myList) - 1):
            if(isinstance(self.myList[i], (int, float, complex)) and
               isinstance(self.myList[i + 1], (int, float, complex))):
                diff = abs(self.myList[i + 1] - self.myList[i])
                diff = abs(self.myList[i + 1] - self.myList[i])
                if diff > n:
                    n = diff
                else:
                    raise TypeError(
                        'List elements must be int, float, or complex!')
        logging.debug('Returns %s', str(n))
        self.maxDiff = n
