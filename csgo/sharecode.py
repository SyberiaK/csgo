import re

dictionary = 'ABCDEFGHJKLMNOPQRSTUVWXYZabcdefhijkmnopqrstuvwxyz23456789'
DICTIONARY_LENGTH = len(dictionary)
CODE_PATTERN = re.compile(r'CSGO(-[{%s}]{5}){5}$' % dictionary)

_bitmask64 = 2 ** 64 - 1


def _swap_endianness(number):
    result = 0

    for n in range(0, 144, 8):
        result = (result << 8) + ((number >> n) & 0xFF)

    return result


def decode(code):
    """
    Decodes a match share code

    :param code: match share code (e.g. ``CSGO-Ab1cD-xYz23-7bcD9-uVZ23-12aBc``)
    :type code: str
    :raises: :class:`ValueError`
    :return: dict with matchid, outcomeid and token
    :rtype: dict

    .. code:: python

        {'matchid': 0,
         'outcomeid': 0,
         'token': 0
         }
    """
    if not CODE_PATTERN.match(code):
        raise ValueError('Invalid share code')

    code = code.removeprefix('CSGO').replace('-', '')

    num = 0
    for c in reversed(code):
        num = num * DICTIONARY_LENGTH + dictionary.index(c)

    num = _swap_endianness(num)

    return {'matchid': num & _bitmask64,
            'outcomeid': num >> 64 & _bitmask64,
            'token': num >> 128 & 0xFFFF}


def encode(matchid, outcomeid, token):
    """Encodes (matchid, outcomeid, token) to match share code

    :param matchid: match id
    :type matchid: int
    :param outcomeid: outcome id
    :type outcomeid: int
    :param token: token
    :type token: int
    :return: match share code (e.g. ``CSGO-Ab1cD-xYz23-7bcD9-uVZ23-12aBc``)
    :rtype: str
    """
    num = _swap_endianness((token << 128) | (outcomeid << 64) | matchid)

    code = ''
    for _ in range(25):
        num, r = divmod(num, DICTIONARY_LENGTH)
        code += dictionary[r]

    return f'CSGO-{code[:5]}-{code[5:10]}-{code[10:15]}-{code[15:20]}-{code[20:]}'
