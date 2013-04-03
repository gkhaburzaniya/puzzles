def matrix(height, width, value = None):
    """Return a list of lists representing a matrix."""
    function = value
    if not callable(value):
        function = lambda x, y: value
    return [[function(x, y) for x in range(height)] for y in range(width)]
