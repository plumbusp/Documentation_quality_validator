import sys
import documentValidator

if __name__ == "__main__":
    if "--help" in sys.argv or "-h" in sys.argv:
        print("Usage: python main.py <file_to_process> <file_delimiter> <lower_bound_for_updates>")
        print("     <csv_file> -> path to your CSV \n   <delimiter> -> CSV separator\n  <lower_bound> -> lower bound for checking document' update times (format: YYYY.MM.DD, YYYY.MM or YYYY)")

    if len(sys.argv) != 4:
        print("Usage: python main.py <file_to_process> <file_delimiter> <lower_bound_for_updates>")
        print("Print --help for the information.")
        print("")
        sys.exit(1)

    file_path = sys.argv[1]
    file_delimiter = sys.argv[2]
    documents_stats= documentValidator.loadDocumentsStats(file_path, file_delimiter)
    performAnalysis = documentValidator.performAndPrintAnalysis(documents_stats, sys.argv[3])
