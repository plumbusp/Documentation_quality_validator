import csv
from datetime import datetime

def loadDocumentsStats(filePath, fileDelimiter):
    with open(filePath, 'r') as file:
        fileReader = csv.DictReader(file, delimiter=fileDelimiter)
        return list(fileReader)

def performAndPrintAnalysis(documents_stats, lower_bound):
    outputHolder = {}
    
    checkForDublicates(documents_stats, outputHolder)
    findMissingVersions(documents_stats, outputHolder)
    findOldUpdates(documents_stats, lower_bound, outputHolder)

    print(" Problems found:")
    problemsCount = sum(len(problems) for problems in outputHolder.values())
    if problemsCount == 0:
        print("    No problems found.")
        return 
    
    for doc_id, problems in outputHolder.items():
        if problems:
            print(f"    Document ID: {doc_id}")
            for problem in problems:
                print(f"      - {problem}")


def findMissingVersions(documents_stats, output_holder):
    for document in documents_stats:
        if document["version"] == "":
            output_holder.setdefault(document["doc_id"], []).append("The doc is missing version information")

def findOldUpdates(documents_stats, lower_bound, output_holder):
    year, *rest = lower_bound.split(".")
    month = rest[0] if rest else "1" 
    day = rest[1] if len(rest) > 1 else "1"

    startEligibleDate = datetime(int(year), int(month), int(day))
    for document in documents_stats:
        d_year, d_month, d_day = document["last_updated"].split("-")
        updateTime = datetime(int(d_year), int(d_month), int(d_day))
        if updateTime < startEligibleDate:
            output_holder.setdefault(document["doc_id"], []).append((f"Was updated at {updateTime} ({startEligibleDate - updateTime} old from the lower bound)"))

def checkForDublicates(documents_stats, output_holder):
    seen = set()
    for document in documents_stats:
        doc_id = document["doc_id"]
        if doc_id in seen:
            output_holder.setdefault(doc_id, []).append(f"Duplicate document ID ({doc_id}) found")
        else:
            seen.add(doc_id)
