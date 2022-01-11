

# Corona_Gene
DNA = '''ATGTACTCATTCGTTTCGGAAGAGACAGGTACGTTAATAGTTAATAGCGTACTTCTTTTTCTTGCTTTCG
TGGTATTCTTGCTAGTTACACTAGCCATCCTTACTGCGCTTCGATTGTGTGCGTACTGCTGCAATATTGT
TAACGTGAGTCTTGTAAAACCTTCTTTTTACGTTTACTCTCGTGTTAAAAATCTGAATTCTTCTAGAGTT
CCTGATCTTCTGGTCTAA'''

# Rattus norvegicus Rhox homeobox family member 11 (Rhox11), mRNA

# DNA = '''acctgttgagctgcctgcaggccgtagagtgtgcgttgggtttctagattttatgagccatcactcaggctgagatagactttggtgacgaagctgtctttgagtcatctctgctcctgtaagcaacccct
# cgcccatattcctattccaccatggctctccaatcccatcatgtggagcccagttcctacaaactggaggaaaatgagatcgaggtgagccttgatgctgatgaagcagcagagggaggcagcttcggagaaggttctctaaat
# ggctcagacaaactaaagtacgagggcatcccagacaaggatgataggatctacgttggagacgtgaagtacattggtaatgacgtcaaagatgagtaccgtgggagccaccaagggtccggagattcacagctggaggagcag
# aagaacttggcttctcccacaatcccacagttccggcgcacaaggccacggatccagttgggtctcacgcccaggcagctgagtgaactggaagacttttttgaaactactaagtacccggatgtgatcacgagaagaaacctc
# gcaaagcacttgtacctggcagaatccagagtgaagagatggtttaagagaagaagagcagatacaggaaagaacagcagactcaaatgctcaagcgagcatctgctgataggtagaagaatgccatgcaacaaagcttttgga
# ggagtcctgaagcatcttcctgtccaggcatcagatgaaggcacgttaggcactaatactcccc'''

DNA = DNA.upper()

# Expected_Protein = "MALQSHHVEPSSYKLEENEIEVSLDADEAAEGGSFGEGSLNGSDKLKYEGIPDKDDRIYVGDVKYIGNDVKDEYRGSHQGSGDSQLEEQKNLASPTIPQFRRTRPRIQLGLTPRQLSELEDFFETTKYPDVITRRNLAKHLYLAESRVKRWFKRRRARYRKEQQTQMLKRASADR"

# Corona_Expected Protein
Expected_Protein = "YMSKQSLLCPCNYQLSHEEKERKHHKNDQCDR"


RNA_Codons = {
    # 'M' - START, '*' - STOP
    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "UGU": "C", "UGC": "C",
    "GAU": "D", "GAC": "D",
    "GAA": "E", "GAG": "E",
    "UUU": "F", "UUC": "F",
    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G",
    "CAU": "H", "CAC": "H",
    "AUA": "I", "AUU": "I", "AUC": "I",
    "AAA": "K", "AAG": "K",
    "UUA": "L", "UUG": "L", "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
    "AUG": "M",
    "AAU": "N", "AAC": "N",
    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAA": "Q", "CAG": "Q",
    "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R",
    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S", "AGU": "S", "AGC": "S",
    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
    "UGG": "W",
    "UAU": "Y", "UAC": "Y",
    "UAA": "*", "UAG": "*", "UGA": "*"
}

# RNA Tracription

DNA_Arranged = DNA.replace("\n", "")
# print(f"\nThe DNA Sequence is : \n\n{DNA_Arranged}")

RNA_Match = DNA_Arranged.maketrans("ATGC", "UACG")
RNA = DNA_Arranged.translate(RNA_Match)

# print(f"\nThe RNA Sequence is: \n\n{RNA}")

# RNA Translation

Actual_Protein = ""

for i in range(0, len(RNA), 3):
    codons = RNA[i:i+3]
    if RNA_Codons[codons] != "*" or RNA_Codons[codons] != "*" or RNA_Codons[codons] != "*":
        # print(codons)
        Actual_Protein += RNA_Codons[codons]
    else:
        break
print(f"\nThe Protein Sequence is: \n\n{Actual_Protein}")
if Expected_Protein == Actual_Protein:
    print("The Protein Matches")
