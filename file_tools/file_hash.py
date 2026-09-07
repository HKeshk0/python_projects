import hashlib
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="Enter file name.")
    parser.add_argument(
        "--algorithm", 
        choices=["md5","sha256","sha1","all"], 
        default="all", 
        help="Select the hashing algorithm."
        )
    args = parser.parse_args()

    filename = args.filename

    results = calculate_hashes(filename, args.algorithm)
    print_hashes(args.algorithm, results)


def calculate_hashes(filename, algorithm):
    results = []
    hashes = {}

    if algorithm in ("md5", "all"):
        hashes["md5"] = hashlib.md5()
    if algorithm in ("sha256", "all"):
        hashes["sha256"] = hashlib.sha256()
    if algorithm in ("sha1", "all"):
        hashes["sha1"] = hashlib.sha1()


    try:
        with open(filename,"rb") as file:
            while chunk := file.read(4096):
                for i in hashes.values():
                    i.update(chunk)
                
            print(f"File: {file.name}")
    except FileNotFoundError:
        print(f"File '{filename}' Doesn't Exist")
        raise SystemExit(1)

    for i in hashes.values():
        results.append(i.hexdigest())
    return results



def print_hashes(algorithm, results):
    if algorithm == "md5":
        print(f"MD5: {results[0]}")
    elif algorithm == "sha256":
        print(f"SHA256: {results[0]}")
    elif algorithm == "sha1":
        print(f"SHA1: {results[0]}")
    else:
        print(f"MD5: {results[0]}")
        print(f"SHA256: {results[1]}")
        print(f"SHA1: {results[2]}")


if __name__ == "__main__":
    main()