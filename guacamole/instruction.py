import itertools
import six

from builtins import str as __unicode__

from guacamole.exceptions import InvalidInstruction


INST_TERM = ';'  # instruction terminator character
ARG_SEP = ','  # instruction arg separator character
ELEM_SEP = '.'  # instruction arg element separator character (e.g. 4.size)

# @TODO: enumerate instruction set


def utf8(unicode_str):
    """
    Return a utf-8 encoded string from a valid unicode string.

    :param unicode_str: Unicode string.

    :return: str
    """
    if six.PY2 and isinstance(unicode_str, __unicode__):
        return unicode_str.encode('utf-8')

    return unicode_str


class GuacamoleInstruction(object):

    def __init__(self, opcode, *args, **kwargs):
        self.opcode = opcode
        self.args = args

    @classmethod
    def load(cls, instruction):
        """
        Loads a new GuacamoleInstruction from encoded instruction string.

        :param instruction: Instruction string.

        :return: GuacamoleInstruction()
        """
        if not instruction.endswith(INST_TERM):
            raise InvalidInstruction('Instruction termination not found.')

        print(type(instruction))
        args = cls.decode_instruction(instruction)

        return cls(args[0], *args[1:])

    @staticmethod
    def decode_instruction(instruction):
        """
        Decode whole instruction and return list of args.
        Usually, returned arg[0] is the instruction opcode.

        example:
        >> args = decode_instruction('4.size,4.1024;')
        >> args == ['size', '1024']
        >> True

        :param instruction: Instruction string.

        :return: list
        """
        if not instruction.endswith(INST_TERM):
            raise InvalidInstruction('Instruction termination not found.')

        # Use proper encoding
        instruction = utf8(instruction)

        # Get arg size
        elems = instruction.split(ELEM_SEP, 1)

        try:
            arg_size = int(elems[0])
        except Exception:
            # Expected ValueError
            raise InvalidInstruction(
                'Invalid arg length.' +
                ' Possibly due to missing element separator!')

        arg_str = elems[1][:arg_size]

        remaining = elems[1][arg_size:]

        args = [arg_str]

        if remaining.startswith(ARG_SEP):
            # Ignore the ARG_SEP to parse next arg.
            remaining = remaining[1:]
        elif remaining == INST_TERM:
            # This was the last arg!
            return args
        else:
            # The remaining is neither starting with ARG_SEP nor INST_TERM.
            raise InvalidInstruction(
                'Instruction arg (%s) has invalid length.' % arg_str)

        next_args = GuacamoleInstruction.decode_instruction(remaining)

        if next_args:
            args = args + next_args

        return args

    @staticmethod
    def encode_arg(arg):
        """
        Encode argument to be sent in a valid GuacamoleInstruction.

        example:
        >> arg = encode_arg('size')
        >> arg == '4.size'
        >> True

        :param arg: arg string.

        :return: str
        """
        arg_utf8 = utf8(arg)

        return ELEM_SEP.join([str(len(str(arg_utf8))), str(arg_utf8)])

    def encode(self):
        """
        Prepare the instruction to be sent over the wire.

        :return: str
        """
        instruction_iter = itertools.chain([self.opcode], self.args)

        elems = ARG_SEP.join(self.encode_arg(arg) for arg in instruction_iter)

        return elems + INST_TERM

    def __str__(self):
        return self.encode()
