from app.utils import clean_data, compute_statistics

if __name__ == "__main__":
    data = [1, -2, None, 5, 10]

    cleaned = clean_data(data)
    stats = compute_statistics(cleaned)

    print("Final Stats:", stats)