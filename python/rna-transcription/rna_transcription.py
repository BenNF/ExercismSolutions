def to_rna(dna_strand):
    result = ""
    map = {
        'A' : 'U',
        'G' : 'C',
        'C' : 'G',
        'T' : 'A',
    }
    for x in dna_strand:
        if x not in "ACGT":
            raise ValueError("Invalid DNA strand input")
        result += map[x]
    return result

