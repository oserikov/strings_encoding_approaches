from abstract_strings_coder import StringsCoder


class ToyTranslitCaesarStringsCoder(StringsCoder):
    """
    a toy class to encode a string written in a subset {абвгдеиклмно} of cyrillic with
    performing a caesar shift of specified length and then transliterating the result.
    if the shift length is zero then just transliterates.

    if `shift_length` is 1 then encoded "окно" is "aloa"

    if `shift_length` is 0 then encoded "нога" is "noga"
    """

    SOURCE_ALPHABET = "абвгдеиклмно"
    TARGET_ALPHABET = "abvgdeiklmno"

    def __init__(self, caesar_shift=0):
        self.caesar_shift = caesar_shift

    def encode(self, string_to_encode) -> str:
        assert all([c in self.SOURCE_ALPHABET for c in string_to_encode])

        result = ""
        for char_to_encode in string_to_encode:
            caesar_idx = (self.SOURCE_ALPHABET.index(char_to_encode) + self.caesar_shift) % len(self.SOURCE_ALPHABET)

            translit_caesar_char = self.TARGET_ALPHABET[caesar_idx]

            result += translit_caesar_char

        return result

    def decode(self, string_to_decode) -> str:
        assert all([c in self.TARGET_ALPHABET for c in string_to_decode])

        result = ""
        for idx, char_to_decode in enumerate(string_to_decode):
            original_idx = (self.TARGET_ALPHABET.index(char_to_decode) - self.caesar_shift) % len(self.TARGET_ALPHABET)

            original_char = self.SOURCE_ALPHABET[original_idx]

            result += original_char

        return result
