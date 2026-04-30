from blocktype import BlockType


def block_to_block_type(block):
    if block[0] > 0 and block[0] < 7 and block[1] == "#":
        return BlockType.H
    if block[:3] == "```\n" and block[-3:] == "```":
        return BlockType.C

    sections = block.split("\n")
    if block[0] == ">":
        for section in sections:
            if len(section) == 0:
                continue
            if section[0] != ">":
                return BlockType.P
        return BlockType.Q

    if block[:1] == "- ":
        for section in sections:
            if len(section) == 0:
                continue
            if section[:1] != "- ":
                return BlockType.P
        return BlockType.UL

    if block[:2] == "1. ":
        line = 1
        for section in sections:
            if len(section) == 0:
                continue
            if section[0] != line or section[1:2] != ". ":
                return BlockType.P
            line += 1
        return BlockType.OL

    return BlockType.P
