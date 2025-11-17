"""
This module provides basic file operations and data manipulation utilities.
"""


def read_file(path):
    """
    Reads content from a file.
    
    Args:
        path (str): The file path to read from.
        
    Returns:
        str: The content of the file.
        
    Raises:
        FileNotFoundError: If the file does not exist.
        IOError: If an error occurs while reading the file.
    """
    pass


def write_file(path, content, append=False):
    """
    Writes or appends content to a file.
    
    Args:
        path (str): The file path to write to.
        content (str): The content to write to the file.
        append (bool, optional): If True, append to the file; if False, overwrite. 
                                Defaults to False.
    
    Returns:
        bool: True if the operation was successful, False otherwise.
        
    Raises:
        IOError: If an error occurs while writing to the file.
    """
    pass


def process_text(text, uppercase=False, remove_spaces=False):
    """
    Processes text with various transformations.
    
    Args:
        text (str): The input text to process.
        uppercase (bool, optional): If True, convert text to uppercase. Defaults to False.
        remove_spaces (bool, optional): If True, remove all whitespace. Defaults to False.
    
    Returns:
        str: The processed text.
        
    Raises:
        TypeError: If text is not a string.
    """
    pass


def merge_lists(*lists):
    """
    Merges multiple lists into a single list.
    
    Args:
        *lists: Variable length argument list of lists to merge.
    
    Returns:
        list: A new list containing all elements from input lists in order.
        
    Example:
        >>> merge_lists([1, 2], [3, 4], [5, 6])
        [1, 2, 3, 4, 5, 6]
    """
    pass


def filter_data(data, key=None, reverse=False):
    """
    Filters and sorts data based on criteria.
    
    Args:
        data (list): The data to filter.
        key (callable, optional): A function of one argument that is used to extract 
                                 a comparison key. Defaults to None.
        reverse (bool, optional): If True, sort in descending order. Defaults to False.
    
    Returns:
        list: A new filtered and sorted list.
        
    Raises:
        TypeError: If data is not a list.
    """
    pass
