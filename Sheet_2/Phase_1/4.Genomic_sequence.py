import json

def main():
    genomic_sequence = json.loads(input("Enter data: "))
    
    filtered_sequence = list(filter(lambda seq: 'TATA' in seq and (seq.count('G') + seq.count('C')) / len(seq) > 0.5, genomic_sequence))

    print(filtered_sequence)

main()

# seq has 'TATA' and 'G+C ratio in sequence > 0.5'