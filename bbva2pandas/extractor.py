import re

YEAR_FIND_REGEX = re.compile(r'EXTRACTO DE \w* (\d{4})', re.MULTILINE)

MOVEMENTS_PARSE_REGEX = re.compile(
    r'''^
    (\d\d/\d\d) #date
    \s
    (\d\d/\d\d) #value date
    \s*
    ([\wÀ-ÿ .,:*%\'\/()\-\\]+?) #concept
    \s+
    (-?\d*.?\d*,\d*) #amount of the movement
    \s*
    (\d*.?\d*,\d*) #balance after movement
    \s*
    (\d*) # credit card number
    \s*
    ([\wÀ-ÿ .,:*%\'\/()\-\\]*) # subconcept
    $''',
    re.MULTILINE | re.IGNORECASE | re.VERBOSE
)


def find_movements(content: str) -> list:
    """Searches the file content for movements"""
    return MOVEMENTS_PARSE_REGEX.findall(content)


def find_year(content: str) -> str:
    """Extracts the year from file content"""
    return YEAR_FIND_REGEX.findall(content)[0]
