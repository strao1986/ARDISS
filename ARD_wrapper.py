import argparse
import FALCO

def main():
    # my code here
    # Set up the parsing of command-line arguments
    parser = argparse.ArgumentParser(description="Impute using Automatic Relevance Determination")
    parser.add_argument("--typed", required=True,
                        help="Filename for the typed values.")
    parser.add_argument("--haps", required=True,
                        help="Filename for the reference SNPs values.")
    parser.add_argument("--out", required=True,
                        help="Path to the output file")
    parser.add_argument("--pop", required=True,
                        help="Path to the population file")
    parser.add_argument("--markers", required=True,
                        help="Path to the markers file")
    parser.add_argument("--masked", required=False, default="",
                        help="Path to the masked file")
    parser.add_argument("--lr", required=False, default=0.1, type=float,
                        help="Learning rate")
    parser.add_argument("--lr_decay", required=False, default=0.9, type=float,
                        help="Learning rate decay value")
    parser.add_argument("--gamma", required=False, default=0.005, type=float,
                        help="Gamma for the mixed rbf")
    args = parser.parse_args()

    print("lr: "+ str(args.lr))
    print("lr_decay: "+ str(args.lr_decay))

    FALCO.impute_ard(args.typed, args.haps, args.out, args.pop, args.markers, masked_file=args.masked, window_size=100, maf=0, lr=args.lr, lr_decay=args.lr_decay, gamma=args.gamma)

if __name__ == "__main__":
    main()