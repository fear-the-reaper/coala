from coalib.bearlib.languages.Language import Language


@Language
class Python:
    aliases = 'py',
    versions = 2.7, 3.3, 3.4, 3.5, 3.6

    extensions = '.py',
    comment_delimiters = '#',
    multiline_comment_delimiters = {}
    string_delimiters = {'"': '"', "'": "'"}
    multiline_string_delimiters = {'"""': '"""', "'''": "'''"}
    indent_types = ':',
    encapsulators = {'(': ')', '[': ']', '{': '}'}
    string_delimiter_escape = {'"': '\\"', "'": "\\'"}
    line_continuation = '\\'
