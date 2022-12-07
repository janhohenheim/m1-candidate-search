from typing import List


def read_file(file: str) -> str:
    """Reads a file and returns a string"""
    with open(file, "r") as f:
        return f.read()


def split_fasta(fasta: str, n: int) -> List[str]:
    """Splits a fasta file into n parts"""
    length = len(fasta)
    split_length = length // n
    split_fasta = []
    for i in range(n):
        print(f"Splitting {i + 1} of {n}")
        begin_of_next_sequence = fasta.find(">", (i + 1) * split_length)
        end = False
        if begin_of_next_sequence == -1:
            begin_of_next_sequence = length
            end = True
        split_fasta.append(fasta[i * split_length : begin_of_next_sequence])
        if end:
            break
    return split_fasta


def write_file(name, content):
    """Writes a file"""
    with open(name, "w") as f:
        f.write(content)


fasta = read_file("data/MI_contigs_canu.fa")
split_fasta = split_fasta(fasta, 6)
for i, subfasta in enumerate(split_fasta):
    write_file("m1_{}.fasta".format(i), subfasta)
