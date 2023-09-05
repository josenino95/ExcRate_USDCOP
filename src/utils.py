from suds.client import Client as SudsCLient
from typing import Tuple
import datetime

def trm(date: datetime.date) -> Tuple[datetime.date, datetime.date, float, str]:
    """
    Fetch the TRM (Tasa Representativa del Mercado) value for a given date from the Superfinanciera service.

    This function communicates with the Superfinanciera's TCRM (Tasa Representativa del Mercado) service to get 
    the TRM details for a specified date. If there's any issue during the request or processing, the function 
    returns the error message.

    Parameters
    ----------
    date : datetime.date
        The date for which to fetch the TRM details.

    Returns
    -------
    Tuple[datetime.date, datetime.date, float, str]
        A tuple containing:
        - validityFrom (datetime.date): The starting date of validity for the TRM value.
        - validityTo (datetime.date): The ending date of validity for the TRM value.
        - value (float): The TRM value.
        - message (str): Any additional message provided by the service. If there's no message, returns an empty string.

    Raises
    ------
    Exception
        If there's any issue during the request or processing.

    Notes
    -----
    Base code obtained from Cristiam Diaz Gist:
    https://gist.github.com/cdiaz/a623334ee994a836cba3

    References
    ----------
    Superfinanciera's TCRM service:
    https://www.superfinanciera.gov.co/SuperfinancieraWebServiceTRM/TCRMServicesWebService/TCRMServicesWebService?WSDL
    """
    WSDL_URL = 'https://www.superfinanciera.gov.co/SuperfinancieraWebServiceTRM/TCRMServicesWebService/TCRMServicesWebService?WSDL'
    try:
        client = SudsCLient(WSDL_URL, location=WSDL_URL, faults=True)
        trm_result = client.service.queryTCRM(date)
    except Exception as e:
        return str(e)

    validityFrom = trm_result['validityFrom']
    validityTo = trm_result['validityTo']
    value = trm_result['value']
    try:
        message = trm_result['message']
    except AttributeError:
        message = ""

    return validityFrom, validityTo, value, message