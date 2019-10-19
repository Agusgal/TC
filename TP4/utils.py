def maprange(a, b, s):
  """
    Linearly map a value 's' in a given range [a1, a2] to a value 't' in a range [b1, b2]

    Code based on https://rosettacode.org/wiki/Map_range

    Parameters
    ----------
    a: array_like
      Starting interval
    b: array_like
      Target interval
    s: float
      Value in the 'a' interval to be mapped in 'b'.

    Returns
    -------
    t: float
      Mapped value in 'b' range. 
    
    Raises
    ------
    ValueError
      If 's' is out of bounds from interval 'a'

    Examples
    --------  
    >>> s = 5
    >>> maprange([0,10],[0,100],5)
    50
    """
  (a1, a2), (b1, b2) = a, b
  #s must be in the interval [a1, a2]
  if a1 <= s <= a2:
    return  b1 + ((s - a1) * (b2 - b1) / (a2 - a1))
  else:
    raise ValueError(f'Value {s} is out of bounds')